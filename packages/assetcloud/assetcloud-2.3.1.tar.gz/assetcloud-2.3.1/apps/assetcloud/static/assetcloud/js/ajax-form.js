/*
 * A click-to-edit form with a single input.
 *
 * Usage:
 *     <form class="ajax-form">
 *         <input type="text"/>
 *     </form>
 *
 * TODO: Replace this entirely with 'click-to-edit' and 'autosubmit'
 */
function addParameter(url, param, value) {

    "use strict";

    // From: http://stackoverflow.com/questions/7640270/adding-modify-query-string-get-variables-in-a-url-with-javascript
    // Credit: Ryan Kinal
    // Using a positive lookahead (?=\=) to find the
    // given parameter, preceded by a ? or &, and followed
    // by a = with a value after than (using a non-greedy selector)
    // and then followed by a & or the end of the string
    var val = new RegExp('(\\?|\\&)' + param + '=.*?(?=(&|$))'),
        qstring = /\?.+$/;

    // Check if the parameter exists
    if (val.test(url)) {
        // if it does, replace it, using the captured group
        // to determine & or ? at the beginning
        return url.replace(val, '$1' + param + '=' + value);
    } else if (qstring.test(url)) {
        // otherwise, if there is a query string at all
        // add the param to the end of it
        return url + '&' + param + '=' + value;
    } else {
        // if there's no query string, add one
        return url + '?' + param + '=' + value;
    }
}

(function ($) {
    "use strict";

    /* TODO: Drop this in favor of click-to-edit, placeholder,
       and auto-submit */
    var placeholderText = 'Click to add a title...';

    //When you click on the html element, swap with the input field:
    $('.ajax-form a').bind('click focus', function () {
        var $a = $(this),
            $input = $a.next('input');
        $a.hide();
        $input.show().focus();
        return false;
    });

    // On focus of the input field:
    $('.ajax-form input').focus(function () {
        var $input = $(this);
        $input.select();
        $input.data('title', $input.val());       // Store it's initial value
    });

    // Allow hitting enter to blur the form
    $('.ajax-form input').keydown(function (e) {
        if (e.keyCode === 13) {
            $(this).blur();
            e.preventDefault();
        }
    });

    // On blur:
    $('.ajax-form input').blur(function () {
        var $input = $(this),
            $a = $input.prev('a'),
            origTitle = $input.data('title'),
            newTitle = $input.val();

        if (newTitle !== origTitle) {           // Has the title changed?
            $a.removeClass('placeholder');
            // Create a new history state to allow 'back' browsing.
            var new_url = addParameter(window.location.href, "__nocache", new Date().getTime());
            window.History.replaceState(null, null, new_url);

            $input.parents('form').submit();    // Submit form to save new title
            //TODO - get server to respond with new value.
                // while waiting for response set field to disabled
                //$input.attr('disabled','disabled');
        }
        if (newTitle === '') {                   // Is the title blank?
            $a.addClass('placeholder');
            newTitle = placeholderText;         // Use placeholder text
        }
        $input.hide();
        $a.text(newTitle).show().effect("highlight", 1000);
    });

}(jQuery));
