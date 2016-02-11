$(function(){
	// 全局变量
	var globalvar = {
		ueSource:"",
		ueDesc:"",
		ueInput:"",
		ueOutput:"",
		ueSampleInput:"",
		ueSampleOutput:"",
		ueHint:"",
		ueAppendcode:"",
		problem_id:12345,			// 问题id
		step:1,						// 当前步骤
		fileallnum:2,				// 上传文件的数量
		fileuploadnum:0				// 已经上传文件数量
	};
	
	// 实例化uedit
	globalvar.ueSource = UE.getEditor('editorSource');	
	globalvar.ueDesc = UE.getEditor('editorDesc');	 
	globalvar.ueInput = UE.getEditor('editorInput');	 
	globalvar.ueOutput = UE.getEditor('editorOutput');	 
	globalvar.ueSampleInput = UE.getEditor('editorSampleInput');	 
	globalvar.ueSampleOutput = UE.getEditor('editorSampleOutput');	 
	globalvar.ueHint = UE.getEditor('editorHint');	 
	globalvar.ueAppendcode = UE.getEditor('editorAppendcode');	 
	/*
	$(".addproblem").hide();				// 进入第二步
	$(".uploadfile").show();
	$("li[data-target=#step2]").addClass("active");*/
	
	// 提交题目
	$("#submit").bind("click",function(){
	
		if(globalvar.step == 1){													// 第一步
			var title = $("#title").val(); var time_limit = $("#time_limit").val();
			var memory_limit = $("#memory_limit").val();
			var spj = $("input[name=spj]:checked").val(); 
			var available = $("input[name=available]:checked").val();
			
			// ue.getContent(); //带格式的文章内容 //ue.getContentTxt(); //纯文本的文章内容
			
			var description = globalvar.ueDesc.getContent(); 
			var input = globalvar.ueInput.getContent(); 
			var output = globalvar.ueOutput.getContent(); 
			var sample_input = globalvar.ueSampleInput.getContent(); 
			var sample_output = globalvar.ueSampleOutput.getContent(); 
			var hint = globalvar.ueHint.getContentTxt(); 
			var append_code = globalvar.ueAppendcode.getContentTxt(); 
			var source = globalvar.ueSource.getContentTxt();
			
			console.log(title); console.log(time_limit);
			console.log(memory_limit); console.log(spj); console.log(source);
			console.log(description); console.log(input); console.log(output);
			console.log(sample_input); console.log(sample_output);
			console.log(hint); console.log(append_code);
			
			if (title == '' || description == '' || input == '' || output ==
			'' || time_limit == 0 || memory_limit == '' || spj == '' ) {
				alert("title、description、input、output、time_limit、memory_limit不允许为空");
				return false; 
			}
			
			$.ajax({url:'problem/addProblem.action',datatype:"json",type:"POST",
				data:{title:title,time_limit:time_limit,memory_limit:memory_limit,spj:spj,source:source,description:description,
				input:input,output:output,sample_input:sample_input,sample_output:sample_output,hint:hint },
				success:function(data){ 
					if(data.errorcode == 1){
						globalvar.problem_id = data.problem_id;
						
						$(".addproblem").hide();				// 进入第二步
						$(".uploadfile").show();
						$("li[data-target=#step2]").addClass("active");
						globalvar.step++;						// 第二
						
						//alert("发布成功");
					}else{ 
						alert("添加题目失败"); 
					} 
				},
				beforeSend:function(){
					if(!$("body").hasClass('waithidemode')){ var str = '<div class="waithidemode" style="position:fixed;top:0;left:0;height: 100%; width: 100%;z-index: 2001;">'; str += '<img src="admin/common/img/loading.gif" alt="" style="position:fixed;margin:auto;left:0; right:0; top:0;bottom:0;z-index: 2002;"></div>'; $("body").append(str); } 
				},
				complete:function(){ 
					$(".waithidemode").remove(); 
				},
				error:function(e){ console.log(data); } 
			});
		}else if(globalvar.step == 2){
			
			// 遍历上传测试文件
			$.each($("input[name='file']"),function(i,item){
				globalvar.fileallnum = i+1;		// 测试文件总数		
				
				var filepath = $(this).val();
				var filename = $(this).attr("data-name");
				
				if(checkFiletype( filepath )==false){
		            alert("请上传txt文件");
		            return false;
		        }
		        
		        // 创建FormData对象,为FormData对象添加数据
		        var fd = new FormData();
		        fd.append("filename", filename);
		        fd.append("fileDirname", globalvar.problem_id);		// 文件夹名称按照id命名
		        $.each(this.files, function(i, file) {
		            fd.append('file', file);
		        });  
		        
		        $(this).hide();										// 隐藏input框
		        var str = '<div class="progressTop'+i+' progressTop"><div class="progress"><div class="bar" style="width:100%;"></div></div></div>';
                	str += '<i class="progressinfo'+i+' progressinfo"></i>';
		        $(this).parent().append(str);
		        

		        // 创建XMLHttpRequest对象,发送数据
		    	var xhr = new XMLHttpRequest();
		    	xhr.upload.addEventListener("progress", function(evt){
		    		uploadProgress(evt);
		    	}, false);
		    	xhr.open("POST", "problem/uploadFile.action");
		    	xhr.send(fd);
		    	
		    	// 上传进度处理
		    	function uploadProgress(evt){
		    	    var percentComplete = Math.round(evt.loaded * 100 / evt.total);
		    	    
		    	    var loaded = (evt.loaded/(1024)).toFixed(2);			// 转化为KB
		    	    var total = (evt.total/(1024)).toFixed(2);				// 转化为KB
		    	    
		    	    $(".progressTop"+i+" .progress .bar").css("width",percentComplete+'%');       	// 进度条
		    	    $(".progressinfo"+i).html(percentComplete+'%'+" "+loaded+"KB/"+total+"KB");  	// 提示条

		    	}
		        
		        // 上传文件完成处理
		        xhr.onreadystatechange=function(){
		            if(xhr.readyState==4) { 
		                if(xhr.status==200) { 
		                    var data = xhr.responseText;
		                    data = JSON.parse(data);
		                    if(data.errorcode == 1){
		                    	calbackprogre();
		                    }
		                }
		            } 
		        };
			});
		}
		
	 
	});
	
	function calbackprogre(){
		globalvar.fileuploadnum++;
		if(globalvar.fileuploadnum == globalvar.fileallnum){
			alert("上传成功");
			 				
			//$(".uploadfile").hide();					// 进入第三步完成
			$("li[data-target=#step3]").addClass("active");
			globalvar.step++;							// 第三
		}
	}
	
	
	// 上传测试文件
    // $("input[name='file']").on("change",function(){
	function uploadFile(filename,filepath){
    	//var filepath = $(this).val(); 
        if(checkFiletype( filepath )==false){
            alert("请上传txt文件");
            return false;
        }
        
        console.log("上传测试文件");
        
        //$(".progressflag").show();  // 显示进度
        
        // 创建FormData对象,为FormData对象添加数据
        var fd = new FormData();
        fd.append("filename", filename);
        fd.append("fileDirname", globalvar.problem_id);		// 文件夹名称按照id命名
        $.each(this.files, function(i, file) {
            fd.append('file', file);
        });  
        
        // 创建XMLHttpRequest对象,发送数据
    	var xhr = new XMLHttpRequest();
    	xhr.upload.addEventListener("progress", function(evt){
    		uploadProgress(evt);
    	}, false);
    	xhr.open("POST", "problem/uploadFile.action");
    	xhr.send(fd);
    	
    	// 上传进度处理
    	function uploadProgress(evt){
    	    var percentComplete = Math.round(evt.loaded * 100 / evt.total);
    	    
    	    var loaded = (evt.loaded/(1024)).toFixed(2);			// 转化为M
    	    var total = (evt.total/(1024)).toFixed(2);				// 转化为M
    	    
    	    $(".progressTop .progress .bar").css("width",percentComplete+'%');       	// 进度条
    	    $(".progressinfo").html(percentComplete+'%'+" "+loaded+"KB/"+total+"KB");  	// 提示条
    	    
    	    console.log("当前上传:"+evt.loaded+"字节"+" 共:"+evt.total+"已完成："+percentComplete+"%");
    	}
        
        // 上传视频完成处理
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4) { 
                if(xhr.status==200) { 
                    var data = xhr.responseText;    // 以文本方式接收响应信息
                    console.log(data);
 
                }
            } 
        };
    }
    //}); 
    
    function checkFiletype(filepath)  {
	    // var filepath=$("input[name='file']").val();
	    // 获得上传文件名
	    var fileArr=filepath.split("\\");
	    var fileTArr=fileArr[fileArr.length-1].toLowerCase().split(".");
	    var filetype=fileTArr[fileTArr.length-1];
	    // 切割出后缀文件名
	    if(filetype != "txt"){
	        return false;
	    }else{
	        return true;
	    }
	}
	
	// 设置弹出框
    function tipTogle(str){
        $(".popOperTip").remove();
        $("body").append('<div class="popOperTip">'+str+'</div>');
        $(".popOperTip").fadeIn(1000);
        setTimeout('$(".popOperTip").fadeOut(1000)',1500);
    }

});