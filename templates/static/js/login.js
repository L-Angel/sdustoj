
/**
 * Created by Lonely on 2015/12/31.
 */
$(function(){
    $username= $.cookie('uname')
   // alert($username);
    if(!isSpace($username)){
        $('.headnavactions').html('<a class=\"headnavtitle\" href=\"useredit\">'+'Welcome '+$username+'</a>');
    }
});

function isSpace(data){
    if(data==""||data==null||data=='null'){
        return true;
    }
    return false;
}