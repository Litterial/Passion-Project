
function SaveForm(name,value)
{
    var cookie=document.cookie=name+ "=" +(value);
    console.log(cookie);
    cookie = document.cookie = "message= ; expires = Thu, 01 Jan 1970 00:00:00 GMT";
    console.log(cookie);
}
//
// othertest[0].addEventListener('input',updatevalue);
// console.log('hi');
// console.log(othertest);


function putCookie(e)
{
    message=tinyMCE.activeEditor.getContent();
    console.log(tinyMCE.activeEditor.getContent());
    console.log("I hope this works");
    SaveForm('message',message);
}


function test()
{
    console.log('test');

}