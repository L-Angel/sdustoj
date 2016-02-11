
/**
 * Created by Lonely on 2015/12/31.
 */
$(function(){
    	$.ajaxSetup({
  beforeSend: function(xhr, settings){
      var csrftoken = $.cookie('csrftoken');
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});
    $username= $.cookie('uname');
    $power= $.cookie('power');
   // alert($username);
    if(!isSpace($username)){
        if($power=='A'){
             $('.headnavactions').html('<a class=\"headnavtitle\" href=\"user?uname='+$username+'\">'+'Welcome '+$username+'</a>'+'<a class=\"headnavtitle\" href=\"\">'+'Terminal'+'</a>');
        }else{
             $('.headnavactions').html('<a class=\"headnavtitle\" href=\"user?uname='+$username+'\">'+'Welcome '+$username+'</a>'+ '<a class=\"headnavtitle\" href=\"loginout\">Login Out</a>');
        }

    }
});

function isSpace(data){
    if(data==""||data==null||data=='null'){
        return true;
    }
    return false;
}


/**
 * Created by sun on 2015/9/29.
 */
/*
$(document).ready(function(){
     //随机背景图片
    var random_bg=Math.floor(Math.random()*5+1);
    var bg='url(../img/loginbg_'+random_bg+'.jpg)';
    $("body").css("background-image",bg);

    // 检测是否已经登陆
    if($.session.get('isLogin') == 'true'){
        window.location='../../adminIndex/html/index.html';
    }

    // 初始化账号input获得焦点
    $("#user_name").focus();

    //移除验证码
    $("#hide").click(function(){
        $(".code").fadeOut("slow");
        return false;
    });
    //显示验证码
    $("#captcha").focus(function(){
        $(".code").fadeIn("fast");
        return false;
    });

    // 隐藏提示文字
    $("#user_name,#password,#captcha").focus(function(){
        $(".usernameinfo,.pwdinfo,.modiinfo,.modifierror,.pwderror").hide(200);
    });

    // 回车键登陆
    $(document).keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){
            $(".submit").trigger("click");
        }
    });

    // 登陆操作
    $(".submit").bind("click",function(){
        var username = $("#user_name").val();
        var password = $("#password").val();
        var modifi = $("#captcha").val();

        if(username == ''){
            $(".usernameinfo").show(200);
            return ;
        }else if(password == ''){
            $(".pwdinfo").show(200);
            return ;
        }else if(modifi == ''){
            $(".modiinfo").show(200);
            return ;
        }

        $.ajax({
            url         :   "../php/login.php",
            datatype    :   "json",
            // async       :   true,           //异步
            data        : {
                'number'    : username,
                'pwd'       : password,
                'captchaCode':modifi          //验证码
            }, success:function(data) {
                console.log(data);
                if(data.error == 1){
                    $.session.set('usernumber', data.adminName);    //用户账号
                    $.session.set('username', data.adminName);      //用户姓名
                    $.session.set('isLogin', "true");               //是否登陆
                    //$.session.clear();
                    //$.session.get('username');
                    //$.session.remove('username');
                    window.location.href="../../adminindex/html/index.html";

                }else if(data.error == 0){
                    $("#codeimage").attr('src','../php/vdimgck.php?type=getValidate&' + Math.random());     //重新获取验证码
                    $(".pwderror").show(200);
                }else if(data.error == 2){
                    $("#codeimage").attr('src','../php/vdimgck.php?type=getValidate&' + Math.random());     //重新获取验证码
                    $(".modifierror").show(200);
                }
            }, error:function(e){
                console.log(e);
            }
        });
    });

     // 设置弹出框
    function tipTogle(str){
        $(".popOperTip").remove();
        $("body").append('<div class="popOperTip">'+str+'</div>');
        $(".popOperTip").fadeIn(1000);
        setTimeout('$(".popOperTip").fadeOut(1000)',1500);
    }

});
*/