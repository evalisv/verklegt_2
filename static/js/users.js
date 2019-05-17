$(document).ready(function(){
    // Selectors
    let registerUserContainer = $('.content-container.register-user');
    let userErrors = $('ul.errorlist');
    let loginUserContainer = $('.content-container.login-user');
    let updateProfileContainer = $('.content-container.update-profile');

    if (registerUserContainer.length > 0) {
        addClassNamesToLabels();
        manipulateHtml();
    }

    if (userErrors.length > 0) {
        if ($('ul.errorlist ul.errorlist').length > 0) {
            $('div > ul.errorlist > li').css('color', 'rgba(230,230,230,0.9)');
            $('ul.errorlist ul.errorlist').addClass('alert alert-danger py-1')
        } else {
            userErrors.addClass('alert alert-danger py-1');
        }
    }

    if (loginUserContainer.length > 0) {
        $('label[for="id_username"]').text('Notendanafn:');
        $('label[for="id_password"]').text('Lykilorð:');
    }

    if (updateProfileContainer.length > 0) {
        $('#profile_image-clear_id, label[for="profile_image-clear_id"]').addClass('hidden');
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
    $('.register-user label[for="id_username"]')
        .addClass('form-group-4 col-sm-4');
    $('.register-user label[for="id_password1"]')
        .addClass('form-group-5 col-sm-4');
    $('.register-user label[for="id_password2"]')
        .addClass('form-group-6 col-sm-4');
    $('.register-user label[for="id_kennitala"]')
        .addClass('form-group-7 col-sm-4');
    $('.register-user label[for="id_phone_number"]')
        .addClass('form-group-7 col-sm-2');
    $('.register-user label[for="id_address"]')
        .addClass('form-group-8 col-sm-4');
    $('.register-user label[for="id_postal_code"]')
        .addClass('form-group-9 col-sm-4');
    $('.register-user label[for="id_country"]')
        .addClass('form-group-9 col-sm-2');
    $('.register-user label[for="id_profile_image"]')
        .addClass('form-group-10 col-sm-4 my-2')
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
    $('.register-user .form-group-9').wrapAll('<div class="row p-2" />');
    $('.register-user .form-group-10').wrapAll('<div class="row p-2" />');
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

    let profileImageContainer = $('#profile-image-container');
    profileImageContainer.wrap('<div class="row" />');
    profileImageContainer.appendTo(updateProfileForm);
    $('.update-profile label').addClass('col-2');

    $('label[for="id_address"]').addClass('form-group-2');
    $('label[for="id_kennitala"]').addClass('form-group-1');
    $('label[for="id_phone_number"], label[for="id_postal_code"], label[for="id_country"]')
        .addClass('form-group-3');

    $('.form-group-1').wrapAll('<div class="group-1 row my-2" />');
    $('.form-group-2').wrapAll('<div class="group-2 row my-2" />');
    $('.form-group-3').wrapAll('<div class="group-3 row my-2" />');
    $('.update-profile .group-3').insertAfter('.group-2');

    $('#submit-profile-changes-wrapper').appendTo(updateProfileForm);
}