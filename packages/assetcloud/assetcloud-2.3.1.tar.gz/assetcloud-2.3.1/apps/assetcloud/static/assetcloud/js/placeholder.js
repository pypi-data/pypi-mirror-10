/*
 * Fallback support for browsers that don't yet support 'placeholder'
 *
 * Usage:
 *   <input type="text" placeholder="Enter some text">
 */
(function ($) {
    "use strict";

    if (Modernizr.input.placeholder) {
        return;
    }

    // Clear the placeholder text on an element, if it currently has one.
    function clearPlaceholder(elem) {
        if ($(elem).hasClass('placeholder')) {
            $(elem).removeClass('placeholder').val('');
        }
    }

    // Set the placeholder text on an element, if it is currently empty.
    function setPlaceholder(elem) {
        if ($(elem).val() === '') {
            $(elem).addClass('placeholder').val($(elem).attr('placeholder'));
        }
    }

    // Clear all the placeholders in a given element.
    function clearAllPlaceholders(elem) {
        $(elem).find('[placeholder]').each(function () {
            clearPlaceholder(this);
        });
    }

    // Set all the placeholders in a given element.
    function setAllPlaceholders(elem) {
        $(elem).find('[placeholder]').each(function () {
            setPlaceholder(this);
        });
    }

    // Bind focus and blur events to set placeholders appropriately.
    $('[placeholder]')
        .focus(function () {
            clearPlaceholder(this);
        })
        .blur(function () {
            setPlaceholder(this);
        });

    // During form submission temporarily blank any placeholders.
    // (Problemtic in that this can cause form submission,
    //  which some other bit of jquery might want to prevent.)
    $('form').submit(function () {
        clearAllPlaceholders(this);
        this.submit();
        setAllPlaceholders(this);
        return false;
    });

    // Initialise all placeholders.
    setAllPlaceholders('body');

}(jQuery));
