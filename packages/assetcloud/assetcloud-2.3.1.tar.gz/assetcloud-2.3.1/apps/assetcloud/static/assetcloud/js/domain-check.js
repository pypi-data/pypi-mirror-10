
(function ($) {
    "use strict";
    var domainCheck = {

        init : function () {

            // Cache some variables
            domainCheck.$input = $('#id_subdomain');
            domainCheck.$wrapper = domainCheck.$input.closest('.control-group');
            domainCheck.$messages = domainCheck.$wrapper.find('[class*="available"]');

            // listen for keyup
            domainCheck.$input.keyup(function () {
                domainCheck.check_value($(this).val());
            });
        },


        check_value : function (value) {

            var data = {'subdomain' : value},
                $yes = domainCheck.$wrapper.find('.available-yes'),
                $no = domainCheck.$wrapper.find('.available-no'),
                $invalid = domainCheck.$wrapper.find('.available-invalid');

            if(data.subdomain) {    
                domainCheck.$wrapper.addClass('working');
                // Perform ajax call to check if domain is valid/available
                $.getJSON(urls['subdomain_available'], data, function (response) {

                var pause = setTimeout(function () {
                    domainCheck.$wrapper.removeClass('working');
                }, 250);
                

                switch (response.status) {

                case "available":
                    domainCheck.success();
                    domainCheck.$messages.hide();
                    $yes.show();
                    break;

                case "unavailable":
                    domainCheck.fail();
                    domainCheck.$messages.hide();
                    $no.show();
                    break;

                case "invalid":
                    domainCheck.fail();
                    domainCheck.$messages.hide();
                    $invalid.show();
                    break;
                    
                }


            });

            } else {
                domainCheck.reset();
                domainCheck.$messages.hide();
            }
        },

        success : function () {
            domainCheck.$wrapper.removeClass('error');
            domainCheck.$wrapper.addClass('success');
        },

        fail : function () {
            domainCheck.$wrapper.addClass('error');
            domainCheck.$wrapper.removeClass('success');
        },

        reset : function () {
            domainCheck.$wrapper.removeClass('error');
            domainCheck.$wrapper.removeClass('success');
        }


    };

    domainCheck.init();


}(jQuery));
