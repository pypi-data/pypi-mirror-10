/*
    Looks for any confirmation modals and assigns actions to their buttons.
    Expects two buttons (button.confirm, button.cancel) and an attribute in
    the div ('data-linked') that specifies the id of the form it is linked
    to.
*/
(function ($) {
    "use strict";

    var $confirmation = $('div.confirmation'),
        current_form_id = "";

    $confirmation.each(function () {
        var $this = $(this),
            $confirm = $this.find('button.confirm'),
            $cancel = $this.find('button.cancel');

        $confirm.click(function () {
            // ignore second and subsequent clicks to avoid trying to delete the
            // same thing twice, which often results in the user seeing a 404
            $confirm.attr('disabled', true);

            var $form = $('#' + current_form_id);
            $form.submit();
        });
        $cancel.click(function () {
            $this.modal('hide');
        });
    });

    // Store id of form that the launched modal relates to (BB - I'm open to 
    // suggestions on a better way of doing this)
    $('[data-target]').click(function () {
        var $parent_form = $(this).parents('form');
        if ($parent_form.length > 0) {
            current_form_id = $parent_form[0].id;
        }
    });

}(jQuery));
