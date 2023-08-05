from __future__ import absolute_import
from __future__ import unicode_literals

from datetime import timedelta


from django import forms
from django.db.models import Q
from django.db.models.sql.constants import QUERY_TERMS
from django.utils import six
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import options
from django.db.models import fields as dbfields
from .fields import RangeField, LookupTypeField

__all__ = [
    'Filter', 'CharFilter', 'BooleanFilter', 'ChoiceFilter',
    'MultipleChoiceFilter', 'DateFilter', 'DateTimeFilter', 'TimeFilter',
    'ModelChoiceFilter', 'ModelMultipleChoiceFilter', 'NumberFilter',
    'RangeFilter', 'DateRangeFilter', 'AllValuesFilter',
]

LOOKUP_TYPES = sorted(QUERY_TERMS) + [
    'in_any', 'in_all', 'not_in_any', 'not_in_all']

LOOKUP_MAP = {
    'icontains' : _('contains'),
    'istartswith' : _('starts with'),
    'lt' : _('less then'),
    'gt' : _('grater then'),
    'lte' : _('less then or equal'),
    'gte' : _('grater then or equal'),
    'exact' : '',
    'range' : '',
    'in_any' : _('in any'),
    'in_all' : _('in all'),
    'not_in_any' : _('not in any'),
    'not_in_all' : _('not in all'),
}


class Filter(object):
    creation_counter = 0
    field_class = forms.Field
    widget = None
    
    def __init__(self, name=None, label=None, widget=None, action=None,
        lookup_type='exact', required=False, distinct=False, **kwargs):
        self.name = name
        self.label = label
        if action:
            self.filter = action
        self._lookup_type = lookup_type
        try:
            self.widget = widget or options.FORMFIELD_FOR_DBFIELD_DEFAULTS[self.dbfield]['widget']
        except (KeyError, AttributeError):
            self.widget = widget
        self.required = required
        self.extra = kwargs
        self.distinct = distinct
        self.creation_counter = Filter.creation_counter
        Filter.creation_counter += 1

    @property
    def lookup_type(self):
        return self._lookup_type

    @lookup_type.setter
    def lookup_type(self, value):
        # When redefining a lookup_type you need to regenerate the field
        # due to the part that holds the lookup choice
        self._lookup_type = value
        try:
            del self._field
        except:
            pass

    @property
    def field(self):
        if not hasattr(self, '_field'):
            if (self.lookup_type is None or
                    isinstance(self.lookup_type, (list, tuple))):
                if self.lookup_type is None:
                    lookup = [(x, LOOKUP_MAP.get(x, x)) for x in LOOKUP_TYPES]
                else:
                    lookup = [
                        (x, LOOKUP_MAP.get(x, x)) for x in self.lookup_type if x in LOOKUP_TYPES]
                self._field = LookupTypeField(self.field_class(
                    required=self.required, widget=self.widget, **self.extra),
                    lookup, required=self.required, label=self.label)
            else:
                self._field = self.field_class(required=self.required,
                    label=self.label, widget=self.widget, **self.extra)
        return self._field

    def filter(self, qs, value):
        if value in ([], (), {}, None, ''):
            return qs
        if isinstance(value, (list, tuple)):
            lookup = six.text_type(value[1])
            if not lookup:
                lookup = 'exact'  # fallback to exact if lookup is not provided
            value = value[0]
        else:
            lookup = self.lookup_type
        qs = qs.filter(**{'%s__%s' % (self.name, lookup): value})
        if self.distinct:
            qs = qs.distinct()
        return qs


class CharFilter(Filter):
    field_class = forms.CharField


class BooleanFilter(Filter):
    field_class = forms.NullBooleanField

    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{self.name: value})
        return qs


class ChoiceFilter(Filter):
    field_class = forms.ChoiceField


class MultipleChoiceFilter(Filter):
    """
    This filter preforms an OR query on the selected options.
    """
    field_class = forms.MultipleChoiceField

    def filter(self, qs, value):
        value = value or ()
        if value and self.lookup_type and not isinstance(self.lookup_type, basestring):
            value, choosen_lookup_type = value
        else:
            choosen_lookup_type = self.lookup_type
            
        # it's not true in general if a models field is not required (null=False)
        # if len(value) == len(self.field.choices):
        #     return qs
        q = Q()

        if choosen_lookup_type in ('in_all', 'not_in_all'):
            for v in value:
                q &= Q(**{self.name: v})
        else: 
            for v in value:
                q |= Q(**{self.name: v})

        if choosen_lookup_type in ('not_in_any', 'not_in_all'):
            return qs.exclude(q).distinct()
        else: 
            return qs.filter(q).distinct()
            


class DateFilter(Filter):
    field_class = forms.DateField
    dbfield = dbfields.DateField

class DateTimeFilter(Filter):
    field_class = forms.DateTimeField
    dbfield = dbfields.DateTimeField

class TimeFilter(Filter):
    field_class = forms.TimeField
    dbfield = dbfields.DateTimeField
  
class ModelChoiceFilter(Filter):
    field_class = forms.ModelChoiceField


class ModelMultipleChoiceFilter(MultipleChoiceFilter):
    field_class = forms.ModelMultipleChoiceField


class NumberFilter(Filter):
    field_class = forms.DecimalField


class RangeFilter(Filter):
    field_class = RangeField

    def filter(self, qs, value):
        if value:
            lookup = '%s__range' % self.name
            return qs.filter(**{lookup: (value.start, value.stop)})
        return qs


_truncate = lambda dt: dt.replace(hour=0, minute=0, second=0)


class DateRangeFilter(ChoiceFilter):
    options = {
        '': (_('Any date'), lambda qs, name: qs.all()),
        1: (_('Today'), lambda qs, name: qs.filter(**{
            '%s__year' % name: now().year,
            '%s__month' % name: now().month,
            '%s__day' % name: now().day
        })),
        2: (_('Past 7 days'), lambda qs, name: qs.filter(**{
            '%s__gte' % name: _truncate(now() - timedelta(days=7)),
            '%s__lt' % name: _truncate(now() + timedelta(days=1)),
        })),
        3: (_('This month'), lambda qs, name: qs.filter(**{
            '%s__year' % name: now().year,
            '%s__month' % name: now().month
        })),
        4: (_('Last month'), lambda qs, name: qs.filter(**{
            '%s__year' % name: now().year if now().month > 1 else now().year-1,
            '%s__month' % name: now().month-1 if now().month >= 2 else 12,
        })),
        5: (_('This year'), lambda qs, name: qs.filter(**{
            '%s__year' % name: now().year,
        })),
        6: (_('Last year'), lambda qs, name: qs.filter(**{
            '%s__year' % name: now().year-1,
        })),
    }

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [
            (key, value[0]) for key, value in six.iteritems(self.options)]
        super(DateRangeFilter, self).__init__(*args, **kwargs)

    def filter(self, qs, value):
        try:
            value = int(value)
        except (ValueError, TypeError):
            value = ''
        return self.options[value][1](qs, self.name)


class AllValuesFilter(ChoiceFilter):
    @property
    def field(self):
        qs = self.model._default_manager.distinct()
        qs = qs.order_by(self.name).values_list(self.name, flat=True)
        self.extra['choices'] = [(o, o) for o in qs]
        return super(AllValuesFilter, self).field
