var update_messages;

(function ($) {
    "use strict";

    update_messages = function () {
        $.ajax({
            type: 'GET',
            url: urls['messages-action'],
            success: function (data) {
                $(".messages").empty().append(data).show();
            }
        });
    };
}(jQuery));
