$(function(){

$.ajaxSetup({
  beforeSend: function(xhr, settings){
      var csrftoken = $.cookie('csrftoken');
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});

	// 提交题目
	$("#submit").bind("click",function(){

		var release = $("#selectRelease").val();
		var type = $("#selectType").val();
		var content = $("#newstxarea").val();


		$.post('addnews_save',
			{
				release:release,
				type:type,
				content:content
			},
			function(data,textStatus){
				console.log(data);
				 if(data=="success"){
                    alert_success();
                }
                else{
                    alert_warning();
                }
			}

		);
	});


	   function alert_success(){
         var txt=  "news添加成功！";
					window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
       }
        function alert_warning(){
         var txt=  "news添加失败！";
					window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
       }
});