(function ($) {
    "use strict";

    $('input[data-reveal]').click(function() {
        var $this = $(this),
            $field = $('#' + $this.attr('data-reveal')),
            // fallback label for browsers without placeholder support
            $label = $('#' + $this.attr('data-reveal') +'-label');
        console.log(Modernizr.input.placeholder);
        console.log($label);    
            
        if ($this.prop("checked")) {
            $field.slideDown();
            if (!Modernizr.input.placeholder) {
                $label.show();
            }    
        } else {
            $field.slideUp();
            $label.hide();
        }  
            
    });

}(jQuery));
