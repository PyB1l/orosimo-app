'use strict';

riot.tag2('newsletter', '<div class="single-widget"> <h2>Newsletter</h2> <hr> <div id="complete" style="display: none" class="alert alert-success alert-dismissible" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> <strong>Συγxαρητήρια!</strong> Η εγγραφή σας στο newsletter ολοκληρώθηκε με επιτυχία. . </div> <form class="blog-search"> <input ref="submit" type="text"> <button class="button button-default" data-text="Subscribe" onclick="{register}" type="submit"><span>Εγγραφή</span></button> </form> <hr> </div>', '', '', function (opts) {
    var tag = this;
    tag.api = '/newsletter';
    tag.register = register;
    tag.validateEmail = validateEmail;

    function validateEmail(value) {
        var atpos = value.indexOf("@");
        var dotpos = value.lastIndexOf(".");

        if (atpos < 1 || dotpos - atpos < 2) {
            return false;
        }
        return true;
    }

    function register(e) {
        e.preventDefault();

        if (!tag.validateEmail(tag.refs.submit.value)) {

            alert('Invalid email for newsletter: ' + tag.refs.submit.value);
            tag.refs.submit.value = '';
            return false;
        }

        var post_data = {
            email: tag.refs.submit.value
        };

        $.ajax({
            type: "POST",
            url: tag.api,
            data: JSON.stringify(post_data),
            contentType: "application/json"
        }).done(function (res) {
            console.log(res);
            tag.refs.submit.value = '';
            $("#complete").fadeIn("fast");
        });
    }
});