/*
    For asset detail page
    ---------------------

    Dependencies: ajax-dialog.js
 */
(function ($) {
    "use strict";

    var $share_assets_dialog = $('#share-assets-dialog');
    var $open_link = $('[data-target="share-assets-dialog"]');
    var url = $open_link.attr('data-asset-share-url');

    var open_dialog = ajaxDialog($share_assets_dialog, function () {
        return url;
    });
    $open_link.click(open_dialog);

    // When submitting the share form, disable the button
    $share_assets_dialog.on('submit', '#share-asset-form', function () {
        $('#share-submit').prop("disabled", true).html('Sending...');
    });
}(jQuery));
