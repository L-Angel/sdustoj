/**
 * Created by Rick on 16/2/16.
 */

$(function(){

});
 function alert_success(){
         var txt=  "Rejudge成功！";
                    window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
       }
        function alert_warning(){
         var txt=  "Rejudge失败！";
                    window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
       }