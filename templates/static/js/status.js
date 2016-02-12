/**
 * Created by Rick on 2015/12/2.
 */
$(function(){
    $.ajaxSetup({
  beforeSend: function(xhr, settings){
      var csrftoken = $.cookie('csrftoken');
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});


    $("tr").click(function(){
        $uname= $.cookie("uname");
        $power= $.cookie("power");
        $csrftoken = $.cookie('csrftoken');
        $recode=$(this).children();
        $user_id=$recode.eq(1).text();
        $sol_id=$recode.eq(0).text();
        $problem=$recode.eq(2).text();
        $result=$recode.eq(3).text();
        $mem=$recode.eq(4).text();
        $time=$recode.eq(5).text();
        $codelen=$recode.eq(7).text();
        $subtime=$recode.eq(8).text();
        $language=$recode.eq(6).text();
        $info="<p><div class=\"info\">/*" +
            "<p>Solution_id : " +$sol_id+
            "<p>User_id : " +$user_id+
            "<p>Problem : " +$problem+
            "<p>Language : " +$language+
            "<p>Result : " +$result+
            "<p>Memory : " +$mem+
            "<p>Time : " +$time+
            "<p>Code_Length : " +$codelen+
            "<p>Submit_Time : " +$subtime+
            "<p>*/</div>div>"
        if($uname==$user_id||$power=='A'||$power=='B'){
            $.post("getcodeinfo",
                {s_id:$sol_id},
                function(data,textStatus){
                    data=$.parseJSON(data);
                    console.log(data.source);
                    $("#bpopup").html("");
                    data.source=data.source.replace('\n',"\\n");
                    $("#bpopup").append("<pre><code class=\""+$language.toLowerCase()+"\">"+data.source+"</code></pre>"+$info);
                    $("#bpopup").bPopup();
                }
            );

        }



})


});
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}