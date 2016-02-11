/**
 * Created by Lonely on 2016/1/19.
 */
   $(function(){
       	$.ajaxSetup({
  beforeSend: function(xhr, settings){
      var csrftoken = $.cookie('csrftoken');
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});
        $("#submit").click(function(){
           $title=$("#title").val();
            $timelimit=$("#timelimit").val();
            $memlimit=$("#memlimit").val();
            $descripe=$("#editorDesc").val();
            $input=$("#editorOutput").val();
            $output=$("#editorInput").val();
            $sampleinput=$("#editorSampleOutput").val();
            $sampleoutput=$("#editorSampleInput").val();
            $hint=$("#editorHint").val();
            $.post("/admin/addproblem_save",{
                title:$title,
                timelimit:$timelimit,
                memlimit:$memlimit,
                descripe:$descripe,
                input:$input,
                output:$output,
                sampleinput:$sampleinput,
                sampleoutput:$sampleoutput,
                hint:$hint
            },function(data,textStatus){
                if(data=="success"){
                    alert_success();
                }
                else{
                    alert_warning();
                }
            })



     });
       function alert_success(){
         var txt=  "题目添加成功！";
					window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
       }
        function alert_warning(){
         var txt=  "题目添加失败！";
					window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
       }
   });

