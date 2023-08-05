/*! jquery.cookie v1.4.1 | MIT x il search in results */
!function(a){"function"==typeof define&&define.amd?define(["jquery"],a):"object"==typeof exports?a(require("jquery")):a(jQuery)}(function(a){function b(a){return h.raw?a:encodeURIComponent(a)}function c(a){return h.raw?a:decodeURIComponent(a)}function d(a){return b(h.json?JSON.stringify(a):String(a))}function e(a){0===a.indexOf('"')&&(a=a.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\"));try{return a=decodeURIComponent(a.replace(g," ")),h.json?JSON.parse(a):a}catch(b){}}function f(b,c){var d=h.raw?b:e(b);return a.isFunction(c)?c(d):d}var g=/\+/g,h=a.cookie=function(e,g,i){if(void 0!==g&&!a.isFunction(g)){if(i=a.extend({},h.defaults,i),"number"==typeof i.expires){var j=i.expires,k=i.expires=new Date;k.setTime(+k+864e5*j)}return document.cookie=[b(e),"=",d(g),i.expires?"; expires="+i.expires.toUTCString():"",i.path?"; path="+i.path:"",i.domain?"; domain="+i.domain:"",i.secure?"; secure":""].join("")}for(var l=e?void 0:{},m=document.cookie?document.cookie.split("; "):[],n=0,o=m.length;o>n;n++){var p=m[n].split("="),q=c(p.shift()),r=p.join("=");if(e&&e===q){l=f(r,g);break}e||void 0===(r=f(r))||(l[q]=r)}return l};h.defaults={},a.removeCookie=function(b,c){return void 0===a.cookie(b)?!1:(a.cookie(b,"",a.extend({},c,{expires:-1})),!a.cookie(b))}});

jQuery(document).ready(function($) {


    // sposta i menu lookup-type nel td sotto la label
     $(".lookupselect").each(function(){
            $(this).parent("td").prev("td").append("<br/>").append(this)
       })
  
    //sistema per ricordare la scelta del search
    // in results
    sis1 = $.cookie('sis1')
    sis2 = $.cookie('sis2')
    if (sis1 === "0"){
        $("#sis1").attr("checked",false)
    }
    if (sis2 === "0"){
        $("#sis2").attr("checked",false)
    }
    $('#sis1').change(function(){
        check =  $("#sis1").attr("checked")
        check = (check == "checked") ? 1 : 0;
        $.cookie('sis1',check)
    });
    $('#sis2').change(function(){
        check =  $("#sis2").attr("checked")
        check = (check == "checked") ? 1 : 0;
        $.cookie('sis2', check)
    });

    //bottone reimposta
    $("#breset").on("click", function(){
        $("#search_form").find("input, option, select").not('.noreset').removeAttr('checked').removeAttr('selected').val("");
        $("#search_form").find('select[multiple!=multiple] option:first').attr('selected',true);
        
        return false
    })

    //gestione del search in results
    $("#changelist-search").on("submit", function(e) {
            if( $("#sis1").attr('checked') == undefined ){
                q = $(this).find("[name=q]").val()
                location.href = window.document.URL.split("?")[0] + "?q=" + q
                return false
            }
    });
    
    
    //hide the all of the element with class msg_body
    $("#search_form_body").hide();
    //toggle the componenet with class msg_body
    $("#search_form_head, #toggle_advanced_search").click(function()
        {
            $("#search_form_body").slideToggle(500);
  	    return false;
        }
    );

    $("#search_form").bind("keypress", function(e) {
        if (e.keyCode == 13) {
            go_search();
            return false;
         }
    });

    $('#bsearch').click(function() {
            go_search();
    });

    /* Advanced search form should be initially closed */
    $('#changelist-filter').hide('fast');
    $('#changelist').removeClass('filtered');

    $('#toggle_filters').click(function() {
        $('#changelist-filter').slideToggle(500);
        $('#changelist').toggleClass('filtered');
	return false;
    });
});


function go_search() {
    // we don't want empty values to pollute GET URL
    var f = $('#search_form').find('input, select').filter(function() {
      return $(this).val();
    })
    //filtro per togliere i menu lookup se non servono
    f = $(f).filter(function(){
        if(!($(this).hasClass("lookupselect"))){ return true}
        tdn = $(this).parent().next()
        sel = tdn.find("select").first()
        inp = tdn.find("input").first()

        if(sel.length){
             if(!(sel.val())){
                 return false
              } 
         }
        if(inp.length){
             if(!(inp.val())){
                return false
             } 
         }
        return true
    })
    
    if( $("#sis2").attr("checked") == undefined ){
        var new_location = "?" + f.serialize();
    }else{
        var new_location = "?" + f.serialize() + '&' + get_other_filters(); // may end with '&'
    } 
        
    window.location = new_location.replace(/&$/, '');
}

function get_other_filters(){
    // we need to preserve all choices made with standard admin search
    // and filter. We preserve anything that we don't "own" in the search-form
    // apart from pagination that needs to be reset each time
    var result = [];
    var tokens = location.search.slice(1).split('&');
    var keys = get_my_names();

    for (var i = 0; i < tokens.length; ++i) {
        var key = tokens[i].split('=');
        if (keys.indexOf(key[0]) == -1) {
            //modifica per  search in results
                if(tokens[i].indexOf("q=") == -1 ){
                        result.push(tokens[i]);
                }
        }
    }
    return result.join('&');
}

function get_my_names(){
    var form = $('#search_form');
    var keys = ['p'];  // page must be reset anyhow: it's a new select
    $('#search_form').find(':input').each(function(){keys.push(this.name)});
    return keys
}
