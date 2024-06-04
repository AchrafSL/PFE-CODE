function confirmCommentOperation()
{

    var result = confirm("Are you sure you want to delete this comment ?? ");
    if(result){
        return true;
    }
    else{
        return false;
    }
    
}