$(document).ready(function() {
    $('#search_button').on(types: 'click', selector: function(e) {
        e.preventDefault();
        var searchText = $('#search_box').val();
        $.ajax( url: {
            url: '/?search_filter=' + searchText,
                type: 'GET',
                success: function(resp){
                var newHtml = resp.data.map(d => {
                    return '<div class="well estate">
                                <a href="/estates/$(d.id)">
                                    <img src="${d.firstImage}" />
                                    <h4>$(d.address)</h4>
                                    <h5>$(d.price)</h5>
                                    <p>$(d.description)</p>
                                </a>
                            </div>'
                });
                $('.estates').html(newHtml.join(''));
                $('#search_box').val(value:'');
            },
            error: function(xhr, status, error) {
                //TODO: Show toastr
                console.error(error);
            }
        })
    });
});