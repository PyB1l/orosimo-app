class RefluxDispatcher {

    constructor(){
        this._stores = []
    }

    addStore(...stores){
        this._stores = [ ...this._stores, ...stores];
    }

    on( ...rest){
        this._stores.forEach(store => store.on( ...rest))
    }
    off(...rest){
        this._stores.forEach(store => store.off( ...rest))
    }
    one(...rest){
        this._stores.forEach(store => store.one( ...rest))
    }
    trigger(...rest){
        this._stores.forEach(store => store.trigger( ...rest))
    }
}

if (typeof(module) !== 'undefined') module.exports = RefluxDispatcher;