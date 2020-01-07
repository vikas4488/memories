


 $(document).ready(function(){

 var crlan="en";

 if ( typeof savelan !== 'undefined' && (savelan == 'en'||savelan == 'hi') ) {
   crlan=savelan;
 }


 $('#showreg').on('click', function(){
     $(this).animate({ left:'10%',width: '58%'}, 500);
     $('#showlogin').animate({left:'70%', width: '20%' }, 500);
         $('#loginsec').slideUp(400);
         $('#regformpop').slideDown(400);
     });
 $('#showlogin').on('click', function(){
     $(this).animate({left:'10%',width: '58%'}, 500);
     $('#showreg').animate({left:'70%', width: '20%' }, 500);
         $('#loginsec').slideDown(400);
         $('#regformpop').slideUp(400);
     });
 $('#profilepage').on('click', function(){
        window.location.href = userprofile;
     });
 $('#dataentrypage,.enter_records').on('click', function(){
        window.location.href = dataentry;
     });
 $('#viewrecords,.view_records').on('click', function(){
        window.location.href = viewrecords;
     });
 $('#contactadmin').on('click', function(){
        window.location.href = contactadmin;
     });
 $('#verifyuser').on('click', function(){
     var webl="https://themysterio.000webhostapp.com";
     var wmsg= lan[crlan]["share_msg"];

     var wtslink="https://wa.me/?text="+wmsg+" "+webl;
        window.location = wtslink;

       // window.location.href = "verifyuser.php";
     });
 $('#logout').on('click', function(){
        window.location.href = logout;
     });
 $('#help').on('click', function(){
        window.location.href = help;
     });
 $('#aboutit').on('click', function(){
        window.location.href = about;
     });
 $('#themepage').on('click', function(){
        window.location.href = theme;
     });

 var tcolor="";
 var tcolor2="";
 $('.editbtn,.editrecbtn').on('click', function(){
     if($(this).parent().find('.dataedit,.recordedit,.recordeditdiv').prop('readonly')==true){
       tcolor=  $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').css("background-color");
       tcolor2=  $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').css("color");
       $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').css({"background-color":"white"});
       $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').css({"color":"black"});
       $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').prop('readonly', false);
       $(this).text(lan[crlan]["cancle_edit"]);
       $(this).parent().find('.updatebtn,.updatebtn2').animate({ marginLeft: '15%' , opacity: 1 }, 500);
       $(this).parent().find('.updatebtn,.updatebtn2').css("display","inline-block");

       $(this).parent().find('.dataedit,.recordedit').css({"border-bottom":"1px solid gray"});
       $(this).parent().find('.recordeditdiv').css({"border":"1px solid gray"});
     }
     else{

         $(this).parent().find("input:not(:first),textarea").each(function(e){

         $(this).val($(this).parent().find(".tempData").text());
         });


          $(this).parent().find('.dataedit,.recordedit').css({"border-bottom":"0"});
       $(this).parent().find('.recordeditdiv').css({"border":"0"});
         $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').css({"background-color":tcolor});
           $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').css({"color":tcolor2});
       $(this).parent().find('.dataedit,.recordedit,.recordeditdiv').prop('readonly', true);
       $(this).text(lan[crlan]["edit_details"]);
       $(this).parent().find('.updatebtn,.updatebtn2').animate({ marginLeft: '-24%' , opacity: 0 ,display:'none'}, 500);
     }
     });
 $('.closeconfirm').on('click', function(){
       $('.popwrap').hide();
     });
 $('.homebtn').on('click', function(){
        window.location.href = navigation;
     });
     //for records show and hide
    $(".viewmore").click(function(){
     $(".viewmore").text(lan[crlan]["show_details"]);
     $(".formwrap").slideUp(400);
     if($(this).parent().parent().find(".formwrap").is(":visible")){
     $(this).parent().find(".viewmore").text(lan[crlan]["show_details"]);
     $(this).parent().find(".formwrap").slideUp(400);

     if($(this).parent().parent().find(".updatebtn").css("opacity")==1)
     $(this).parent().parent().find(".editrecbtn").click();

     }
     else{
     $(this).parent().find(".viewmore").text(lan[crlan]["hide_details"]);
     $(this).parent().parent().find(".formwrap").slideDown(400);
     }
   });

   //for help show and hide
    $(".viewmore_help").click(function(){
     $(".formwrap").slideUp(400);
     if($(this).parent().find(".formwrap").is(":visible")){
     $(this).parent().find(".formwrap").slideUp(400);

     }
     else{
     $(this).parent().find(".formwrap").slideDown(400);
     }
   });


  $(function () {
         $('.updatebtn').on('click', function (e) {
              $(".popwrap").show();
               $(".closeconfirm").hide();
           $.ajax({
             type: 'post',
             url: updaterecords,
             dataType: 'text',
             data: $(this).parent().serialize(),
             success: function (response) {
                 var status = response;

                $(".closeconfirm").show();
                 $(".ajaxmsg").text(status);
                 $('.dataedit,.recordedit,.recordeditdiv').css({"background-color":tcolor});
                 $('.dataedit,.recordedit,.recordeditdiv').css({"color":tcolor2});
                 $('.recordedit,.recordeditdiv').prop('readonly', true);
                     $('.editrecbtn').text(lan[crlan]["edit_details"]);
                         $('.updatebtn').animate({ marginLeft: '-24%' , opacity: 0 ,display:'none'}, 500);

             }
           });

         });

       });


 $(function () {
         $('.updateuserdata').on('click', function (e) {
              $(".popwrap").show();
               $(".closeconfirm").hide();
           $.ajax({
             type: 'post',
             url: 'updateuserdata.php',
             dataType: 'text',
             data: $(this).parent().serialize(),
             success: function (response) {

                 var pFrom = response.indexOf("startstatus ") + "startstatus ".length;
                 var pTo = response.lastIndexOf(" endstatus");

                 var status = response.substring(pFrom,pTo);

                $(".closeconfirm").show();
                 $(".ajaxmsg").text(status);
                 $('.dataedit,.recordedit,.recordeditdiv').css({"background-color":tcolor});
                 $('.dataedit,.recordedit,.recordeditdiv').css({"color":tcolor2});
                 $('.recordedit,.recordeditdiv').prop('readonly', true);
                     $('.editrecbtn').text(lan[crlan]["edit_details"]);
                         $('.updatebtn').animate({ marginLeft: '-24%' , opacity: 0 ,display:'none'}, 500);

             }
           });

         });

       });



 $('.openuserpage').on('click', function () {
     $(this).parent().attr('action', 'openuserpage.php');
      $(this).parent().attr('target', '_blank');
       $(this).parent().attr('method', 'post');
   $(this).parent().submit();
   return false;
 });

   $('.lans').on('click', function () {

                 var tem=crlan;
                if(tem=="en")
                {
                    $(this).text("english");
                    crlan="hi";
                }
                else if(tem=="hi")
                {
                    $(this).text("हिंदी");
                    crlan="en";
                }
              changeLanguageNow(crlan);
              $.ajax({
             url: 'changelan.php',
             type: 'post',
             success: function (response) {
                 //alert(response);
             }
              });
         });


 $('#loginbutton,#regbutton').on('click', function () {
    var flag=true;
     var msg="";
     var pass1="";
     var pass2="";
     var cnfmsg="<div style='color: green;'>please confirm below details</div><br>";
     $(this).parent().find("input").each(function(){

         if($(this).attr('type')=="radio"){
             if ($(this).is(":checked")) {
                 cnfmsg=cnfmsg+"<div>"+$(this).parent().children("span").text()+" : ";
           cnfmsg=cnfmsg+ $(this).val()+"</div><br>";
         }

         }
         else if($(this).attr('type')!="password"){
         cnfmsg=cnfmsg+"<div>"+$(this).parent().children("span").text()+" : ";
           cnfmsg=cnfmsg+ $(this).val()+"</div><br>";
         }

        if($(this).val().trim()==""){
            flag=false;
            //msg="fields can't be empty";
            msg=lan[crlan]["field_not_empty"];
            return false;
        }else if($(this).attr('type')=="number"&&($(this).val().length<10||$(this).val().length>10)){
                flag=false;
               // msg="number should be 10 digit";
                msg=lan[crlan]["number_length"];
                return false;
        }else if($(this).attr('type')=="password"&&$(this).val().length<4){
             //msg="password should atleast 6 digit";
             msg=lan[crlan]["pass_length"];

                flag=false;
                return false;
        }
        if($(this).attr('type')=="password"){
         if(pass1=="")
             pass1=$(this).val();
             else
             pass2=$(this).val();
        }
     });
     if($(this).attr('id')=="regbutton"&&pass1!=pass2){
         msg=lan[crlan]["pass_missmatch"];
         flag=false;
     }

        if(!flag){
             $(".uipop").show();
             $(".uipopmsg").text(msg);
        }else{
            if($(this).attr("id")=="regbutton"){
            $(".formpop").show();
            $(".cancle_btn").show();
             $(".formmsg").html(cnfmsg);
            }else{
            $(this).parent().submit();
            $(".popwraplogin").show();
            }
        }

 });
 $('.submitForm').on('click', function () {

     $("#regformpop").submit();
     $(".popwraplogin").show();

 });

 $(".lan").each(function(){
 var he=$(this).attr("class").split(/\s+/);

      var attr = $(this).attr('data-placeholder');
 if (typeof attr !== typeof undefined && attr !== false) {
     $(this).attr("data-placeholder",lan[crlan][he[1]]);
 }else{
  $(this).text(lan[crlan][he[1]]);
 }
 });
 function changeLanguageNow(crlan){
     $(".lan").each(function(){
 var he=$(this).attr("class").split(/\s+/);

      var attr = $(this).attr('data-placeholder');
 if (typeof attr !== typeof undefined && attr !== false) {
     $(this).attr("data-placeholder",lan[crlan][he[1]]);
 }else{
  $(this).text(lan[crlan][he[1]]);
 }
 });
 }

 $('.whatsappwrap').on('click', function () {
     var wtstext="";
     $(this).parent().find("input:not(:first),textarea").each(function(e){
         wtstext = wtstext +$(this).parent().find(".lan").text()+" : ";

         wtstext = wtstext + $(this).parent().find(".tempData").text()+".||\n ";
         });
        // alert(wtstext);
        var wtslink="https://wa.me/?text="+wtstext;
        window.location = wtslink;
 });

 $('.searchbtn').on('click', function () {
     var flag=false;
     var date1="";
     var date2="";
     var msg="pelase enter some valid data";
     $(this).parent().find("input").each(function(e){
         if($(this).attr('name')=="date1")
                 date1=$(this).val();
         else if($(this).attr('name')=="date2")
                 date2=$(this).val();
         else if($(this).val()!="")
         {
             flag=true;
             return false;
         }
     });

     if((date1!=""&&date2!=""))
         flag=true;
     else if((date1!=""&&date2=="")||(date2!=""&&date1==""))
         var msg="pelase provide both the dates";

     if(flag)
     $(this).parent().submit();
     else{
         $('.popwrap').show();
         $('.ajaxmsg').text(msg);
     }

 });

 $('.search-nav').on('click', function () {
     $(".search-nav").css("box-shadow","");
     $(".search-nav").css("border-radius","");
     $(this).css("box-shadow","0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.12), 0 1px 5px 0 rgba(0,0,0,0.2)");
     var crid=$(this).attr('id');
     var cridd=crid+"-div";

     $('.search-nav-div').hide("linear");
     $('.search-nav-div').parent().find(".searchbtn").hide("linear");
     $('#'+cridd).show("linear");
     $('#'+cridd).parent().find(".searchbtn").show("linear");
     //$('.search-wrap').find("input").val("");

 });

   $(".opentheme").click(function(){
     $(this).parent().parent().parent().find(".popcard").show(200).animate({ width: '90%' ,left : '5px' ,top : '5px',display : 'block'}, 400);

   });


    $(".createtheme").click(function(){
     $(this).parent().find(".popcard").show(200).animate({ width: '90%' ,left : '5px' ,top : '5px',display : 'block'}, 400);

   });

   $(".thcancle").click(function(){
     $(this).parent().parent().parent().find(".popcard").hide(200);

   });

   $(".settheme").click(function(){
     $(this).parent().submit();

   });
     $(".thdelete").on('click', function () {
         var tid=$(this).parent().find('input[name ="themeid"]').val();
         var tname=$(this).parent().find('input[name ="themename"]').val();
     $("#themedelete").find('input[name ="tid"]').val(tid);
     $(".formpop").show();
     $(".formmsg").text("delete "+tname +" ?");
   });
     $(".dlform").click(function(){
         $("#themedelete").submit();
     });

   });

   $(function () {
    $('.sendmsg').on('click', function (e) {
        var objDiv = document.getElementById("msg_wrap_id");
        objDiv.scrollTop = objDiv.scrollHeight;
        msg=$(".feedback").text();
        $(".hiddenmsg").val(msg);
        $(".feedback").text('');
        $(".msg_wrap").append('<div class="send_div"><div class="send_msg"><div class="chat-pop-right">'+msg+'</div></div></div><div class="tick jssent">⸮</div><br>')    
        var objDiv = document.getElementById("msg_wrap_id");
        objDiv.scrollTop = objDiv.scrollHeight;
        $.ajax({
        type: 'post',
        url: sendmsg,
        dataType: 'text',
        data: $(this).parent().serialize(),
        success: function (response) {
            var status = response;
            $(".jssent").html("✓");
            $(".jssent").removeClass("jssent");
        }
      });

    });

  });
  var objDiv = document.getElementById("msg_wrap_id");
        objDiv.scrollTop = objDiv.scrollHeight;