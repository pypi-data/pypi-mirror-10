/*
 * A form which displays as standard text,
 * which turns into a form when an element is clicked.
 */
(function ($) {
    "use strict";

    $('.click-to-edit [data-linked]').click(function () {
        var linkedId = $(this).attr('data-linked');
        $(this).closest('div.click-to-edit').addClass('edit');
        $('#' + linkedId).focus().select();
    });

    $('.click-to-edit form input').each(function () {
        $(this).data('saved-value', $(this).val());
    });

    $('.click-to-edit .cancel').click(function (event) {
        var $this = $(this),
            $container = $this.closest('div.click-to-edit');

        $container.find('form input').each(function () {
            $this.val($this.data('saved-value'));
        });
        $this.closest('div.click-to-edit').removeClass('edit');
        event.preventDefault();
    });

}(jQuery));
