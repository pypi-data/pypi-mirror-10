/*
    For tracking javascript click events (e.g. launching a modal) in google analytics

    To use just add a data-attribute to your action link, passing in params as a json object:
    data-track='{"category": "Upgrade", "action": "Launch", "label": "Account page button"}'
    
    Note: JSON must be well-formed, which means it must have double quotes around the property labels.
    This means you need to use single quotes on the data-track attribute itself.

 
 */

(function ($) {
    "use strict";

    $('[data-track]').click(function() {
        var params = $(this).data('track');
        // Record event in google analytics - https://developers.google.com/analytics/devguides/collection/gajs/eventTrackerGuide
        _gaq.push(['_trackEvent', params.category, params.action, params.label]);
    });

}(jQuery));
