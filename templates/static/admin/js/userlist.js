$(function () {
    var globalvar = {
        password: null,
        repeatpwd: null,
        dataid: null,
        datadefunct: null,
        curNode: null,
        username:null,
        uanme:null,
    };
    globalvar.username = $.cookie("uname")
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            var csrftoken = $.cookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            if (!$("body").hasClass('waithidemode')) {
                var str = '<div class="waithidemode" style="position:fixed;top:0;left:0;height: 100%; width: 100%;z-index: 2001;">';
                str += '<img src="../static/admin/common/img/loading.gif" alt="" style="position:fixed;margin:auto;left:0; right:0; top:0;bottom:0;z-index: 2002;"></div>';
                $("body").append(str);
            }
        },
        complete: function () {
            $(".waithidemode").remove();
        },
        error: function (e) {
            console.log(data);
        }
    });


    $("body").delegate("#delete", "click", function () {

        $u_id = $(this).parent().parent().parent().children().eq(0).text();
        $result = confirm("是否删除本用户信息!");
        if ($result == true) {


            $.post("/admin/dealdata", {
                type: 'user',
                u_id: $u_id
            }, function (data, textStatus) {
                data = $.parseJSON(data);
                if (data.result == "success") {
                    alert_success();
                    window.location.href = window.location.href;
                }
                else {
                    alert_warning();
                    window.location.href = window.location.href;

                }
            })
        }
    })
    // 设置弹出框
    $("body").delegate("#edit", "click", function () {
        // 重置数据

       // globalvar.datadefunct = $(this).parent().attr("data-defunct");
        //globalvar.dataid = $(this).parent().attr("data-id");
        globalvar.curNode = $(this).parent().parent().parent();
        $user_id=globalvar.curNode.children().eq(0).text()
        // root用户不显示调权限
         globalvar.uname=$user_id;
        if ($user_id == 'admin' || globalvar.defunct == 'B') {
            $("#privilegelabel").hide();
            globalvar.datadefunct='Z';
        } else {
            $("#privilegelabel").show();
        }

        $(".popucontainer").show();

        $("#privilege").val(globalvar.datadefunct);
    });

    // 确定弹出窗设置
    $("#updataOk").bind("click", function () {
        globalvar.password = $("#pwd").val();
        globalvar.repeatpwd = $("#confirmpwd").val();
        globalvar.datadefunct = $("#privilege").val();
        console.log(globalvar.uname);
        if(isSpace(globalvar.uname)){
           globalvar.uname="null";
        }
        else if (globalvar.password != globalvar.repeatpwd) {
            tipTogle("密码不一致");
            return false;
        }

         $.post("/admin/dealuser",
         {uname:globalvar.uname,power:globalvar.datadefunct,pwd:globalvar.password},
         function(data) {
             data= $.parseJSON(data);
         console.log(data);
         if(data.result == "success"){
         tipTogle("操作成功");
         $(".closealert").triggerHandler("click");
             setTimeout("",1000);
             window.location.href=window.location.href;
         }else{
         tipTogle("操作失败");
         }


         });

    });

    // 取消弹出框
    $(".closealert").bind("click", function () {
        // 重置数据
        $("#confirmpwd").val('');
        $("#pwd").val('');
        $(".popucontainer").hide();
    });

// 设置弹出框
    function tipTogle(str){
        $(".popOperTip").remove();
        $("body").append('<div class="popOperTip">'+str+'</div>');
        $(".popOperTip").fadeIn(1000);
        setTimeout('$(".popOperTip").fadeOut(1000)',1500);
    }
    function alert_success() {
        var txt = "操作成功！";
        window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
    }

    function alert_warning() {
        var txt = "操作失败!";
        window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
    }
    function isSpace(data) {
        if (data == null || data == "null") { true;
        }
        return false;
    }
});