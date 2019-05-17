$(document).ready(function() {
    let regChecked = document.getElementById("agree-to-terms");
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