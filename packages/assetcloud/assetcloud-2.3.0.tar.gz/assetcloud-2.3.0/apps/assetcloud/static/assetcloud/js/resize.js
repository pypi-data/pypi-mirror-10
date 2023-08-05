/*
 * For custom download size interface
 *
 */

(function ($) {
    "use strict";

    /*global assetDimensions */

    var resize = {
        init : function () {
            // Cache some jquery objects as properties
            resize.$modal = $('#resize-modal');
            resize.$input_width = resize.$modal.find('input.resize-width');
            resize.$input_height = resize.$modal.find('input.resize-height');

            // Define some other properties
            resize.lock_aspect = true;
            resize.aspect_ratio = assetDimensions.width / assetDimensions.height;


            // Closing the modal
            resize.$modal.find('.cancel, .close').click(function () {
                resize.$modal.modal('hide');
                return false;
            });

            // Behaviour of aspect ratio lock toggle
            resize.$modal.find('#toggle-aspect-lock').click(function () {
                var $this = $(this);
                if (resize.lock_aspect === true) {
                    $this.parent('div').addClass('unlocked');
                    resize.lock_aspect = false;
                } else {
                    $this.parent('div').removeClass('unlocked');
                    resize.lock_aspect = true;
                }
                return false;
            });

            // Behaviour of input fields
            resize.$input_width.add(resize.$input_height).keyup(function () {
                var $thisInput = $(this);
                if ($thisInput.val() !== "") {
                    if (!resize.validate($thisInput)) {
                        return false;
                    }
                }
                if (resize.lock_aspect) {
                    resize.constrain($thisInput);
                }

            });


            resize.$modal.on('show', function () {
                // give the width input the focus
                resize.$input_width.focus();
            });

            resize.$modal.find('#custom-resize').submit(function () {
                var url = resize.$modal.attr('data-resize-url');
                url += resize.$input_width.val() + '/' + resize.$input_height.val() + '/';
                window.location = url;
                return false;
            });

            // init button tooltip
            resize.$modal.find('.aspect-lock a.btn').tooltip({placement: 'right', delay: 500});

        },

        validate : function ($thisInput) {
            if ($.isNumeric($thisInput.val())) {
                $thisInput.closest('.control-group').removeClass('error')
                    .end()
                    .parent().next().slideUp();
                return true;
            } else {
                // not numeric - show an error
                $thisInput.closest('.control-group').addClass('error')
                    .end()
                    .parent().next().slideDown();
                return false;
            }
        },

        constrain : function ($thisInput) {
            if ($thisInput.hasClass('resize-width')) {
                // We are dealing with the width field
                resize.$input_height
                    .val(Math.round($thisInput.val() / resize.aspect_ratio));

            } else {
                resize.$input_width
                    .val(Math.round($thisInput.val() * resize.aspect_ratio));

            }

        }
    };



    $(function () {
        if (typeof assetDimensions !== "undefined") {
            resize.init();
        }

    });

}(jQuery));
