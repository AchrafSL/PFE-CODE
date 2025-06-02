function redirectToHome(url){
    window.location.href = url;

}
function redirectToLogin(url){
    window.location.href = url;
}

function GoToUSR_Page(url){
    window.location.href = url;
}
function redirectToHomeAction(variable2){
    var form = document.forms[variable2];
    form.action = "/home";
    form.method = "GET";
    form.submit();
}