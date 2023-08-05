/*
 * Support for date input fields.
 *
 * Usage: <input type='text' class='date-field'/>
 *
 * At a future date we might simply use <input type='date'>,
 * with jQuery as a fallback,
 * but support for that at the moment has a few issues...
 *
 * http://code.google.com/p/chromium/issues/detail?id=79064
 * http://stackoverflow.com/questions/2968817/ ...
 *                          is-there-a-way-to-localize-input-type-date-in-html5
 */
(function ($) {
    "use strict";

    // Make sure DOM is ready
    // (firefox sometimes complains .datepicker is not a function)
    $(function () {
        var dateFormat = 'dd/mm/yy';
        if (LOCALE == "en" || LOCALE == "en-US") {
            dateFormat = 'mm/dd/yy';
        }
        $('input.date-field').datepicker({
            dateFormat: dateFormat,
            showOn: "both",
            buttonImage: STATIC_URL("assetcloud/img/icons/calendar.png"),
            buttonImageOnly: true
        });
    });

}(jQuery));
