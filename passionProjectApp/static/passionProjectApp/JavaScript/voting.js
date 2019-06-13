


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
    var tempID=("#question"+($(this).attr("data-upvote")));
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

$(".Q-downvote-link ").click(function (e) {
    console.log('test');
    e.preventDefault();
    console.log('preventDefault works');
    var dataUrl = $(this).attr('data-href');
    var tempID=("#question"+($(this).attr("data-downvote")));
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