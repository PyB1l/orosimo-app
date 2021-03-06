'use strict';

riot.tag2('news', '<div class="single-widget"> <h2>ΟΡΟΣΗΜΟ νέα</h2> <div class="popular-post-widget"> <div class="media" each="{newslist}"> <div class="media-left"> <a href="/posts/{id}"> <i class="fa fa-rss-square wc-icon" style="font-size: 6em; color: #ee4532"></i> </a> </div> <div class="media-body"> <h4 class="media-heading"><a href="/posts/{id}">{title}</a></h4> <p>{body}</p> </div> </div> </div> </div>', '', '', function (opts) {
    var tag = this;
    tag.newslist = [];
    tag.api = '/api/v1.0/posts?limit=3';

    tag.on("mount", function () {
        $.getJSON(tag.api).done(function (resp) {
            tag.newslist = resp.data;
            tag.newslist.forEach(function (post) {
                post.body = post.body.slice(0, 60) + ' ...';
            });
            tag.update();
            console.dir(tag.newslist);
        });
    });
});