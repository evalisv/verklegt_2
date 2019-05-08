$(document).ready(function() {
    $('[data-selector="filter"]').click(function() {
        $('.filter').toggleClass('hidden');
        $(this).toggleClass('active');
    });

    $('li.level1 > label').click(function() {
        let region = $(this).text();
        switch (region) {
            case 'Höfuðborgarsvæðið':
                $('#capital').toggleClass('hidden');
                break;
            case 'Vesturland':
                $('#west').toggleClass('hidden');
                break;
            case 'Vestfirðir':
                $('#northwest').toggleClass('hidden');
                break;
            case 'Norðurland':
                $('#north').toggleClass('hidden');
                break;
            case 'Austurland':
                $('#east').toggleClass('hidden');
                break;
            case 'Suðurland':
                $('#south').toggleClass('hidden');
                break;
            case 'Suðurnes':
                $('#southwest').toggleClass('hidden');
                break;
        }
    });

    $('li.level1').on('change', 'input[type="checkbox"]', function() {
        let checkBoxes, isChecked, isCollapsed;
        let region = $(this).next('label').text();
        isCollapsed = $(this).parents('li.level1').find('ul.level2').hasClass('hidden');
        isChecked = $(this).prop('checked');
        switch (region) {
            case 'Höfuðborgarsvæðið':
                checkBoxes = $('#capital li input[type="checkbox"]');
                if (isChecked) {
                    checkBoxes.prop('checked', true);
                    if (isCollapsed) {
                        $('#capital').removeClass('hidden');
                    }
                } else {
                    checkBoxes.prop('checked', false);
                }
                break;
            case 'Vesturland':
                checkBoxes = $('#west li input[type="checkbox"]');
                if (isChecked) {
                    checkBoxes.prop('checked', true);
                    if (isCollapsed) {
                        $('#west').removeClass('hidden');
                    }
                } else {
                    checkBoxes.prop('checked', false);
                }
                break;
            case 'Vestfirðir':
                checkBoxes = $('#northwest li input[type="checkbox"]');
                if (isChecked) {
                    checkBoxes.prop('checked', true);
                    if (isCollapsed) {
                        $('#northwest').removeClass('hidden');
                    }
                } else {
                    checkBoxes.prop('checked', false);
                }
                break;
            case 'Norðurland':
                checkBoxes = $('#north li input[type="checkbox"]');
                if (isChecked) {
                    checkBoxes.prop('checked', true);
                    if (isCollapsed) {
                        $('#north').removeClass('hidden');
                    }
                } else {
                    checkBoxes.prop('checked', false);
                }
                break;
            case 'Austurland':
                checkBoxes = $('#east li input[type="checkbox"]');
                if (isChecked) {
                    checkBoxes.prop('checked', true);
                    if (isCollapsed) {
                        $('#east').removeClass('hidden');
                    }
                } else {
                    checkBoxes.prop('checked', false);
                }
                break;
            case 'Suðurland':
                checkBoxes = $('#south li input[type="checkbox"]');
                if (isChecked) {
                    checkBoxes.prop('checked', true);
                    if (isCollapsed) {
                        $('#south').removeClass('hidden');
                    }
                } else {
                    checkBoxes.prop('checked', false);
                }
                break;
            case 'Suðurnes':
                checkBoxes = $('#southwest li input[type="checkbox"]');
                if (isChecked) {
                    checkBoxes.prop('checked', true);
                    if (isCollapsed) {
                        $('#southwest').removeClass('hidden');
                    }
                } else {
                    checkBoxes.prop('checked', false);
                }
                break;
        }
    });
});
