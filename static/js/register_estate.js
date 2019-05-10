$(document).ready(function() {
    if ($('.content-container.register-estate').length > 0) {
        addClassNamesToLabels();
        manipulateHtml();
    }
});

function addClassNamesToLabels() {
    $('label[for="id_address"], label[for="id_postal_code"]')
        .addClass('form-group-1 col-sm-2');
    $('label[for="id_size"], label[for="id_bedrooms"], label[for="id_bathrooms"]')
        .addClass('form-group-2 col-sm-2');
    $('label[for="id_price"], label[for="id_fasteignamat"], label[for="id_brunabotamat"]')
        .addClass('form-group-3 col-sm-2');
    $('label[for="id_type"], label[for="id_year_built"]')
        .addClass('form-group-4 col-sm-2');
    $('label[for="id_entry"], label[for="id_elevator"], label[for="id_garage"]')
        .addClass('form-group-5 col-sm-2');
    $('label[for="id_description"]')
        .addClass('form-group-6 col-sm-2');
    $('label[for="id_images"]')
        .addClass('form-group-7 col-sm-2');
}

function manipulateHtml() {
    $('.form-group-1').wrapAll('<div class="row p-4" />');
    $('.form-group-2').wrapAll('<div class="row p-4" />');
    $('.form-group-3').wrapAll('<div class="row p-4" />');
    $('.form-group-4').wrapAll('<div class="row p-4" />');
    $('.form-group-5').wrapAll('<div class="row p-4" />');
    $('.form-group-6').wrapAll('<div class="row p-4" />');
    $('.form-group-7').wrapAll('<div class="row p-4" />');
}