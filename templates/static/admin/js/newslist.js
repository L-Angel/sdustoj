$(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            var csrftoken = $.cookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });


    $("body").delegate("#operate","click", function () {

        $news_id = $(this).parent().parent().parent().children().eq(0).text();
        $release = 0
        $result = confirm("是否发布本条信息!");
        if ($result == true) {
            $release = 1
        } else if ($result == false) {
            $release = 0
        }
        $.post("/admin/dealnews", {
            news_id: $news_id,
            release: $release,
            op: 'release'
        }, function (data, textStatus) {
            if (data == "success") {
                alert_success()
            }
            else {
                alert_warning()
            }
            window.location.href=window.location.href;

        })
    })

    $("#delete").bind("click", function () {

        $news_id = $(this).parent().parent().parent().children().eq(0).text();
        $result = confirm("是否删除本条消息!");
        if ($result == true) {


            $.post("/admin/dealnews", {
                news_id: $news_id,
                op: 'del'
            }, function (data, textStatus) {
                if (data == "success") {
                    alert_success();
                }
                else {
                    alert_warning();
                                        window.location.href=window.location.href;

                }
            })
        }

    })
});
function alert_success() {
    var txt = "操作成功！";
    window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
}
function alert_warning() {
    var txt = "操作失败!";
    window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
}