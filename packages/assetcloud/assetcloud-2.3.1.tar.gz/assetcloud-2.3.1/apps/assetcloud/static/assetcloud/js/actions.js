var get_selected_asset_ids;
var get_selected_asset_ids_as_parameter;
var num_assets_selected;

(function ($) {
    "use strict";

    //Stop dropdowns with interactive dialogs from auto-closing
    $('.dropdown-menu').on('click', '.no-close', function(e) {
        e.stopPropagation();
    });


    get_selected_asset_ids = function () {
        return $.map(
            $(".select-bar input:checked"),
            function (el) {
                return $(el).attr('data-asset-id');
            }
        );
    };

    get_selected_asset_ids_as_parameter = function () {
        return "asset_ids=" + get_selected_asset_ids().join(',');
    };

    num_assets_selected = function () {
        return get_selected_asset_ids().length;
    };

    // Get reference to buttons that require assets to be selected to be active
    var $bulk_buttons = $(".bulk-actions .btn");


    var update_page = function () {
        // function to update button status and selection count
        var asset_count = num_assets_selected();

        // update any counts on the page
        $('.selected-count').text(asset_count);

        if (asset_count > 0) {
            $bulk_buttons.removeClass('disabled');
            $('#selected-count').find('strong').text(asset_count);
        } else {
            $bulk_buttons.addClass('disabled');
            $('#selected-count').find('strong').text(asset_count);
        }
    };

    var check_something_selected = function ($this_button) {
        if (num_assets_selected() > 0 || $this_button.hasClass('download-all')) {
            return true;
        } else {
            alert('Please select some items.');
            return false;
        }
    };


    // Get reference to any action buttons
    var $action_buttons = $(".action");

    // Construct and process the action on click
    $action_buttons.click(function () {

        var $this_button = $(this);
        //Get urls
        var url = $this_button.attr('data-post-url');
        var redirect = $this_button.attr('data-redirect');
        var waiting_text = $this_button.attr('data-waiting-text');

        if (check_something_selected($this_button)) {

            var original_html = $this_button.html();
            if (typeof waiting_text !== 'undefined') {
                $this_button
                    .addClass('disabled')
                    .html('<i class="icon-loading"></i> ' + waiting_text);
            }

            // Make ajax call
            $.ajax({
                type: 'POST',
                url: url,
                data: get_selected_asset_ids_as_parameter(),
                success: function (data) {
                    if (typeof redirect !== 'undefined' && redirect) {
                        window.location = redirect;
                    } else {
                        update_messages();
                        $('#select-none').click();
                    }

                    if (typeof waiting_text !== 'undefined') {
                        //set button back to how it was after a short delay (else it reverts too early)
                        var pause = setTimeout(function () {
                            $this_button.html(original_html).removeClass('disabled');
                        }, 1000);

                    }
                },
                error: function(data) {
                    update_messages();
                }
            });
        }
        return false;
    });

    var bulk_tag_request;

    // Bulk tag button
    $("#bulk-tag-action").click(function () {
        var $this = $(this);

        function is_opening() {
            // Logic inverted because this is called before the dropdown
            return !$this.parent().hasClass('open');
        }

        if (check_something_selected($this)) {

            if (bulk_tag_request) {
                bulk_tag_request.abort();
            }

            if (is_opening()) {
                // Clear tags
                var $tag_container = $("#bulk-tag").find(".tags");
                $tag_container.html('<p class="center"><span class="loading-small">Loading...</span></p>');
                
                // Load common tags
                var url = $this.attr('data-common-tags-url');
                bulk_tag_request = $.ajax({
                    type: 'POST',
                    url: url,
                    data: get_selected_asset_ids_as_parameter(),
                    success: function (data) {
                        $tag_container.html("");
                        for (var i = 0; i < data.length; i++) {
                            bulk_tagging.add_tag_to_container_no_animation(data[i])
                        }
                    },
                    error: function(data) {
                        update_messages();
                    }
                });
            }
        } else {
            return false;
        }

    });


    var $share_assets_dialog = $('#share-assets-dialog');
    var get_share_assets_dialog_load_url = function(event) {
        var asset_ids = get_selected_asset_ids();
        return urls['share_assets'] + '?asset_ids=' + asset_ids;
    };

    var ajax_dialog_click_handler = ajaxDialog(
        $share_assets_dialog, get_share_assets_dialog_load_url);

    $("#bulk-share-action").click(function (event) {
        var $this = $(this);

        function is_opening() {
            // Logic inverted because this is called before the dropdown
            return !$this.parent().hasClass('open');
        }

        if (check_something_selected($this)) {
            if (is_opening()) {
                ajax_dialog_click_handler(event);
            }
        }
    });

    // Bulk delete button
    $("#bulk-delete-action").click(function () {
        return check_something_selected($(this));
        // this button also toggles a bootstrap modal (controlled by the button elements data attributes).
    });

    var $assets = $('.asset-list li');

    // Selecting an asset
    $assets.find('input[type=checkbox]').click(function (event) {
        // get reference to parent li and highlight it
        var $thisLI = $(this).closest('li');
        $thisLI.toggleClass('on');

        update_page();

    });

    // select all or none links
    $('#select-all').click(function () {
        $assets.find('input:enabled').prop('checked',true);
        $assets.addClass('on');
        update_page();
    });
    $('#select-none').click(function () {
        $assets.find('input').prop('checked',false);
        $assets.removeClass('on');
        update_page();
    });
    // Highlight any already selected assets when the page loads.
    $assets.find('input:checked').each(function () {
        $(this).closest('li').addClass('on');
    });
    update_page();
  
}(jQuery));
