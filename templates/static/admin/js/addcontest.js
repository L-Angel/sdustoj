$(function(){
	$.ajaxSetup({
  beforeSend: function(xhr, settings){
      var csrftoken = $.cookie('csrftoken');
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});

	// 全局变量
	var globalvar = {
		title:"",
		start_time:"",
		end_time:"",
		defunct:"",
		points:"",
		contest_private:"",
		langmask:"",
		contest_mode:""
	};
	
	// 时间设置
	jQuery('#startTime,#endTime').datetimepicker({
		timeFormat: "HH:mm:ss",
		dateFormat: "yy-mm-dd"
	});
	
	// 提交题目
	$("#submit").bind("click",function(){

		var title = $("#title").val(); 
		var startTime = $("#startTime").val();
		var endTime = $("#endTime").val();
		var contest_private = $("#selectPublic").val(); 
		var language = $("#selectLanguage").val();
		var problems = $("#problemstxarea").val();
		var users = $("#userstxarea").val();		
		 
		console.log(title); console.log(startTime);
		console.log(endTime); console.log(contest_private); console.log(language);
		console.log(users); console.log(problems); 
		
		if (title == '' || startTime == '' || endTime == '' || problems == '' || users == '' ) {
			alert("title、startTime、endTime、contest_private、language、problems、users不允许为空");
			return false; 
		}
		
		$.post('addcontest_save',
			{title:title,starttime:startTime,endtime:endTime,contest_private:contest_private,language:language,problems:problems,users:users },
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
	
	// 设置弹出框
    function tipTogle(str){
        $(".popOperTip").remove();
        $("body").append('<div class="popOperTip">'+str+'</div>');
        $(".popOperTip").fadeIn(1000);
        setTimeout('$(".popOperTip").fadeOut(1000)',1500);
    }
	   function alert_success(){
         var txt=  "比赛添加成功！";
					window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.success);
       }
        function alert_warning(){
         var txt=  "比赛添加失败！";
					window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.warning);
       }
});