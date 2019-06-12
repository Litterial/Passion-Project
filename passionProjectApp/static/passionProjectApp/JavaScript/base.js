var cookie;
function SaveForm(name,value)
{
    console.log(value);
    cookie=document.cookie=name+ "=" +encodeURIComponent(value+';')+ "; domain="+window.location.hostname+"; path=/";
    console.log(cookie);

}
function deleteCookie()
{
    cookie = document.cookie = "message= ; expires = Thu, 01 Jan 1970 00:00:00 GMT; domain="+window.location.hostname+"; path=/";
    console.log(cookie);
}



function putCookie(e)
{
    message=tinyMCE.activeEditor.getContent();
    console.log(tinyMCE.activeEditor.getContent());
    console.log("I hope this works");
    SaveForm('message',message);
}




