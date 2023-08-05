/**
    Make $dialog an AJAX dialog - when the form in it is submitted the
    response will be loaded into $dialog instead of the whole page.

    Returns a click handler function that you should attach to the button
    that you want to open the dialog. This returned function loads the HTML
    into the $dialog from the server and sets up the form so that when it is
    submitted the result is loaded into $dialog instead of the whole page,
    unless the server returns the string 'OK' as the response in which case
    the page is reloaded.

    @param $dialog the dialog element. Should contain 'loading' HTML before you call this function.
    @param get_load_from_url function to return URL to load initial form HTML from. Takes the click event as an argument.
    @param extra_init_fn (optional) extra function to call every time the form is initialised.
    @param get_extra_options (optional) function that returns extra properties to pass to ajaxForm().
*/
function ajaxDialog($dialog, get_load_from_url, extra_init_fn, get_extra_options) {
    "use strict";

    //store initial modal html
    var blank_dialog_html = $dialog.html();

    function handleXhrError(xhr) {
        document.open();
        document.write(xhr.responseText);
        document.close();
    }

    // when clicking the 'open dialog' button
    var load_dialog = function (event) {
        $dialog.load(get_load_from_url(event), '', function on_complete() {
            function init_ajax_form($dialog) {
                if (extra_init_fn) {
                    extra_init_fn(event);
                }

                var options = {
                    type: 'POST',
                    success: function (response) {
                        if (response == 'OK') {
                            document.location.reload(true);
                        } else {
                            $dialog.html(response);
                            init_ajax_form($dialog);
                        }
                    },
                    error: handleXhrError
                };

                if (get_extra_options) {
                    var extra_options = get_extra_options(event);
                    for (var attr_name in extra_options) {
                        if (extra_options. hasOwnProperty(attr_name)) {
                            options[attr_name] = extra_options[attr_name];
                        }
                    }
                }

                $dialog.find('form').ajaxForm(options);
            }
            init_ajax_form($dialog);
        });
    };

    $dialog.on('hidden', function () {
        //Reset edit modal back to its initial 'loading' state
        $dialog.html(blank_dialog_html);
    });

    return load_dialog;
}
