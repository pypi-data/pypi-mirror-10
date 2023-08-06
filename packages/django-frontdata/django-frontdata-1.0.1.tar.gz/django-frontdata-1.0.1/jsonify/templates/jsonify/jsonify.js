;(function () {
    "use strict";

    var root = this,
        cache = undefined;

    var initCache = function () {
        cache = {};
        var tags = document.getElementsByClassName('json-data');
        for (var i=0; i < tags.length; i++) {
            var tag = tags[i];
            cache[tag.dataset.key] = JSON.parse(tag.innerHTML);
        }
    };

    var getCache = function () {
        if (typeof cache == 'undefined') {
            initCache();
        }
        return cache;
    };

    root.hasJsonData = function (key) {
        key || (key = 'initial');
        return key in getCache();
    };

    root.getJsonData = function (key) {
        key || (key = 'initial');
        return getCache()[key];
    };

}).apply(window);
