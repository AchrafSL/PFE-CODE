function passwordForgotActionChange(){
    var form = document.forms["LoginForm"];
    form.action = "/passwordForgot";
    form.submit();
}
function ReturnToLoginActionChange(){
    var form = document.forms["ResetPassword"];
    form.action = "/Login";
    form.method = "GET";
    form.submit();
}