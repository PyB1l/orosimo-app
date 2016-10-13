<search>
    <div class="single-widget">
        <h2>ΑΝΑΖΗΤΗΣΗ</h2>
        <form class="blog-search" onsubmit={ search }>
            <input type="text" name="search_term">
            <button class="button button-default" data-text="Search" type="submit"><span>Search</span></button>
        </form>
    </div>

    this.api = "/api/search"
    this.results = []

    var self = this

    search(event) {
        event.preventDefault()

        $.getJSON(self.api + '?term=' + self.search_term.value).done(
            function(resp) {
                console.log(resp)
            }
        )
    }

</search>