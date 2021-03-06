'use strict';

riot.tag2('post', '<article class="single-from-blog"> <div class="blog-comment"> <h2>Άφησε το σχόλιο σου ...</h2> <form class="comment-form" onsubmit="{addComment}"> <div class="form-group"> <input type="text" placeholder="Όνομα" name="name" class="form-control"> </div> <div class="form-group"> <input placeholder="Enter Email" name="email" class="form-control" type="email"> </div> <div class="form-group"> <textarea class="form-control" name="body"></textarea> </div> <button class="button button-default" data-text="Comment" type="submit"><span>Comment</span></button> <button class="button button-default" data-text="Like" onclick="{addLike}"><span>Like</span></button> <button class="button button-default" data-text="περισσότερα νέα" onclick="{allPosts}"> <span> περισσότερα νέα </span> </button> </form> </div> </article> <br> <br> <br> <div id="like" style="display: none" class="alert alert-success alert-dismissible" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> <strong>Συγxαρητήρια!</strong> Το Like στο άρθρο καταχωρήθηκε. </div> <div id="comment" style="display: none" class="alert alert-success alert-dismissible" role="success"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> <strong>Συγxαρητήρια!</strong> Το Comment στο άρθρο καταχωρήθηκε. </div>', '', '', function (opts) {
    var tag = this;

    tag.post = opts.post_id;
    tag.like_api = '/admin/api/post/like/';
    tag.comment_api = '/admin/api/post/comment/';
    tag.allPosts = allPosts;
    tag.addLike = addLike;
    tag.addComment = addComment;

    function allPosts(event) {
        event.preventDefault();
        window.location = '/posts';
    }

    function addLike(event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: tag.like_api + tag.post
        }).done(function () {
            $(" #like").fadeIn("fast");
        });
    }

    function addComment(event) {
        event.preventDefault();

        var comment_data = {
            person: tag.name.value,
            email: tag.email.value,
            body: tag.body.value
        };

        $.ajax({
            type: "POST",
            url: tag.comment_api + tag.post,
            data: JSON.stringify(comment_data),
            contentType: "application/json"
        }).done(function () {
            $(" #comment").fadeIn("fast");
        });
    }
});