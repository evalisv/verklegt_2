$(document).ready(function() {
    // Selectors
    let makeOffer = $('.content-container.make-offer');

    if (makeOffer.length > 0) {
        addClassNamesToLabels();
    }
});

function addClassNamesToLabels() {
    // Selectors
    let amount = $('label[for="id_amount"]');
    let expires = $('label[for="id_expires_day"]');

    amount.addClass('col-3 float-left');
    expires.addClass('col-3 float-left');
}