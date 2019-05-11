$(document).ready(function(){
    $('#register').click(function(e) {

        let pw1 = $('#id_password1').val()
        let pw2 = $('#id_password2').val()

        if(pw1 !== pw2){
            e.preventDefault()
        }



    })
});