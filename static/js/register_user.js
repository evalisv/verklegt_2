$(document).ready(function(){
    $('#register').click(function(e) {

        let pw1 = $('#id_password1').val()
        let pw2 = $('#id_password2').val()

        if(pw1 !== pw2){
            e.preventDefault()
        }
        else if(pw1.length < 8 && pw2.length < 8){
            e.preventDefault()
            console.log('password eru of stutt og event data er: ' + e.data)
        }

        else {
            console.log('password stemma og eru í lagi')
        }


    })
});