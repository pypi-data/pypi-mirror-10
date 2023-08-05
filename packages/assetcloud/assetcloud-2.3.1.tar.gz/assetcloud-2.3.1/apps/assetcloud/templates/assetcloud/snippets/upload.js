// This is somewhat mungy, but it`ll do the job until we have some concrete UI behind it.

(function ($) {
    "use strict";

    var uploader = new plupload.Uploader({
        runtimes : 'html5,flash',
        browse_button : 'pickfiles',
        browse_button_hover: "browse-button-hover",
        drop_element: "drop-area",
        url : '{% url "asset-upload-action" %}',
        flash_swf_url : '{{ STATIC_URL }}js/lib/plupload-1.5.1.1/plupload.flash.swf',
        headers : {'X-Requested-With' : 'XMLHttpRequest', 'X-CSRFToken' : '{{csrf_token}}'},
        multipart: true,
        urlstream_upload: true      // flash runtime didn't work without this option
    });

    var initialPageState = true;

    // Get a collection of links that would interrupt an upload when clicked.
    var $interruptLinks = $('#header .nav-primary a').add('#header .dropdown-menu a').add('#view_last_upload').add('#footer a');

    uploader.bind('FilesAdded', function (up, files) {
        //Create list items for each uploaded file
        var $log = $('#file-list'),
            i;

        for (i = 0; i < files.length; i += 1) {
            var $preview = $('<li id="' + files[i].id + '"><div></div>' +
                        files[i].name + ' <em>' + plupload.formatSize(files[i].size) + '</em><span></span></li>');
            $log.append($preview);
        }

        // Start upload automatically
        setTimeout(function () { up.start(); }, 100);
    });

    uploader.bind('UploadFile', function (up, file) {
        $('#submit-form').append('<input type="hidden" name="file-' + file.id + '" value="' + file.name + '" />');
    });

    uploader.bind('UploadProgress', function (up, file) {
        //console.log('progress Event fired');
        $('#' + file.id).find('div').css('width', file.percent + '%');
        $('#' + file.id).find('span').text(file.percent + '%');
    });

    uploader.bind('FileUploaded', function (up, file, info) {
        // Called when a file has finished uploading
        var response_obj = $.parseJSON(info.response);
        var error = response_obj.error;
        if (typeof (error) != 'undefined') {
            up.trigger('Error', {
                message: error.message,
                code: error.code,
                details: error.details,
                file: file
            });
            return false;
        }
    });

    uploader.bind('Error', function (up, err) {
        $('#content').prepend('<div class="alert alert-error">' +
            (err.file ? err.file.name + ': ' : '') +
            err.message +
            '</div>' +
            '<!-- Code: ' + err.code + ' -->');

        up.refresh(); // Reposition Flash/Silverlight
    });




    var summary_statuses = {
        ALL_OK: 0,
        SOME_OK: 1,
        ALL_FAILED: 2
    };

    var get_summary_status = function (up) {
        var ok_count = 0;
        var failed_count = 0;
        var i;
        for (i = 0; i < up.files.length; i++) {
            var file = up.files[i];
            if (file.status == plupload.DONE) {
                ok_count++;
            } else {
                failed_count++;
            }
        }

        if (failed_count == 0) {
            return summary_statuses.ALL_OK;
        } else if (ok_count > 0) {
            return summary_statuses.SOME_OK;
        } else {
            return summary_statuses.ALL_FAILED;
        }
    };

    uploader.bind('StateChanged', function (up) {
        if (up.state === plupload.STOPPED) {

            // Remove check to links on the page that will interrupt this upload
            $interruptLinks.removeClass('js-warn-interrupt');

            // Change button text once some files have been uploaded.
            $('#pickfiles').text('Upload more files...');

            var summary_status = get_summary_status(up);
            if (summary_status == summary_statuses.ALL_OK) {
                $('#all_uploads_successful').fadeIn();
                $('#some_uploads_failed').fadeOut();
            } else {
                $('#all_uploads_successful').fadeOut();
                $('#some_uploads_failed').fadeIn();
            }

            if (summary_status != summary_statuses.ALL_FAILED) {
                $('#view_uploaded_files').fadeIn();
            }

            $('#cancel').hide();
            $('#inProgress').fadeOut();

        } else if (up.state == plupload.STARTED) {

            // Add check to links on the page that will interrupt this upload
            $interruptLinks.addClass('js-warn-interrupt');


            $('#inProgress').show();
            $('#cancel').show();
            $('#all_uploads_successful').fadeOut();
            $('#some_uploads_failed').fadeOut();
            $('#view_uploaded_files').fadeOut();

            if (initialPageState) {
                $('.alert-wrap').fadeIn();
            }

            initialPageState = false;
        }
    });
    
    // Listen for clicks on interrupt links
    $('body').on('click', '.js-warn-interrupt', function() {
        return confirm('This will cancel the current upload. Are you sure?');
    });

    uploader.init();

    // UI for drag and drop behaviour
    if (!!window.FileReader && Modernizr.draganddrop) {
        // On with the sexy drag and drop action.
        // A timeout is used to prevent flickering of the drop hint due all the extra
        // dragover/dragleave events that are fired when you hover over any child elements
        // see:
        // http://stackoverflow.com/questions/8459838/changing-mouse-cursor-for-html5-drag-drop-files-gmail-drag-drop
        var resetTimer;

        var reset = function () {
            $('#drop-hint').hide();
        };

        var handle_dragging = function (e) {

            //var srcElement = e.srcElement ? e.srcElement : e.target;

            // Check it is a file being dragged not just some selected text
            if ($.inArray('Files', e.dataTransfer.types) > -1) {
                // Mouse cursor effect
                //e.dataTransfer.dropEffect = (srcElement.id == 'drop-hint') ? 'copy' : 'none';
                // -BB: the above prevented drop working outside drop-hint
                e.dataTransfer.dropEffect = 'copy';

                if (e.type === "dragover") {
                    // Cancel the hiding of the drop-hint
                    if (resetTimer) {
                        clearTimeout(resetTimer);
                    }
                    //show the drop-hint
                    $('#drop-hint').fadeIn(200);
                } else if (e.type === "dragleave") {
                    // hide the drop hint after a small delay
                    resetTimer = window.setTimeout(reset, 40);
                } else if (e.type === "drop") {
                    reset();
                }
            }
        };

        document.body.addEventListener("dragleave", handle_dragging, false);
        document.body.addEventListener("dragover", handle_dragging, false);
        document.body.addEventListener("drop", handle_dragging, false);
    }

}(jQuery));
