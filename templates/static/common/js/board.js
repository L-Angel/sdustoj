/**
 * Created by Rick on 16/2/10.
 */
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
        type:0
    },function(data,textStatus){
        console.log(textStatus);
        data= $.parseJSON(data);
        console.warn(data);
        string=""
        for(i=0;i<data.length;i++){
            string+=data[i].content;
        }
        $(".info-content").html(string);
    });
});