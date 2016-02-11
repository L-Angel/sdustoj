/**
 * Created by Rick on 16/2/10.
 */
$(function(){
    $.ajaxSetup({
  beforeSend: function(xhr, settings){
      var csrftoken = $.cookie('csrftoken');
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});

    $.post("getnewsinfo",{
        type:1
    },function(data,textStatus){
        console.log(textStatus);
        data= $.parseJSON(data);
        console.warn(data);
        string=""
        for(i=0;i<data.length;i++){
            string+=data[i].content;
        }
        console.log(string);
        var $notice="<marquee scrollamount=3 ><FONT style=\"FONT-SIZE: 20pt; FILTER: dropshadow(color=#228B22,offX=5,offY=3,Positive=1); WIDTH: 100%; COLOR: #880000; LINE-HEIGHT: 150%; FONT-FAMILY:'Adobe Ming Std';\"><B>"+string+"</B></FONT></marquee>"
   $(".toptitle").parent().remove('marquee')
    $(".toptitle").parent().append($notice)
    });
});