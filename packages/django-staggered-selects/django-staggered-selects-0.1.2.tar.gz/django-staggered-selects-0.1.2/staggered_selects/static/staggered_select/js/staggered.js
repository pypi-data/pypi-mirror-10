django.jQuery(document).ready(function() {
    var defaultSelectOption = '<option value="" selected="selected">---------</option>';

    django.jQuery(".staggered-select").each(function(i, selectDiv) {
        var selectObj = django.jQuery(selectDiv),
            watched = "id_" + selectObj.next().attr("watched_field"),
            choiceLoader = selectObj.next().attr("get_choices_function"),
            watchedVerboseText = django.jQuery(
                                            "label[for='" + watched + "']"
                                        ).text();

        selectObj.prev(".sselect-message").find(".watched-verbose").text(
            '"' + watchedVerboseText + '"'
        );

        var getCurrentWatchedValue = function(watchedSelector) {
            var watchedDOMObject = django.jQuery("#" + watchedSelector),
                watchedValueObj = {
                    name: '',
                    slug: ''
                };

            if (watchedDOMObject.is('select')) {
                watchedValueObj.name = watchedDOMObject.find("option:selected").text();
                watchedValueObj.slug = watchedDOMObject.find("option:selected").val();
            } else {
                watchedValueObj.name = watchedDOMObject.val();
                watchedValueObj.slug = watchedDOMObject.val();
            }

            return watchedValueObj;
        };

        var updateContents = function(watchedValue) {
            // Select the null value and fade the select-box out as a placeholder fades in
            var currentDjangoValue = selectObj.next().val();

            selectObj.val("").change().fadeOut();

            selectObj.empty().append(defaultSelectOption);

            // Load the new choices after a brief delay.
            setTimeout(function() {
                if (watchedValue.slug !== "") {
                    window[choiceLoader](
                        selectObj,
                        watchedValue,
                        function(results, postRenderCallback) {
                            var valueMatchesCurrent = false;

                            for (var i = 0; i < results.length; i++) {
                                var result = results[i];

                                selectObj.append(
                                    '<option value="' + result.slug + '">' +
                                        result.name + '</option>'
                                );

                                if (result.slug == currentDjangoValue) {
                                    valueMatchesCurrent = true;
                                }
                            }

                            postRenderCallback();

                            selectObj.prev().fadeOut();
                            selectObj.fadeIn();

                            if (valueMatchesCurrent) {
                                selectObj.val(currentDjangoValue);
                            }
                        }
                    );
                } else {
                    selectObj.prev().fadeIn();
                }
            }, 50);
        };

        updateContents(getCurrentWatchedValue(watched));

        django.jQuery("#" + watched).change(function(argument) {
            updateContents(getCurrentWatchedValue(watched));
        });

        selectObj.change(function(argument) {
            selectObj.next().val(selectObj.val()).change();
        });
    });
});
