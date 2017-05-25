'use strict';

var RefluxDispatcher = function () {
    function RefluxDispatcher() {
        babelHelpers.classCallCheck(this, RefluxDispatcher);

        this._stores = [];
    }

    RefluxDispatcher.prototype.addStore = function addStore() {
        for (var _len = arguments.length, stores = Array(_len), _key = 0; _key < _len; _key++) {
            stores[_key] = arguments[_key];
        }

        this._stores = [].concat(this._stores, stores);
    };

    RefluxDispatcher.prototype.on = function on() {
        for (var _len2 = arguments.length, rest = Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
            rest[_key2] = arguments[_key2];
        }

        this._stores.forEach(function (store) {
            return store.on.apply(store, rest);
        });
    };

    RefluxDispatcher.prototype.off = function off() {
        for (var _len3 = arguments.length, rest = Array(_len3), _key3 = 0; _key3 < _len3; _key3++) {
            rest[_key3] = arguments[_key3];
        }

        this._stores.forEach(function (store) {
            return store.off.apply(store, rest);
        });
    };

    RefluxDispatcher.prototype.one = function one() {
        for (var _len4 = arguments.length, rest = Array(_len4), _key4 = 0; _key4 < _len4; _key4++) {
            rest[_key4] = arguments[_key4];
        }

        this._stores.forEach(function (store) {
            return store.one.apply(store, rest);
        });
    };

    RefluxDispatcher.prototype.trigger = function trigger() {
        for (var _len5 = arguments.length, rest = Array(_len5), _key5 = 0; _key5 < _len5; _key5++) {
            rest[_key5] = arguments[_key5];
        }

        this._stores.forEach(function (store) {
            return store.trigger.apply(store, rest);
        });
    };

    return RefluxDispatcher;
}();

if (typeof module !== 'undefined') module.exports = RefluxDispatcher;