riot.tag2('success', '<div class="blog-comment"> <blockquote style="font-family: \'Roboto Condensed\', sans-serif"> Γιατί οι δικές σας επιτυχίες μασ επιβεβαιώνουν στην πράξη εδώ και 25 χρόνια!<br> <cite style="font-family: \'Roboto Condensed\', sans-serif"> - επιτελέιο ΟΡΟΣΗΜΟ</cite> </blockquote> <div class="single-widget"> <ul class="nav nav-tabs"> <li class="dropdown"> <a class="dropdown-toggle" data-toggle="dropdown" href="#" style="font-family: \'Roboto Condensed\', sans-serif">Έτος <b class="caret"></b></a> <ul class="dropdown-menu"> <li each="{available}" onclick="{load}"><a href="#{school_year}" role="tab" data-toggle="tab">{school_year}</a></li> </ul> </li> <li role="presentation" class="disabled active"><a href="#" style="font-family: \'Roboto Condensed\', sans-serif">{current}</a></li> </ul> <div class="single-from-blog"> <table class="table table-hover table-striped"> <thead class="thead-inverse"> <tr> <th style="font-family: \'Roboto Condensed\', sans-serif">Ονοματεπώνυμο</th> <th style="font-family: \'Roboto Condensed\', sans-serif">Τμήμα</th> </tr> </thead> <tbody> <tr each="{success_list}"> <td>{full_name}</td> <td> {university} </td> </tr> </tbody> </table> </div> </div> </div>', '', '', function(opts) {

    this.current = ''
    this.available = []
    this.success_list = []
    this.get_years = '/admin/api/success/available'
    this.get_success = '/admin/api/success/get_year/'
    var self = this

    this.on("mount", function() {
        $.getJSON(self.get_years).done(function(resp) {
            self.available = resp.data.years
            self.load_year(self.available[0].school_year)
          })
    })

    this.load_year = function(year) {
        $.getJSON(self.get_success + year).done(function(resp) {
            self.success_list = resp.data
            self.current = year
            self.update()
         })
    }.bind(this)

    this.load = function(event) {
        event.preventDefault()
        request_year = event.currentTarget.innerText
        self.load_year(request_year)
    }.bind(this)
});