/*
 * An auto-submit form will submit as soon as any of it's inputs lose focus.
 *
 * Usage: <form class='auto-submit'>...</form>
 */
(function ($) {
    "use strict";

    $('.auto-submit input, .auto-submit textarea')
        .blur(function () {
            $(this).closest('form').submit();
        })
        .keydown(function (event) {
            if (event.keyCode === 13) {
                $(this).blur();
            }
        });

}(jQuery));
