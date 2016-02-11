$(function () {
    // 全局变量
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            var csrftoken = $.cookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    $("body").delegate("#delete","click",function () {

        $c_id = $(this).parent().parent().parent().children().eq(0).text();
        $result = confirm("是否删除本场比赛!");
        if ($result == true) {


            $.post("/admin/dealdata", {
                type: 'contest',
                c_id: $c_id
            }, function (data, textStatus) {
                console.log(textStatus);
                console.warn(data);
                data= $.parseJSON(data);
                if (data.result == "success") {
                    alert_success();
                    window.location.href=window.location.href;
                }
                else {
                    alert_warning();
                    window.location.href=window.location.href;
                }
            })
        }
    })
    function alert_success() {
    var txt = "操作成功！";
    window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
}
function alert_warning() {
    var txt = "操作失败!";
    window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
}
});
