// https://gist.github.com/alanhamlett/6316427
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
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
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    }
});

// Credit goes to Dave McDermid
// https://boagworld.com/dev/creating-a-draggable-sitemap-with-jquery/
var historyStack = {
    stack: new Array(),
    temp: null,
    saveState: function(item) {
        historyStack.temp = { item: $(item), itemParent: $(item).parent(), itemAfter: $(item).prev() };
    },
    commit: function() {
        if (historyStack.temp != null) historyStack.stack.push(historyStack.temp);
    },
    restoreState: function() {
        var h = historyStack.stack.pop();
        if (h == null) return;
        if (h.itemAfter.length > 0) {
            h.itemAfter.after(h.item);
        }
        else {
            h.itemParent.prepend(h.item);
        }
        //checks the classes on the lists
        $('#sitemap li.sm2_liOpen').not(':has(li)').removeClass('sm2_liOpen');
        $('#sitemap li:has(ul li):not(.sm2_liClosed)').addClass('sm2_liOpen');
    }
};

$(function() {
    $('#sitemap li').prepend('<div class="dropzone"></div>');

    $('#sitemap dl, #sitemap .dropzone').droppable({
        accept: '#sitemap li',
        tolerance: 'pointer',
        drop: function(e, ui) {
            var method;
            var li = $(this).parent();
            var child = !$(this).hasClass('dropzone');
            if (child && li.children('ul').length == 0) {
                li.append('<ul/>');
            }
            if (child) {
                method = 'insert';
                li.addClass('sm2_liOpen').removeClass('sm2_liClosed').children('ul').append(ui.draggable);
            }
            else {
                method = 'move';
                li.before(ui.draggable);
            }
            $('#sitemap li.sm2_liOpen').not(':has(li:not(.ui-draggable-dragging))').removeClass('sm2_liOpen');
            li.find('dl,.dropzone').css({ backgroundColor: '', borderColor: '' });

            var to;
            var dragged = $(ui.draggable[0]);

            if(method === 'insert'){
                to = dragged.parent().parent();
            }
            if(method === 'move'){
                to = li;
            }

            historyStack.commit();

            $.ajax({
                url: 'reorder/',
                type: 'POST',
                data: {
                    method: method,
                    source: dragged.attr('id'),
                    target: to.attr('id')
                }
            }).success(function (data) {
                $.each(data, function (i, o) {
                    $('#' + o.menu_id + ' a.edit-plugin').first().attr('href', o.path);
                });
            }).error(function(retval){
                historyStack.restoreState();
                $('.top-right').notify({
                    type: 'danger',
                    message: {text: retval.responseText},
                    fadeOut: {enabled: true, delay: 5000}
                }).show();


            });
        },
        over: function() {
            $(this).filter('dl').css({ backgroundColor: '#ccc' });
            $(this).filter('.dropzone').css({ borderColor: '#aaa' });
        },
        out: function() {
            $(this).filter('dl').css({ backgroundColor: '' });
            $(this).filter('.dropzone').css({ borderColor: '' });
        }
    });
    
    $('#sitemap li').draggable({
        handle: ' > dl',
        opacity: .8,
        addClasses: false,
        helper: 'clone',
        zIndex: 100,
        start: function(e, ui) {
            historyStack.saveState(this);
        }
    });

    $('.sm2_expander').on('click', function() {
        $(this).parent().parent().toggleClass('sm2_liOpen').toggleClass('sm2_liClosed');
        return false;
    });

    $('.edit-label').on('click', function(){
        var id = $(this).parent().parent().attr('id');
        var label = $('#' + id + '-label');

        label.attr('contentEditable', true).focus();
        label.addClass('editable');
        label.unbind('keydown');
        label.on('keydown', function(e){
           if(e.keyCode === 13){
               label.attr('contentEditable', false);
               label.removeClass('editable');

               $.ajax({
                   url: id + '/rename/',
                   type: 'POST',
                   data: {
                       title: label.html()
                   }
               }).done(function (data) {
                   $.each(data, function(i, o){
                       $('#' + o.menu_id + ' a.edit-plugin').first().attr('href', o.path);
                   });
               })
           }
        });
    });

    $('#sitemap .menu-label').on('mousedown', function(e){
        e.stopPropagation();
    });
});

