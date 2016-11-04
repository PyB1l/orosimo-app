riot.tag2('post', '<article class="single-from-blog"> <div class="blog-comment"> <h2>Άφησε το σχόλιο σου ...</h2> <form class="comment-form" onsubmit="{addComment}"> <div class="form-group"> <input type="text" placeholder="Όνομα" name="name" class="form-control"> </div> <div class="form-group"> <input placeholder="Enter Email" name="email" class="form-control" type="email"> </div> <div class="form-group"> <textarea class="form-control" name="body"></textarea> </div> <button class="button button-default" data-text="Comment" type="submit"><span>Comment</span></button> <button class="button button-default" data-text="Like" onclick="{addLike}"><span>Like</span></button> <button class="button button-default" data-text="περισσότερα νέα" onclick="{allPosts}"> <span> περισσότερα νέα </span> </button> </form> </div> </article> <br> <br> <br> <div id="like" style="display: none" class="alert alert-success alert-dismissible" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> <strong>Συγxαρητήρια!</strong> Το Like στο άρθρο καταχωρήθηκε. </div> <div id="comment" style="display: none" class="alert alert-success alert-dismissible" role="success"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> <strong>Συγxαρητήρια!</strong> Το Comment στο άρθρο καταχωρήθηκε. </div>', '', '', function(opts) {

    this.post = opts.post_id
    this.like_api = '/admin/api/post/like/'
    this.comment_api = '/admin/api/post/comment/'
    var self = this

    this.allPosts = function(event) {
        event.preventDefault()
        window.location = '/posts';
    }.bind(this)

    this.addLike = function(event) {
        event.preventDefault()
         $.ajax({
            type: "POST",
            url: self.like_api + self.post,
        }).done(function(resp) {
            $("  #like").fadeIn("fast")
        })
    }.bind(this)

    this.addComment = function(event) {
        event.preventDefault()

        comment_data = {
            person: self.name.value,
            email: self.email.value,
            body: self.body.value
        }

         $.ajax({
            type: "POST",
            url: self.comment_api + self.post,
            data: JSON.stringify(comment_data),
            contentType: "application/json"
        }).done(function(resp) {
            $("  #comment").fadeIn("fast")
        })
    }.bind(this)

});