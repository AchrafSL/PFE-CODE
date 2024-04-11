function validateForm() {
    var email = document.forms["SignupForm"]["email"].value;
    var password  = document.forms["SignupForm"]["password"].value;
    var firstname= document.forms["SignupForm"]["firstname"].value;
    var lastname = document.forms["SignupForm"]["lastname"].value;

    if (email == "" || password == "" || firstname == "" || lastname == "") {
        document.getElementById("errorMsg").innerHTML = "Please fill in all fields";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }

    // Test if the email is valid : MSG "Please enter a valid email address"

/*  /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

    These are called regex (Regular Expression) : is a squence of char that specifies a search pattern

    [ - - - - ] char set 
    ^                     # Asserts the start of the string
    ([A-Za-z0-9_\-\.])+   # Matches one or more characters from A-Z, a-z, 0-9, underscore (_), hyphen (-), or period (.)
    \@                    # Matches the "@" symbol
    ([A-Za-z0-9_\-\.])+   # Matches one or more characters from A-Z, a-z, 0-9, underscore (_), hyphen (-), or period (.)
    \.                    # Matches the period (dot)
    ([A-Za-z]{2,4})       # Matches two to four characters from A-Z or a-z
    $                     # Asserts the end of the string

    ----------------------------------------------------------------------------------------------
    // Regex Explained : (/pattern/attributs)
    attributs : 
    g | Global search 
    i | Case insensitive search
    m | multi-line search
    etc....
    | you can combine attributs like gi ....

    Pattern :
    -----------

    Special char :
    / M/ search for space and M 
    /abc/ search for abc
    /ab*c/ search for ac abc abbc abbbbbbb...c | as many as b {0 , +oo} 
    /ab+c/ do same thing but | b {1, +oo}
    /ab?c/ do same thing but | b {0 , 1}
    /ab{n}c/ same thing but exactly n times
    /ab{n,}c/ same thing but  | b {n , +oo}
    /ab{n,m}c/ |  same thing but | b {n , m}
    * is a special char (like * , + , ? , ... ) Do some shortcut work

    Groups and ranges :
    /x|y/ matches x or y example : "Green or red Apple" replace /Green|Red/gi with _  ->    _ or _ Apple
    /[xyz]/ any occurence of x or y or z  same job as /x|y|z/
    /[x-z]/ any occurence of the chars between [x,z] also x and z
    /[^xyz] every char but xyz | it like negation 
    /(xyz)/ match the group xyz not x or y or z

    Char Classes :
    /.y/ | matches any single char except line terminator \n  , \r for example : ay by cy my ..
    /\d/ | /[0-9]/
    /\D/ | /[^0-9]/
    /\w/ | /[A-Za-z0-9_]/
    /\W/ | /[^A-Za-z0-9_]/
    /\s/ | matches a white space
    /\S/ | matches a single char other than white space

    Assertions:
    ^ | matches the start of the string example: /^[xyz]/
        match : 'xyz =>' but not '=>xyz' the string should start with the pattern after ^
    $ | matches the end of the string example: /[xyz]$/
        match : '=> xyz' but not 'xyz =>' the string should end with pattern before $
    
    x(?=y) | ...
    x(?!y) | ...
    (?<=y)x | ...
    (?<!y)x | ...
    \b | ...
    \B | ..

    ----------------------------------------------------------------------------------------------
*/
    const emailPattern = /^[A-Za-z0-9_\-\.]+\@[A-Za-z0-9_\-\.]+\.[A-Za-z]{2,4}$/ ;
    // match is not working because emailPattern is not a string it's a regex
    if (!emailPattern.test(email)){
        // NOT A VALID EMAIL :
        document.getElementById("errorMsg").innerHTML = "Please enter a valid email address";
        document.getElementById("errorMsg").style.display = "block";
        return false;
    }

     
    // Test if the password is valid : MSGS
    // 1" Password requires at least one lowercase character"
    // 2 " Password requires at least one uppercase character"
    // 3 "Password requires at least one special character "
    // 4 "Password requires at least one number "
    // 5 "Password requires 8 characters minimum"

    return true; // Allow form submission
}
