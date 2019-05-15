$(document).ready(function() {
    // addClassNamesToLabels();
    if ($('.content-container.register-estate').length > 0 || $('.content-container.update-estate').length > 0) {
        console.log('if');
        // addClassNamesToLabels();

        $('.register-estate label[for="id_address"], .register-estate label[for="id_postal_code"], .update-estate label[for="id_address"], .update-estate label[for="id_postal_code"]')
        .addClass('form-group-1 col-sm-2');
    $('.register-estate label[for="id_size"], .register-estate label[for="id_bedrooms"], .register-estate label[for="id_bathrooms"], .update-estate label[for="id_size"], .update-estate label[for="id_bedrooms"], .update-estate label[for="id_bathrooms"]')
        .addClass('form-group-2 col-sm-2');
    $('.register-estate label[for="id_price"], .register-estate label[for="id_fasteignamat"], .register-estate label[for="id_brunabotamat"], .register-estate label[for="id_price"], .register-estate label[for="id_fasteignamat"], .register-estate label[for="id_brunabotamat"]')
        .addClass('form-group-3 col-sm-2');
    $('.register-estate label[for="id_type"], .register-estate label[for="id_year_built"]')
        .addClass('form-group-4 col-sm-2');
    $('.register-estate label[for="id_entry"], .register-estate label[for="id_elevator"], .register-estate label[for="id_garage"]')
        .addClass('form-group-5 col-sm-2');
    $('.register-estate label[for="id_description"]')
        .addClass('form-group-6 col-sm-2');
    $('.register-estate label[for="id_images"], .register-estate label[for="id_open_house"]')
        .addClass('form-group-7 col-sm-2');

        manipulateHtml();
        $('#id_open_house').after('<div class="input-group-append" data-target="#datetimepicker1" data-toggle="datetimepicker">\n' +
            '<div class="input-group-text"><i class="fa fa-calendar"></i></div>\n' +
            '</div>');
        $('.datetimepicker-input, .input-group-append').wrapAll('<div class="input-group date col-sm-4" id="datetimepicker1" data-target-input="nearest" />')
    }
});

function addClassNamesToLabels() {
    console.log('add classnames');
    $('.register-estate label[for="id_address"], .register-estate label[for="id_postal_code"]')
        .addClass('form-group-1 col-sm-2');
    $('.register-estate label[for="id_size"], .register-estate label[for="id_bedrooms"], .register-estate label[for="id_bathrooms"]')
        .addClass('form-group-2 col-sm-2');
    $('.register-estate label[for="id_price"], .register-estate label[for="id_fasteignamat"], .register-estate label[for="id_brunabotamat"]')
        .addClass('form-group-3 col-sm-2');
    $('.register-estate label[for="id_type"], .register-estate label[for="id_year_built"]')
        .addClass('form-group-4 col-sm-2');
    $('.register-estate label[for="id_entry"], .register-estate label[for="id_elevator"], .register-estate label[for="id_garage"]')
        .addClass('form-group-5 col-sm-2');
    $('.register-estate label[for="id_description"]')
        .addClass('form-group-6 col-sm-2');
    $('.register-estate label[for="id_images"], .register-estate label[for="id_open_house"]')
        .addClass('form-group-7 col-sm-2');
}

function manipulateHtml() {
    console.log('add man');
    $('.form-group-1').wrapAll('<div class="row p-4" />');
    $('.form-group-2').wrapAll('<div class="row p-4" />');
    $('.form-group-3').wrapAll('<div class="row p-4" />');
    $('.form-group-4').wrapAll('<div class="row p-4" />');
    $('.form-group-5').wrapAll('<div class="row p-4" />');
    $('.form-group-6').wrapAll('<div class="row p-4" />');
    $('.form-group-7').wrapAll('<div class="row p-4" />');
}
