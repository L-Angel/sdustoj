//获取url信息
 function GetQueryString(name) { 
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i"); 
    var r = window.location.search.substr(1).match(reg); 
    if (r != null) return unescape(r[2]); return null; 
} 
$(function(){
    // 检测是否登陆
    //if($.session.get('isLogin') != 'true'){
    //    window.location='../../login/html/login.html';
    //}
    // 退出登陆
    $("#lagoutId").bind("click",function(){
        $.session.remove('username');
        $.session.remove('isLogin');
        $.session.clear();
        window.location='/admin/login';
    });

    //用户设置选项
    $(".useraction").bind("click",function(){
        var $menu = $(this).parent().children(".usermenu");
        var $upmenu = $(this).children("i");
        if($menu.is(":visible")){
            $menu.slideUp();
            $upmenu.removeClass("upmenu");
        }else {
            $menu.slideDown();
            $upmenu.addClass("upmenu");
        }
    });
    //左侧菜单点击事件
    $("body").delegate(".navlist li","click",function(){
        var $submenu = $(this).children(".submenu");
        
        if ($submenu.length != 0) {
            if ($submenu.is(":visible")) {
                $submenu.slideUp();
            } else {
                $submenu.slideDown();
            }
            return false;            // 阻止事件冒泡和事件默认属性
        }
        else {
            var url = $(this).children("a").attr("href");
            var submenuname =  escape($(this).children("a").text());             //当前菜单名称
            // var menuname =  escape("修改密码");             //当前菜单名称
            var menuname = escape($(this).parent().parent().children("a").text());//父菜单名称
            // var submenuname = escape("系统设置");//父菜单名称
            window.location=url+'? menuName='+menuname+'&submenuName='+submenuname;
            return false;   //event.stopPropagation();      //  阻止事件冒泡
        }
    });

    // 设置左侧菜单信息
    var menuName = GetQueryString("menuName");
    var submenuName = GetQueryString("submenuName"); 
    $("li.menuli a").each(function(i,item){
        if($(this).text() === menuName){
            $(this).siblings(".submenu").show();
           
            // 三级菜单显示Hack方法
            $(this).parent().parent().show();
        }else if($(this).text() === submenuName){
            $(this).parent().addClass("active");
        }
    }); 

});
