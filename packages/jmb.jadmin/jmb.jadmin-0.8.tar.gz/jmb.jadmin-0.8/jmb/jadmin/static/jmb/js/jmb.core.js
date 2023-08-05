//NAME space di jmb 
if (window.jmb == undefined) window.jmb = {};

// vedi jmb.i18n.view
jmb.i18n_fix = function(c){
	
	if (jmb.catalog == undefined) jmb.catalog = [];
		if(typeof(django)!="undefined"){
			if(django.catalog){
				c = (c) ? c: django.catalog
				jmb.catalog.push(c)
				$.each(jmb.catalog, function(){
					django.catalog = $.extend(django.catalog, this);
				})
			}
		}
		if(typeof(catalog)!="undefined"){
			if(catalog){
				c = (c) ? c: catalog
				jmb.catalog.push(c)
				$.each(jmb.catalog, function(){
					catalog = $.extend(catalog, this);
			})
		}
	}
}


jmb.extra_action_fields_show = function(value){
	$(".extrafield").hide()
	$(".extrafield.action_"+value).show()
}

jmb.extra_action_fields_init = function(){
	 $(function(){
		 $('select[name=action]').change(function(e){
			 var value = $('select[name=action]').val()
			 jmb.extra_action_fields_show(value)
		 });
		 jmb.extra_action_fields_show($('select[name=action]').val())
	 });
}
// fissa a 10px la larghezza delle colonne edit/delete nella change-list
jmb.fix_width_edit_delete = function () {
    $(function(){
        $("[field=v], [field=e], [field=d]").parent("th").width("10px").css("textAlign","center")
    });
}
//nasconde i campi nascosti nella change-form, che hanno name initial
jmb.hide_input = function () {
    $(function(){
    	 $(".form-row div input[type=hidden]:not([name*='initial'])").parent("div").hide()
    	//$(".form-row div input[type=hidden]:not([name*='initial'])").parents(".form-row").hide()
    });
}

//funzione per le admin tab, colora di rosso se sono presenti errori e apre la tab giusta
jmb.error_tab = function () {
     $(function(){
        $(".admintab-content .tab-pane").each(function(){
            var errors = $(this).find(".errors").length
            var errorslist = $(this).find(".errorlist li").length
            if(errors || errorslist){ 
                $("a[href='#"+  $(this).attr("id")+"']").addClass("taberror")
                $("a[href='#"+  $(this).attr("id")+"']").append('<span class="badge badge-important">'+ (errors || errorslist) +'</span>')
            }
        })
     });
    
}

//funzione per le admintab per averle sempre fisse in alto anche se si scorre
jmb.stickytab = function () {
    $(function(){
        //https://github.com/garand/sticky
        $(".stickytab").sticky({topSpacing:1, bottomSpacing:1});
    });
}


//i link con classe iframe vengo aperti nel popup, e possibile avere una funzione di callback
jmb.iframe_hjson_link = function (callback) {
	if(typeof(callback) == "undefined") callback  = function(){}
    $(document).on("click", ".iframe", function () {
    	jmb.last_link = this
        link = $(this).attr("href")
	if (link.indexOf('?') < 0) {
           link += '?'
        } else {
           link += '&'
        }
    	origin = ($("body").hasClass("change-form")) ? "&_origin=change-form" : ""
    	origin = ($("body").hasClass("change-list")) ? "&_origin=change-list" : ""
        if ($(this).hasClass("hjson")) link += "_hjson=1&_popup=1" + origin;
    	if ($(this).hasClass("refresh")) link += "&_refresh=1";
        var title = $(this).attr("title")
        var width = $(this).attr("width")
        var height = $(this).attr("height")
        jmb.show_in_popup(link, title, width, height,callback)
        return false;
    });

}

jmb.auto_popup = function (classe,callback) {
	if (!(classe)) classe = 'a.iframe:not(.hjson)';
    jQuery(document).ready(function($) {
	    $(classe)
		    .click(
			    function() {
			        var src = $(this).attr("href")
			        suffix = (src.indexOf("?") !=-1) ?"&_popup=1" : "?_popup=1"
				    src+=  suffix
				    var title = $(this).attr("title")
				    var width = $(this).attr("width")
				    var height = $(this).attr("height")
				    jmb.show_in_popup(src, title, width, height,callback)
				    return false;
			    })
    })
}

//aggiunge un messaggio alla lista classe = {info|error}
//parametro add se true aggiunge alla lista, se false cancella tutto
jmb.add_message = function(text, classe,add){
	if($(".messagelist").length==0){
		$("#content").before('<ul class="messagelist"></ul>')
	}
	if(add){
		$(".messagelist").append('<li class="'+classe+'">'+ text +'</li>')
	}else{
		$(".messagelist").html('<li class="'+classe+'">'+ text +'</li>')
	}
}

//apre il popup
jmb.show_in_popup = function (src, title, width, height, callback) {

	if(typeof(callback) == "undefined") callback  = function(){}
    if (!(src)) return false;
    var title = title || " "
    var width = width || 1000
    var height = height || 500
    var iframe = $('<iframe id="popiframe" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>');

    dialog = $("<div></div>").append(iframe).appendTo("body")
    $(dialog).dialog({
        autoOpen: false,
        modal: true,
        resizable: true,
        width: "auto",
        height: "auto",
        close: function () {
            iframe.attr("src", "");
            callback()
        },
        open: function (event, ui) {
            iframe.attr({
                width: '100%',
                height: '90%'
            });
            iframe.parents(".ui-dialog").css(
                'width', width);
            $(".ui-dialog-content").css('overflow', 'hidden');
                
                
            $(".ui-dialog-titlebar-close").html("X")
            dialog.parent().height(parseInt(height) + 10)
            dialog.height(height)
        }
    });
    iframe.attr({
        width: +width,
        height: +height,
        src: src
    });
    $(dialog).dialog("option", "title", title)
    $(dialog).dialog("open");

    return true;
}

//funzione chiamata dal return delle pagine con hjson
jmb.iframe_callback = function(action, model, pk, content, message, method) {
    if (action == "change") {
        tr = $("<div></div>").append(content).find("tr")
        //aggiunge la checkbox e sostiutisce il tr con quello nuovo
        $(tr).prepend('<td class="action-checkbox"><input class="action-select" name="_selected_action" type="checkbox" value="'+pk+'"></td>')
        row = $(jmb.last_link).parents("tr")
        row.html(tr.html())
    }
    
    if (action == "add") {
       // da implementare in futuro
    }

    if (action == "delete") {
    	row = $(jmb.last_link).parents("tr")
        $(row).hide("slow", function() {
        	// ricolora blu e bianco le righe alternate
        	$(row).parents("tbody").find("tr:visible:even").addClass("row1").removeClass("row2")
        	$(row).parents("tbody").find("tr:visible:odd").addClass("row2").removeClass("row1")
        });
        
    }
    if(message){
    	//aggiunge il messaggio se presente
        if( $("ul.messagelist").length==0){
		    $(".breadcrumbs").after("<ul class='messagelist'></ul>")
	    }
	    $("ul.messagelist").html($("<li class='info'></li>").html(message))
	}
	if(typeof(dialog)!="undefined") dialog.dialog("close")
	
	if (method == "_json_continue"){
		//caso del salva e continua
		$(jmb.last_link).click()
    }
    if (method == "_addanother"){
    	row = $(jmb.last_link).parents("tr")
    	tr = $("<div></div>").append(content).find("tr")
        $(tr).prepend('<td class="action-checkbox"><input class="action-select" name="_selected_action" type="checkbox" value="'+pk+'"></td>')
    	$(row).after(tr);
    	$(row).parents("tbody").find("tr:visible:even").addClass("row1").removeClass("row2")
    	$(row).parents("tbody").find("tr:visible:odd").addClass("row2").removeClass("row1")
    }
    
}

iframe_callback = jmb.iframe_callback