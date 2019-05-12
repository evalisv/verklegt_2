$(document).ready(function(){
    if ($('.content-container.register-user').length > 0) {
        fillOutUserName();
        addClassNamesToLabels();
        manipulateHtml();
    }

    if ($('.register-user ul.errorlist').length > 0) {
        $('.register-user ul.errorlist').addClass('alert alert-danger py-1');
        if ($('.register-user ul.errorlist li').text() === 'A user with that username already exists.') {
            $('label[for="id_username"] + ul.errorlist').addClass('username-error');
            $('.register-user ul.errorlist li').text('Notandi með þetta netfang er þegar skráður.');
        }
    }
});

function addClassNamesToLabels() {
    $('.register-user label[for="id_first_name"]')
        .addClass('form-group-1 col-sm-4');
    $('.register-user label[for="id_last_name"]')
        .addClass('form-group-2 col-sm-4');
    $('.register-user label[for="id_email"]')
        .addClass('form-group-3 col-sm-4');
    $('.register-user label[for="id_password1"]')
        .addClass('form-group-4 col-sm-4');
    $('.register-user label[for="id_password2"]')
        .addClass('form-group-5 col-sm-4');
    $('.register-user label[for="id_kennitala"]')
        .addClass('form-group-6 col-sm-4');
    $('.register-user label[for="id_phone_number"]')
        .addClass('form-group-6 col-sm-2');
    $('.register-user label[for="id_address"]')
        .addClass('form-group-7 col-sm-4');
    $('.register-user label[for="id_postal_code"]')
        .addClass('form-group-8 col-sm-4');
    $('.register-user label[for="id_country"]')
        .addClass('form-group-8 col-sm-2');
}

function manipulateHtml() {
    $('.register-user .form-group-1').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-2').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-3').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-4').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-5').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-6').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-7').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-8').wrapAll('<div class="row p-2" />');
}

function fillOutUserName() {
    $('#id_username').removeAttr('autofocus').addClass('disabled');
    $('#id_email').on('keyup', function() {
        let email = $('#id_email').val();
        $('#id_username').val(email);
    });
}
