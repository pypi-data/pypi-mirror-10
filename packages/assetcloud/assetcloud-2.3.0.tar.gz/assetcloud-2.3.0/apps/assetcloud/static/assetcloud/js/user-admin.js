/*
    For user admin page
    --------------------

    Dependencies: ajax-dialog.js
 */
(function ($) {
    "use strict";

    var $edit_modal = $('#edit-modal');
    $edit_modal.modal({
        show: false
    });

    function update_tagging_state() {
        if ($edit_modal.find('input[name="viewOptions"]:checked').val() === 'tagged') {
            $('#user-tagging').slideDown();
        } else {
            $('#user-tagging').slideUp();
        }
    }

    var $edit_modal_link = $('[href="#edit-modal"]');

    //Get user id
    var get_user_id_from_link = function($link) {
        return $link.attr('data-user-id');
    };

    var get_user_update_url_from_link = function($link) {
        return $link.attr('data-user-update-url');
    };

    var get_load_from_url = function(event)
    {
        var user_id = get_user_id_from_link($(event.target));
        return user_id ? get_user_update_url_from_link($(event.target)) : urls['user_add'];
    };

    var edit_modal_extra_init_fn = function(event) {
        $edit_modal.local_tagging = new local_tagging_class("tagging", true);
        update_tagging_state();
    };

    var edit_modal_extra_ajax_form_options = {
        beforeSubmit: function(arr) {
            // Append tags to list
            var tags = $edit_modal.local_tagging.get_tag_list();
            if ($('input[name="viewOptions"]:checked').val() == "all") {
                tags = [];
            }
            var hidden_input = $("#id_tags");
            hidden_input.val(JSON.stringify(tags));
            for (var i=0; i<arr.length; i++) {
                if (arr[i].name == 'tags') {
                    arr[i].value =  hidden_input.val();
                    break;
                }
            }
        }
    };

    var get_edit_modal_extra_ajax_form_options = function(event) {
        return edit_modal_extra_ajax_form_options;
    }

    var ajax_dialog_click_handler = ajaxDialog(
            $edit_modal, get_load_from_url,
            edit_modal_extra_init_fn, get_edit_modal_extra_ajax_form_options);

    // when clicking an edit button
    $edit_modal_link.click(function (event) {

        // Update the title of the modal dialogue depending on whether we are editing or adding
        var $modal_header = $edit_modal.find('.modal-header h3');
        var user_id = get_user_id_from_link($(this));
        if(user_id) {
            //we are loading the edit form
            $modal_header.text('Edit user');
        } else {
            $modal_header.text('Add user');
        }

        $edit_modal.modal('show');

        ajax_dialog_click_handler(event);
    });


    // When submitting the share form, disable the button
    $edit_modal.on('submit', '#update-user-form', function () {
        $('#id_save_user_button').prop("disabled", true).html('Saving...');
    });


    // toggle behaviour of radio buttons - using .on() for an event delegation
    // approach as these radios do not yet exist in the DOM
    $edit_modal.on('change', 'input[name="role"]', function () {
        if ($(this).val() === 'viewer') {
            $('#view-options').slideDown();
        } else {
            $('#view-options').slideUp();
        }
    });

    $edit_modal.on('change', 'input[name="viewOptions"]', function () {
        update_tagging_state();
    });

}(jQuery));
