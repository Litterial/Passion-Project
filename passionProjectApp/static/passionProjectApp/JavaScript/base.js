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




function updateText(count,newcount)
{
    console.log('updateText');
    count.text(newcount);
    console.log(newcount)
}



$(".Q-upvote-link ").click(function (e) {
    console.log('test');
    e.preventDefault();
    console.log('preventDefault works');
    var dataUrl = $(this).attr('data-href');
    var questionID="question"+($(this).attr("data-upvote"));
    console.log(questionID);
    $.ajax({
            url: dataUrl,
            method: "GET",
            data: {},
            success: function (data) {
                console.log(data);
                var newLikes;
                if(data.upvote){
                    newLikes=data.voteTotal;
                    console.log('upvote');
                    console.log(newLikes);
                    updateText(questionID,newLikes);

                }
                else{
                    newLikes=data.voteTotal;
                    updateText(questionID,newLikes);
                }

            },
            error: function (fail) {
                console.log('fail');
                console.log(fail)
            }
        }
    )
});

$(".Q-downvote-link ").click(function (e) {
    console.log('test');
    e.preventDefault();
    console.log('preventDefault works');
    var dataUrl = $(this).attr('data-href');
    var questionID="question"+($(this).attr("data-downvote"));
    console.log(questionID);
    $.ajax({
            url: dataUrl,
            method: "GET",
            data: {},
            success: function (data) {
                console.log(data);
                var newLikes;
                if(data.downvote){
                    newLikes=data.voteTotal;
                    console.log('upvote');
                    console.log(newLikes);
                    updateText(questionID,newLikes);

                }
                else{
                    newLikes=data.voteTotal;
                    updateText(questionID,newLikes);
                }

            },
            error: function (fail) {
                console.log('fail');
                console.log(fail)
            }
        }
    )
});