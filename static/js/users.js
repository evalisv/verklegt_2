$(document).ready(function(){
    // Selectors
    let registerUserContainer = $('.content-container.register-user');
    let registerUserErrors = $('.register-user ul.errorlist');
    let registerUserErrorsItem = $('.register-user ul.errorlist li');
    let loginUserContainer = $('.content-container.login-user');
    let updateProfileContainer = $('.content-container.update-profile');

    if (registerUserContainer.length > 0) {
        fillOutUserName();
        addClassNamesToLabels();
        manipulateHtml();
    }

    if (registerUserErrors.length > 0) {
        registerUserErrors.addClass('alert alert-danger py-1');
        if (registerUserErrorsItem.text() === 'A user with that username already exists.') {
            $('label[for="id_username"] + ul.errorlist').addClass('username-error');
            $(registerUserErrorsItem).text('Notandi með þetta netfang er þegar skráður.');
        }
    }

    if (loginUserContainer.length > 0) {
        $('label[for="id_username"]').text('Notendanafn:');
        $('label[for="id_password"]').text('Lykilorð:');
    }

    if (updateProfileContainer.length > 0) {
        manipulateUpdateFormHtml();
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

function manipulateUpdateFormHtml() {
    let updateProfileForm = $('.content-container.update-profile form');
    let profileImage = $('.update-profile a[href^="media/media/users"]');
    let newHtml = $(updateProfileForm).html().toString()
        .replace('Núverandi mynd:', '<label id="for-current">Núverandi mynd:</label>')
        .replace('Skipta um mynd:', '<label id="for-changing">Skipta um mynd:</label>');
    $(updateProfileForm).html(newHtml);

    $('#for-current').next('a').wrap('<div class="col-4 profile-image-display image-wrapper" />');
    let imgSource = profileImage.attr('href');
    $('.profile-image-display.image-wrapper').prepend('<img src="/' + imgSource + '"/>');
    $('#for-current, .profile-image-display, #for-changing, #id_profile_image')
        .wrapAll('<div class="row my-2" id="profile-image-container" />');
    // $('#profile-image-container').wrap('<div class="row" />');
    $('#profile-image-container').appendTo(updateProfileForm);
    $('#submit-profile-changes').appendTo(updateProfileForm);
    $('.update-profile label').addClass('col-2');

    $('label[for="id_address"]').addClass('form-group-2');
    $('label[for="id_phone_number"], label[for="id_postal_code"], label[for="id_country"]')
        .addClass('form-group-3');

    $('.form-group-2').wrapAll('<div class="group-2 row my-2" />');
    $('.form-group-3').wrapAll('<div class="group-3 row my-2" />');
    $('.update-profile .group-3').insertAfter('.group-2');
}