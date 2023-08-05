(function ($) {
    "use strict";

    var local_tagging = new local_tagging_class("tagging", false);

    // When the form is submitted update the hidden tags JSON field with JSON
    // for the chosen tags.
    $('#id_customise_account_form').on('submit', function () {
        // Append tags to list
        var hidden_input = $("#id_homepage_tags_json");
        hidden_input.val(local_tagging.get_tags_as_json());

    });

}(jQuery));
