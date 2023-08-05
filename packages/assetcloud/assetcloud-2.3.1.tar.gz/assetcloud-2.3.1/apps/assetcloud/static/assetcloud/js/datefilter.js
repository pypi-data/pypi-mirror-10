/*
    Date filtering on the search page.
*/

(function ($) {
    "use strict";

    var $date_filter = $('.date-filter'),
        $custom_range_link = $date_filter.find('.custom-range-link'),
        $custom_range_cancel = $date_filter.find('.cancel'),
        $custom_range_fields = $date_filter.find('.custom-range-fields');

    $custom_range_link.click(function () {
        $custom_range_link.hide();
        $custom_range_fields.show();
        return false;
    });

    $custom_range_cancel.click(function () {
        $custom_range_fields.fadeOut('fast', function () {
            $custom_range_link.show();
        });
        return false;
    });

}(jQuery));
