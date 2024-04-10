function passwordForgotActionChange(){
    var form = document.forms["LoginForm"];
    form.action = "/passwordForgot";
    form.submit();
}