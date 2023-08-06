window.$ = django.jQuery;

$(document).ready(function(){

    // Intercept anchor clicks
    $(document).on('click', '.grp-dashboard-module a[data-intention="ajax"]', function(e){
        var url = $(this).attr('href');
        var target = $(this).closest('.grp-dashboard-module');
        $.get(url, function(data){
            target.html(data);
        });
        return false;
    });

    // Intercept form submits for right panel
    $(document).on('submit', '#right-content .grp-dashboard-module form', function(e){
        var form = $(this);
        var url = form.attr('action');
        var target = form.closest('.grp-dashboard-module');
        var data = form.serialize();
        $.ajax({
            url: url,
            data: data,
            type: form.attr('method'),
            cache: false,
            success: function(data){
                target.html(data);
            }
        });
        return false;
    });

    // Animate left column
    $(document).on('click', '#left-content-toggle', function(e){
        var el = $(this);
        var left_content = $('#left-content');
        var center = $('#grp-content-container');
        el.toggleClass('collapsed');

        if (el.hasClass('collapsed')){
            left_content.animate({
                'margin-left': '-25%'
            });
            center.delay(50).animate({
                'margin-left': '0'
            });
            django.jQuery.cookie('left_content_collapsed', 1, {expires: 365, path: '/'});
        }
        else{
            center.animate({
                'margin-left': '25%',
            });
            left_content.delay(50).animate({
                'margin-left': 0
            });
             django.jQuery.cookie('left_content_collapsed', '', {expires: 365, path: '/'});
        }

        return false;
    });

    // Animate right column
    $(document).on('click', '#right-content-toggle', function(e){
        var el = $(this);
        var right_content = $('#right-content');
        var center = $('#grp-content-container');
        el.toggleClass('collapsed');

        if (el.hasClass('collapsed')){
            right_content.animate({
                'margin-right': '-27%'
            });
            center.delay(50).animate({
                'margin-right': '0'
            });
            django.jQuery.cookie('right_content_collapsed', 1, {expires: 365, path: '/'});
        }
        else{
            center.animate({
                'margin-right': '25%',
            });
            right_content.delay(50).animate({
                'margin-right': 0
            });
            django.jQuery.cookie('right_content_collapsed', '', {expires: 365, path: '/'});
        }

        return false;
    });

});
