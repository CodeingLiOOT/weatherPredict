function logIn(){
    var name = document.getElementById("userId").value;
    var password = document.getElementById("userPassword").value;
    if(name==""||password==""){
        alert("用户名或密码不能为空");
    }else{
        var xmlhttp = new XMLHttpRequest();
    //alert("creat xmlrequest")
        xmlhttp.open("get","check?id="+name+"&pw="+password,true);
        xmlhttp.onreadystatechange=function(){

            if(xmlhttp.readyState==4&&xmlhttp.status==200){
                //alert("statuc changed success");
                var txt =xmlhttp.responseText;
                if (txt == "manager"){
                    window.location='/weather/'
                    //发送请求跳转到weather
                }else if(txt=="normal"){
                    window.location='/low_weather/'
                }
                else{
                    alert("用户名或密码错误！");
                    document.getElementById("userId").value="";
                    document.getElementById("userPassword").value="";
                    //alert(txt);
                }
            }


        }

        xmlhttp.send(null);
        //alert("send success");
    }

}