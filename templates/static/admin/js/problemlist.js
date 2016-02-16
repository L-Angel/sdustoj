$(function () {
    // 全局变量
    var globalvar = {
        curNode: null,
        problem_id: null,
        describe: null,
        input: null,
        output: null,
        sampleinput: null,
        sampleout: null,
        title: null,
        hint: null,
        appendcode: null

    };
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            var csrftoken = $.cookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });


    $("#body").delegate("#delete", "click", function () {

        $p_id = $(this).parent().parent().parent().children().eq(0).text();
        $result = confirm("是否删除本条题目!");
        if ($result == true) {

        }
        $.post("/admin/dealdata", {
            type: 'problem',
            p_id: $p_id
        }, function (data, textStatus) {
            data = $.parseJSON(data)
            if (data.result == "success") {
                alert_success();
            }
            else {
                alert_warning();
            }
            window.location.href = window.location.href;

        })

    })
    $("body").delegate("#operate", "click", function () {
        // 重置数据

        // globalvar.datadefunct = $(this).parent().attr("data-defunct");
        //globalvar.dataid = $(this).parent().attr("data-id");
        globalvar.curNode = $(this).parent().parent().parent();
        $problem_id = globalvar.curNode.children().eq(0).text()
        // root用户不显示调权限

        globalvar.problem_id = $problem_id;
        $.post('/admin/editproblem', {
            type: 'get',
            p_id: $problem_id
        }, function (data, textStatus) {
            data = $.parseJSON(data)
            $("#ptitle").val(data.title)
            $("#pdescribe").val(data.describe)
            $("#pinput").val(data.input)
            $("#poutput").val(data.output)
            $("#psampleinput").val(data.sampleinput)
            $("#psampleoutput").val(data.sampleoutput)
            $("#phint").val(data.hint)
            $("#pappendcode").val(data.appendcode)

        })
        $(".popucontainer").show();

    });

    // 确定弹出窗设置
    $("#updataOk").bind("click", function () {
        $.post('editproblem', {
            type: 'save',
            p_id: globalvar.problem_id,
            title: $("#ptitle").val(),
            describe: $("#pdescribe").val(),
            input: $("#pinput").val(),
            output: $("#poutput").val(),
            sampleinput: $("#psampleinput").val(),
            sampleoutput: $("#psampleoutput").val(),
            hint: $("#phint").val(),
            appendcode: $("#pappendcode").val()
        }, function (data, textStatus) {
            data = $.parseJSON(data)
            if (data.result == "success") {
                tipTogle("操作成功");
                $(".closealert").triggerHandler("click");
                setTimeout("", 1000);
                window.location.href = window.location.href;
            } else {
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
    function tipTogle(str) {
        $(".popOperTip").remove();
        $("body").append('<div class="popOperTip">' + str + '</div>');
        $(".popOperTip").fadeIn(1000);
        setTimeout('$(".popOperTip").fadeOut(1000)', 1500);
    }

    function isSpace(data) {
        if (data == null || data == "null") {
            true;
        }
        return false;
    }

    function alert_success() {
        var txt = "操作成功！";
        window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
    }

    function alert_warning() {
        var txt = "操作失败!";
        window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
    }
});
