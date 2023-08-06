/* Jquery function ************************************************************/
jQuery(function($) {
    // Gallery image links
    $("a.gal").colorbox({rel:'a.gal'});
    $("section.post article a.main-image").colorbox();

    // Gallery video close
    $('#modal-video .close').click(function() {
        $('video').each(function(){this.player.pause()})
    });

    // CSRF ready for AJAX POSTS
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});


/* COOKIES ********************************************************************/

function enableCookieMenu() {
    if($.cookie("selected") != undefined && $.cookie("selected") != '') {
        console.log($.cookie("selected"));
        $("#cookiemenu").addClass('inline-block');
        $("#cookiemenu").removeClass('hidden');
        $(".cookiemenu-wrap .advice").addClass('show');
        $(".cookiemenu-wrap .advice").removeClass('hidden');
        $(".cookiemenu-wrap .advice").html($.cookie("selected").split(",").filter(Number).length + ' photos selected, <a onclick="removeSelection();return false;" href="">remove selection</a>')
    } else {
        $("#cookiemenu").addClass('hidden');
        $("#cookiemenu").removeClass('inline-block');
        $(".cookiemenu-wrap .advice").addClass('hidden');
        $(".cookiemenu-wrap .advice").removeClass('show');
    }
}

function removeSelection() {
    cookies = $.cookie("selected").split(",").filter(Number);
    cookies.forEach(function(cookie) {
        disableCookieItem(cookie);
    });
    $.removeCookie('selected', { path: '/' });
    enableCookieMenu();
}

function enableCookieItem(id) {
    $(".image-"+id).addClass('cookie-selected');
    $("#selectedbutton-"+id).addClass('btn-success');$("#selectedbutton-"+id).removeClass('btn-default');
    $("#selectedbutton-"+id+' i').addClass('fa-check-square-o');$("#selectedbutton-"+id+' i').removeClass('fa-square-o');
}

function disableCookieItem(id) {
    $(".image-"+id).removeClass('cookie-selected');
    $("#selectedbutton-"+id).addClass('btn-default');$("#selectedbutton-"+id).removeClass('btn-success');
    $("#selectedbutton-"+id+' i').addClass('fa-square-o');$("#selectedbutton-"+id+' i').removeClass('fa-check-square-o');
}

function loadCookies() {
    if($.cookie("selected") != undefined && $.cookie("selected") != '') {
        cookies = $.cookie("selected").split(",").filter(Number);
        cookies.forEach(function(cookie) {
            enableCookieItem(cookie);
        });
    }
    enableCookieMenu();
}

function updateCookie(id) {

    if($.cookie("selected") == undefined) {
        $.cookie('selected', id+',', { path: '/' });
        enableCookieItem(id);
        $(".image-"+id).addClass('cookie-selected');
        $("#selectedbutton-"+id).addClass('btn-success');$("#selectedbutton-"+id).removeClass('btn-default');
        $("#selectedbutton-"+id+' i').addClass('fa-check-square-o');$("#selectedbutton-"+id+' i').removeClass('fa-square-o');
    } else {
        if($.cookie("selected").indexOf(id+',') != -1) {
            $.cookie('selected', $.cookie("selected").replace(id+',', ''), { path: '/' });
            disableCookieItem(id);
        } else {
            $.cookie('selected', $.cookie("selected")+id+',', { path: '/' });
            enableCookieItem(id);
        }
    }
    enableCookieMenu();
}

/* AJAX ***********************************************************************/

function ajaxDelete(id, url) {
    // Default values
    id = id || ""
    url = url || ""

    // If id is empty and there are cookies
    if(id == "" && $.cookie("selected") != undefined && $.cookie("selected") != '') {
        id = JSON.stringify($.cookie("selected").split(",").filter(Number));
    }
    $.ajax({
        async:false,
        type:"GET",
        dataType: "json",
        url: url,
        data: {
            pk: id,
        },
        success: function(data){
            if(data.multiple==0) {
                $('.image-'+id).remove();
            }
            if(data.multiple==1) {
                jQuery.each(data.pk, function(k, v) {
                    $('.image-'+v).remove();
                });
            }
            removeSelection();
        }
    });
}

function ajaxDownload(url) {
    // If there are cookies
    if($.cookie("selected") != undefined && $.cookie("selected") != '') {
        id = $.cookie("selected").split(",").filter(Number);
        window.location.replace(url+"?id="+id);
    }
}

function enableAjaxItem(id) {
    $('#photowrap-'+id).removeClass('active');
    $('#photowrap-'+id).addClass('inactive');
    $('#status-'+id+' i').removeClass('fa-check-circle-o');
    $('#status-'+id+' i').addClass('fa-circle-o');
}

function disableAjaxItem(id) {
    $('#photowrap-'+id).removeClass('inactive');
    $('#photowrap-'+id).addClass('active');
    $('#status-'+id+' i').removeClass('fa-circle-o');
    $('#status-'+id+' i').addClass('fa-check-circle-o');
}


function ajaxChangeStatus(id, status, url) {
    // Default values
    id = id || ""
    status = status || "False"
    url = url || ""

    if(status == "False") {
        status = 0;
    }
    if(status == "True") {
        status = 1;
    }

    // If id is empty and there are cookies
    if(id == "" && $.cookie("selected") != undefined && $.cookie("selected") != '') {
        id = JSON.stringify($.cookie("selected").split(",").filter(Number));
    }
    $.ajax({
        async:false,
        type:"GET",
        dataType: "json",
        url: url,
        data: {
            pk: id,
            status: status,
        },
        success: function(data){
            if(data.multiple==0) {
                if(data.status==0) {
                    enableAjaxItem(id);
                }
                else {
                    disableAjaxItem(id);
                }
            }
            if(data.multiple==1) {
                jQuery.each(data.pk, function(k, v) {
                    if(data.status==0) {
                        enableAjaxItem(v);
                    }
                    else {
                        disableAjaxItem(v);
                    }
                });
            }
        }
    });
}

function ajaxTags(id, url) {
    // Default values
    id = id || ""
    url = url || ""

    // If id is empty and there are cookies
    if(id == "" && $.cookie("selected") != undefined && $.cookie("selected") != '') {
        id = JSON.stringify($.cookie("selected").split(",").filter(Number));
        tags = JSON.stringify($("#s2-0").select2("val"));
    }
    else {
     tags = JSON.stringify($("#s2-"+id).select2("val"));
    }
    $.ajax({
        async:false,
        type:"POST",
        dataType: "json",
        url: url,
        data: {
            pk: id,
            tags: tags,
        },
        success: function(data){
            if(data.multiple==0) {
                $("#imagemodal-"+id).modal('hide');
                $("#listags-"+id).html(data.html);
            }
            if(data.multiple==1) {
                jQuery.each(data.pk, function(k, v) {
                    $("#imagemodal-0").modal('hide');
                    selector = 'html-'+v;
                    $("#listags-"+v).html(data[selector]);
                });
            }
        }
    });
}

function ajaxVideo(id, url) {
    $.ajax({
        async:false,
        type:"POST",
        dataType: "text",
        url: url,
        data: {
            pk: id,
        },
        success: function(data){
            $("#modal-video .modal-body").html(data);
            $("#modal-video").modal('show');
        }
    });
}

function ajaxMkThumb(url) {
    $.ajax({
        async:false,
        type:"GET",
        dataType: "json",
        url: url,
        success: function(data){
            location.reload();
        }
    });
}

function ajaxMediaSync(url) {
    $.ajax({
        async:false,
        type:"GET",
        dataType: "json",
        url: url,
        success: function(data){
            location.reload();
        }
    });
}
