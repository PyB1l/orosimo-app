'use strict';

riot.tag2('register', '<div class="blog-comment"> <h2>Online Εγγραφή</h2> <form id="register" class="comment-form" onsubmit="{register}" class="{hidden: submitted}" name="form"> <div class="form-group"> <input name="first_name" type="text" placeholder="Όνομα" class="form-control"> </div> <div class="form-group"> <input name="last_name" type="text" placeholder="Επώνυμο" class="form-control"> </div> <div class="form-group"> <input name="area" type="text" placeholder="Περιοχή" class="form-control"> </div> <div class="form-group"> <select name="grade" class="form-control selectpicker" title="Σχολική Tάξη"> <option value="Γ Λυκείου">Γ Λυκείου</option> <option value="Β Λυκείου">B Λυκείου</option> <option value="Α Λυκείου">A Λυκείου</option> <option value="Γυμνάσιο">Γυμνάσιο</option> <option value="ΕΠΑΛ">ΕΠΑΛ</option> <option value="Νυχτερινό">Νυχτερινό ΓΕΛ</option> </select> </div> <div class="form-group"> <input name="email" placeholder="Email" class="form-control" type="email"> </div> <div class="form-group"> <input name="phone" type="text" placeholder="Τηλέφωνο" class="form-control"> </div> <div class="form-group"> <textarea name="comment" class="form-control" placeholder="σχόλιο"></textarea> </div> <button class="button button-default" data-text="υποβολή" type="submit"><span>υποβολή</span></button> </form><br><br><hr> <div id="complete" style="display: none" class="alert alert-success alert-dismissible" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> <strong>Συγxαρητήρια!</strong> To email με τα στοιχεια εγγραφής σας έχει αποσταλεί στην γραμματεία. Θα επικοινωνήσουμε άμεσα μαζί στον αριθμό τηλεφώνου που συμπληρώσατε στην φορμα. </div> </div>', '.hidden { display: None }', '', function (opts) {
    var tag = this;

    tag.api = '/register';
    tag.submitted = true;
    tag.register = register;

    function register(event) {
        event.preventDefault();

        var register_data = {
            name: tag.first_name.value + ' ' + tag.last_name.value,
            class: tag.grade.value,
            phone: tag.phone.value,
            school: tag.grade.value,
            address: tag.area.value
        };

        $.ajax({
            type: "POST",
            url: tag.api,
            data: JSON.stringify(register_data),
            contentType: "application/json"
        }).done(function () {
            $("#complete").fadeIn("fast");
        });
    }
});