'use strict';

riot.tag2('search', '<div class="single-widget"> <h2>ΑΝΑΖΗΤΗΣΗ</h2> <form class="blog-search" onsubmit="{search}"> <input type="text" name="search_term"> <button class="button button-default" data-text="Search" type="submit"><span>Search</span></button> </form> </div>', '', '', function (opts) {
    var tag = this;
    tag.results = [];
    tag.search = search;

    function search(event) {
        event.preventDefault();

        $.getJSON(self.api + '?term=' + tag.search_term.value).done(function (resp) {
            console.log(resp);
        });
    }
});