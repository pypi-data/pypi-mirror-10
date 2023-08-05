var local_tagging_class;
var ajax_tagging_class;
var bulk_tagging = null;


// Memoizes a no-arg function
function memoize_getter(fn) {
    var local;
    return function() {
        if (!local) {
            local = fn.call(this);
        }
        return local;
    };
}

(function ($) {
    "use strict";

    $('#bulk-tag').on('click', function (e) {
        e.stopPropagation();
    });


    // Initialise tag filtering
    function init_tag_filter() {
        if ($('.tag-filter').length) {
            var $tag_filter = $('.tag-filter'),
                $specify_tags_link = $tag_filter.find('.specify-tags-link'),
                $specify_tags_cancel = $tag_filter.find('a.cancel'),
                $specify_tags_fields = $tag_filter.find('.specify-tags-fields'),
                $browse_tags_link = $('.browse-tags-link'),
                $tags_field = $('#tags'),
                $browse_tags_dialog = $('#browse-tags-dialog');

            $specify_tags_link.click(function () {
                $specify_tags_fields.slideDown('fast');
                $specify_tags_fields.find('input').focus();
                return false;
            });

            $specify_tags_cancel.click(function () {
                $specify_tags_fields.slideUp('fast');
                return false;
            });


            $browse_tags_link.click(function() {

                $.ajax({
                    url: urls['tag-list'],
                    cache: false, 
                    success: function(tags,textStatus,jqXHR) {


                        var $taglist = $('<ul class="tags"></ul>');

                        // Construct a tag from each json object
                        $.each(tags,function(index, value) {
                              $taglist
                                .append(
                                    $('<li/>')
                                    .html('<a href="#" class="tag">'+value+'</a>')
                                    .click(function() {
                                        // append the clicked value to the tags hidden field and submit the form
                                        $tags_field.val($tags_field.val()+','+value);
                                        $tag_filter.closest('form').submit();
                                        return false;
                                    })

                                );
                        });

                        // append the list of tags into the dropdown
                        $browse_tags_dialog.html($taglist);
                    }
                });
                
            });
        }
    }

    function Tagging(container_id) {
        // Closure for reference from inner functions
        var me = this;

        this.init = function () {
            if (this.get_container().length) {
                init_tag_filter();

                this.init_tag_autosave();

                this.autocomplete_ajax_request = null;

                this.init_autocomplete();

                this.init_click_handlers();
            }
        };

        this.init_tag_autosave = function () {
            
            // when save button is clicked also apply any
            // tags sitting in the add tag field
            // i.e. forgive the user for not pressing "Add Tag" and
            // assume they do want to save the tags entered
            $(".autosave-tags").on("click", function(){
                if (me.get_tag_input().val() !== "") {
                    me.get_submit_button().click();
                }
                return true;
            });

        },

        this.init_autocomplete = function () {
            // See:
            //   http://jqueryui.com/demos/autocomplete/#multiple
            //   http://charlesleifer.com/blog/ ...
            //                    suggesting-tags-django-taggit-and-jquery-ui/
            function split(val) {
                return val.split(/ \s*/g);
            }
            function extractLast(term) {
                return split(term).pop();
            }
            var autocomplete_url = me.get_tag_input().attr('data-autocomplete-url');

            // don't navigate away from the field on tab when selecting an item
            this.get_tag_input().bind('keydown', function (event) {
                if (event.keyCode === $.ui.keyCode.TAB && $(this).data('autocomplete').menu.active) {
                    event.preventDefault();
                }
            }).autocomplete({
                minLength: 1,
                source: function (request, response) {
                    var term = request.term;
                    var last_token = extractLast(term);
                    if (last_token.length === 0 || me.is_adding_tag()) {
                        response([]);
                    } else {
                        me.auto_complete_ajax_request = $.ajax({
                            url: autocomplete_url,
                            dataType: 'json',
                            data: {'term': last_token},
                            complete: function () {
                                me.auto_complete_ajax_request = null;
                            },
                            success: function (data) {
                                response(data);
                            }
                        });
                    }
                },
                focus: function () {
                    // prevent value inserted on focus
                    return false;
                },
                select: function (event, ui) {
                    // Otherwise add the tag to the input field
                    var terms = split(this.value);
                    // Remove the current input
                    terms.pop();
                    // Add the selected item
                    terms.push(ui.item.value);
                    // Add placeholder to get the space at the end
                    terms.push("");
                    this.value = terms.join(" ");
                    // Submit the form only if the enter key was pressed
                    if (event.which === $.ui.keyCode.ENTER) {
                        me.get_submit_button().click();
                    }
                    return false;
                }
            });
        };

        this.init_click_handlers = function () {
            // Handle click event on 'a' elements -
            // use delegate to handle dynamic content
            this.get_container().delegate('a', 'click', function () {
                if ($(this).hasClass('close')) {
                    var tag = $(this).parent().find('a.tag').html();
                    me.delete_tag(tag);

                    var $li = $(this).parent('li');
                    $li.fadeTo(250, 0.5);
                    return false;
                } else if ($(this).hasClass('show')) {
                    // Show form and give text field the focus
                    me.get_form().show();
                    me.get_tag_input().focus();

                    me.get_container().find('a.show').hide();
                    return false;
                } else if ($(this).hasClass('cancel')) {
                    // Hide form and clear the text field
                    me.get_form().hide();
                    me.get_tag_input().val('');

                    me.get_container().find('a.show').show();
                    return false;
                }
            });
        };

        this.is_adding_tag = function () {
            return false; // Only potentially true for ajax adding
        };

        this.split_tags = function (tag_string) {
            var tags = tag_string.split(',');
            return $.grep($.map(tags, $.trim),
                          function (tag) { return tag.length > 0; });
        };

        this.get_tag_values = function () {
            return me.split_tags(this.get_tag_input().val());
        };

        this.add_tags = function(tags) {
            for (var i=0; i<tags.length; i++) {
                this.add_tag(tags[i]);
            }
        };

        this.get_tag_input = memoize_getter(function () {
            return this.get_container().find('.add_more_tags');
        });

        this.get_container = memoize_getter(function () {
            return $('#'+container_id);
        });

        this.get_submit_button = memoize_getter(function () {
            return this.get_container().find('button');
        });

        this.get_form = memoize_getter(function () {
            return this.get_container().find('form');
        });

        this.add_tag_to_container_no_animation = function (tag_html, fetch_from_server, force_user_tag) {
            return this.add_tag_to_container(tag_html, fetch_from_server, force_user_tag, true);
        };

        this.add_tag_to_container = function (tag_html, fetch_from_server, force_user_tag, no_animation) {
            function add(html) {
                var $li = $(html);
                me.get_container().find('ul').append($li);
                if (!no_animation) {
                    $li.effect("highlight",  2000);
                }
                me.get_container().find('p.no-tags').hide();
                // Clear and give focus to input ready for next tag
                me.get_tag_input().val('').focus();
            }

            if (fetch_from_server) {
                var url = me.get_container().attr('data-tag-html-url');
                $.ajax({
                    type: 'GET',
                    url: url,
                    data: {'tag_name': tag_html,
                           'force_user_tag': force_user_tag ? 1 : 0},
                    success: function (data) {
                        add(data);
                    }
                });
            }
            else {
                add(tag_html);
            }
        };

        this.get_tag_li = function (tag) {
            var lis = this.get_container().find('li').find('a.tag');
            for (var i=0; i<lis.length; i++) {
                if ($(lis[i]).html() == tag) {
                    return $(lis[i]).parent();
                }
            }
        };

        this.remove_tag_from_container = function (tag) {
            var $li = this.get_tag_li(tag);
            $li.fadeOut(250, function () {
                $(this).remove();
                if (me.get_container().find('li').length === 0) {
                    me.get_container().find('p.no-tags').show();
                }
            });
        };

        this.fade_tag_in = function (tag) {
            var $li = this.get_tag_li(tag);
            $li.fadeTo(250, 1);
        };
    }

    function local_tagging(container_id, force_user_tag) {
        if (!$("#" + container_id).length) {
            return;
        }
        var tagging_obj = new Tagging(container_id);

        tagging_obj.init();

        function infer_tag_list() {
            var lis = tagging_obj.get_container().find('li').find('a.tag');
            var tags = [];
            for (var i=0; i<lis.length; i++) {
                tags.push($(lis[i]).html());
            }
            return tags;
        }

        var tag_list = infer_tag_list();

        function add_new_tag(tag) {
            tag_list.push(tag);
        }
        function is_new_tag(tag) {
            return $.inArray(tag, tag_list) == -1;
        }
        function remove_existing_tag(tag) {
            tag_list.splice($.inArray(tag, tag_list), 1);
        }

        tagging_obj.get_tags_as_json = function() {
            return JSON.stringify(this.get_tag_list());
        }

        tagging_obj.get_submit_button().click(function (e) {
            tagging_obj.add_tags(tagging_obj.get_tag_values());
            e.preventDefault();
        });

        tagging_obj.add_tag = function(tag) {
            if (is_new_tag(tag)) {
                add_new_tag(tag);
                // Hardcode force user tag because local tagging is only used
                // for update user form
                tagging_obj.add_tag_to_container(tag, true,
                                                 force_user_tag == true);
            }
        }

        tagging_obj.delete_tag = function(tag) {
            if (!is_new_tag(tag)) {
                remove_existing_tag(tag);
                tagging_obj.remove_tag_from_container(tag);
            }
        }

        tagging_obj.get_tag_list = function() {
            return tag_list;
        }

        return tagging_obj;
    }

    local_tagging_class = local_tagging;

    function ajax_tagging(container_id) {
        if (!$("#" + container_id).length) {
            return;
        }

        var tagging_obj = new Tagging(container_id);
        tagging_obj.init();

        // Track in-flight AJAX requests.
        var add_tag_ajax_request = null;

        tagging_obj.get_form().submit(function (e) {
            if (tagging_obj.autocomplete_ajax_request !== null) {
                tagging_obj.autocomplete_ajax_request.abort();
            }
            tagging_obj.get_tag_values()
            var input_value = tagging_obj.get_tag_values();
            // don't call add_tags if user hasn't specified any
            if(input_value != "") {
                tagging_obj.add_tags(tagging_obj.get_tag_values());
            }
            e.preventDefault();
        });

        tagging_obj.is_adding_tag = function() {
            return add_tag_ajax_request !== null;
        };

        tagging_obj.add_tags = function(tags) {

            // this removes the autocomplete dropdown
            tagging_obj.get_tag_input().blur();

            // Cache container div
            var $tagging_container = tagging_obj.get_container();

            // trigger 'working' state
            $tagging_container.addClass('working');

            var url = $tagging_container.attr('data-add-tags-url');
            var asset_id = $tagging_container.attr('data-asset-id');
            if (!asset_id) {
                asset_id = get_selected_asset_ids().join(',');
            }

            var quoted_tags = $.map(tags,
                                    function (tag) {
                                        return '"' + tag + '"';
                                    }).join(',');

            add_tag_ajax_request = $.ajax({
                type: 'POST',
                url: url,
                dataType: 'json',
                data: {'tags': quoted_tags, asset_ids: asset_id},
                complete: function () {
                    add_tag_ajax_request = null;
                },
                success: function (data) {
                    for (var i = 0; i < data.length; i++) {
                        tagging_obj.add_tag_to_container($.trim(data[i]));
                    }
                    $tagging_container.removeClass('working');
                }
            });
        };

        tagging_obj.delete_tag = function(tag) {
            var url = tagging_obj.get_container().attr('data-delete-tags-url');
            var asset_id = tagging_obj.get_container().attr('data-asset-id');
            if (!asset_id) {
                asset_id = get_selected_asset_ids().join(',');
            }

            $.ajax({
                type: 'POST',
                url: url,
                dataType: 'json',
                data: {'tags': '"' + tag + '"', 'asset_ids': asset_id},
                success: function (data) {
                    tagging_obj.remove_tag_from_container(tag);
                },
                error: function (data) {
                    tagging_obj.fade_tag_in(tag);
                }
            });
        };

        return tagging_obj;
    }
    ajax_tagging_class = ajax_tagging;
    new ajax_tagging("tagging");
    bulk_tagging = new ajax_tagging("bulk_tagging");
}(jQuery));

