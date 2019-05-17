$(document).ready(function() {
    let regChecked = document.getElementById("register-estate-checked");
    let btnRegUser = document.getElementById("btn-register-user");

    regChecked.onclick = function(){
        console.log('clickeed');
        if(regChecked.checked == true){
            btnRegUser.disabled = false;
        }
        else{
            btnRegUser.disabled = true;
        }
    }
})