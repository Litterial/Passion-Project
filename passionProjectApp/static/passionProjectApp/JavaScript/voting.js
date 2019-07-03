


function updateText(count,newcount)
{
    console.log('updateText');
    count.innerHTML=newcount;
    console.log(newcount)
}



$(".Q-upvote-link ").click(function (e) {
    console.log('test');
    e.preventDefault();
    console.log('preventDefault works');
    var dataUrl = $(this).attr('data-href');
    var tempID=$(this).attr("data-upvote");
    var ID="#question"+tempID;
    var upID="#upQ"+tempID;
    var downID="#downQ"+ tempID;
    var questionID=document.querySelector(ID);
    var upArrow=document.querySelector(upID);
    var downArrow=document.querySelector(downID);
    console.log(downArrow);
    console.log(questionID);
    $(downArrow).addClass("triangledown").removeClass('triangledownvoted');

    $.ajax({
            url: dataUrl,
            method: "GET",
            data: {},
            success: function (data) {
                console.log(data);
                var newLikes;
                if(data.upvote){
                    console.log(data.upvote);
                    newLikes=data.voteTotal;
                    console.log('upvote');
                    console.log(newLikes);
                    $(upArrow).addClass('triangleupvoted').removeClass('triangleup');
                    updateText(questionID,newLikes);

                }
                else{
                    newLikes=data.voteTotal;
                    console.log(data.upvote);
                    console.log('downvote');
                    console.log(newLikes);
                    $(upArrow).addClass('triangleup').removeClass('triangleupvoted');

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
    var tempID=$(this).attr('data-downvote');
    var ID="#question"+tempID;
    var upID="#upQ"+tempID;
    var downID='#downQ'+tempID;
    var questionID=document.querySelector(ID);
    var upArrow=document.querySelector(upID);
    var downArrow=document.querySelector(downID);
    console.log(questionID);
    console.log(upArrow);
    $(upArrow).addClass('triangleup').removeClass('triangleupvoted');
    $.ajax({
            url: dataUrl,
            method: "GET",
            data: {},
            success: function (data) {
                console.log(data);
                var newLikes;
                if(data.downvote){
                    console.log(data.downvote);
                    newLikes=data.voteTotal;
                    console.log('upvote');
                    console.log(newLikes);
                    $(downArrow).addClass('triangledownvoted').removeClass('triangledown');
                    updateText(questionID,newLikes);

                }
                else{
                    newLikes=data.voteTotal;
                    console.log(data.downvote);
                    console.log('downvote');
                    console.log(newLikes);
                    $(downArrow).addClass('triangledown').removeClass('triangledownvoted');
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

$(".A-upvote-link ").click(function (e) {
    console.log('test');
    e.preventDefault();
    console.log('preventDefault works');
    var dataUrl = $(this).attr('data-href');
    var tempID=("#answer"+($(this).attr("data-upvote")));
    var questionID=document.querySelector(tempID);
    console.log(questionID);
    $.ajax({
            url: dataUrl,
            method: "GET",
            data: {},
            success: function (data) {
                console.log(data);
                var newLikes;
                if(data.upvote){
                    console.log(data.upvote);
                    newLikes=data.voteTotal;
                    console.log('upvote');
                    console.log(newLikes);
                    updateText(questionID,newLikes);

                }
                else{
                    newLikes=data.voteTotal;
                    console.log(data.upvote);
                    console.log('downvote');
                    console.log(newLikes);
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

$(".A-downvote-link ").click(function (e) {
    console.log('test');
    e.preventDefault();
    console.log('preventDefault works');
    var dataUrl = $(this).attr('data-href');
    var tempID=("#answer"+($(this).attr("data-downvote")));
    var questionID=document.querySelector(tempID);
    console.log(questionID);
    $.ajax({
            url: dataUrl,
            method: "GET",
            data: {},
            success: function (data) {
                console.log(data);
                var newLikes;
                if(data.downvote){
                    console.log(data.downvote);
                    newLikes=data.voteTotal;
                    console.log('upvote');
                    console.log(newLikes);
                    updateText(questionID,newLikes);

                }
                else{
                    newLikes=data.voteTotal;
                    console.log(data.downvote);
                    console.log('downvote');
                    console.log(newLikes);
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