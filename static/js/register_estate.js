$(document).ready(function() {
    // Selectors
    let register = '.content-container.register-estate';
    let update = '.content-container.update-estate';

    if ($(register).length > 0 || $(update).length > 0) {
        let container;
        if ($(register).length > 0) {
            container = 'register';

        } else {
            container = 'update'
        }

        addLabelClassNames(container);
        rearrangeHtml();

        $('#id_open_house').after('<div class="input-group-append" data-target="#datetimepicker1" data-toggle="datetimepicker">\n' +
            '<div class="input-group-text"><i class="fa fa-calendar"></i></div>\n' +
            '</div>');
        $('.datetimepicker-input, .input-group-append')
            .wrapAll('<div class="input-group date col-sm-4" id="datetimepicker1" data-target-input="nearest" />')
    }
});

function addLabelClassNames(form) {
    // Selectors
    let address = '.content-container.' + form + '-estate label[for="id_address"]';
    let postal_code = '.content-container.' + form + '-estate label[for="id_postal_code"]';
    let size = '.content-container.' + form + '-estate label[for="id_size"]';
    let bedrooms = '.content-container.' + form + '-estate label[for="id_bedrooms"]';
    let bathrooms = '.content-container.' + form + '-estate label[for="id_bathrooms"]';
    let price = '.content-container.' + form + '-estate label[for="id_price"]';
    let fasteignamat = '.content-container.' + form + '-estate label[for="id_fasteignamat"]';
    let brunabotamat = '.content-container.' + form + '-estate label[for="id_brunabotamat"]';
    let type = '.content-container.' + form + '-estate label[for="id_type"]';
    let yearBuilt = '.content-container.' + form + '-estate label[for="id_year_built"]';
    let entry = '.content-container.' + form + '-estate label[for="id_entry"]';
    let elevator = '.content-container.' + form + '-estate label[for="id_elevator"]';
    let garage = '.content-container.' + form + '-estate label[for="id_garage"]';
    let description = '.content-container.' + form + '-estate label[for="id_description"]';
    let openHouse = '.content-container.' + form + '-estate label[for="id_open_house"]';
    let images = '.content-container.' + form + '-estate label[for="id_images"]';

    $(address).addClass('form-group-1 col-sm-2');
    $(postal_code).addClass('form-group-1 col-sm-2');
    $(size).addClass('form-group-2 col-sm-2');
    $(bedrooms).addClass('form-group-2 col-sm-2');
    $(bathrooms).addClass('form-group-2 col-sm-2');
    $(price).addClass('form-group-3 col-sm-2');
    $(fasteignamat).addClass('form-group-3 col-sm-2');
    $(brunabotamat).addClass('form-group-3 col-sm-2');
    $(type).addClass('form-group-4 col-sm-2');
    $(yearBuilt).addClass('form-group-4 col-sm-2');
    $(entry).addClass('form-group-5 col-sm-2');
    $(elevator).addClass('form-group-5 col-sm-2');
    $(garage).addClass('form-group-5 col-sm-2');
    $(description).addClass('form-group-6 col-sm-2');
    $(openHouse).addClass('form-group-7 col-sm-2');
    $(images).addClass('form-group-7 col-sm-2');
}

function rearrangeHtml() {
    $('.form-group-1').wrapAll('<div class="row p-4" />');
    $('.form-group-2').wrapAll('<div class="row p-4" />');
    $('.form-group-3').wrapAll('<div class="row p-4" />');
    $('.form-group-4').wrapAll('<div class="row p-4" />');
    $('.form-group-5').wrapAll('<div class="row p-4" />');
    $('.form-group-6').wrapAll('<div class="row p-4" />');
    $('.form-group-7').wrapAll('<div class="row p-4" />');
}

