from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from .forms import RealQuestionForm,RealQuestion,UserForm,AnswerForm,Answer,RealQuestionComment,AnswerComment,CommentAnswerForm,CommentQuestionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils.http import is_safe_url
from django.db.models import Count
from django.core.paginator import Paginator
import datetime,os
from django.conf import settings
import urllib.request
from django.db.models import Q
from random import sample
from rest_framework.decorators import api_view,renderer_classes,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.

def index(request):
    #Finds 10 random questions
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]

    # grabs the id of every question found inside of randomquestion
    rando_reference=[p.id for p in randomquestion]
    print(rando_reference)
    today=datetime.datetime.utcnow()+datetime.timedelta(minutes=3)
    cutoff=datetime.datetime.utcnow()-datetime.timedelta(days=1)#cutoff date is ~24 hours before today

    #searchs for questions between today and the cutoff day and orders by in descending order
    #annotate calculates the values of each item in the query set
    tempquestions=RealQuestion.objects.filter(date_created__range=[cutoff,today]).annotate(count=Count('answer')).order_by('-count')
    #Paginator class takes a queryset argument and divides(paginations) it by a number argument
    paginator=Paginator(tempquestions,10)
    print(paginator)
    #request.GET looks for the key-value pair of the get request. .get() returns the value of the key.
    page=request.GET.get('page')
    print('lastpage')
    allquestions=paginator.get_page(page)
    print(paginator.num_pages)
    print(len(tempquestions))

    #used to find a different selection of questions from randomquestion in case there are no question created within the past 24 hours
    other=RealQuestion.objects.exclude(id__in = rando_reference).order_by('?')[:5]
    other_refernce=[p.id for p in other]
    print(rando_reference)
    print(other_refernce)
    range_limit=range(1,6)
    range_end=range(paginator.num_pages-4,paginator.num_pages+1)
    context={"allquestions":allquestions, "randomquestion":randomquestion,'other':other,'range_limit':range_limit,'range_end':range_end}
    print('today')
    print(today)
    print('cutoff')
    print(cutoff)
    return render(request,"passionProjectApp/index.html",context)

#code is very similar to index
def weekResults(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    #gets questions  with most answer
    rando_reference=[p.id for p in randomquestion]
    other=RealQuestion.objects.exclude(id__in = rando_reference).order_by('?')[:5]
    other_refernce=[p.id for p in other]
    today=datetime.datetime.utcnow()+datetime.timedelta(minutes=3)
    cutoff=datetime.datetime.utcnow()-datetime.timedelta(days=7) #cutoff is ~ 7 days from today
    tempquestions=RealQuestion.objects.filter(date_created__range=[cutoff,today]).annotate(count=Count('answer')).order_by('-count')
    paginator=Paginator(tempquestions,10)
    page=request.GET.get('page')
    print('lastpage')
    allquestions=paginator.get_page(page)
    context={"allquestions":allquestions, "randomquestion":randomquestion,"other":other}
    print('today')
    print(today)
    print('cutoff')
    print(cutoff)
    return render(request,"passionProjectApp/weekResults.html",context)

#code is very similiar to index
def monthResults(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    rando_reference=[p.id for p in randomquestion]
    other=RealQuestion.objects.exclude(id__in = rando_reference).order_by('?')[:5]
    other_refernce=[p.id for p in other]
    #gets questions  with most answer
    today=datetime.datetime.utcnow()+datetime.timedelta(minutes=3)
    cutoff=datetime.datetime.utcnow()-datetime.timedelta(days=31) #cutoff date is ~1 month from today
    tempquestions=RealQuestion.objects.filter(date_created__range=[cutoff,today]).annotate(count=Count('answer')).order_by('-count')
    paginator=Paginator(tempquestions,10)
    page=request.GET.get('page')
    print('lastpage')
    allquestions=paginator.get_page(page)
    context={"allquestions":allquestions, "randomquestion":randomquestion,"other":other}
    print('today')
    print(today)
    print('cutoff')
    print(cutoff)
    return render(request,"passionProjectApp/monthResults.html",context)

#user registration
def register(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    form=UserForm(request.POST or None)
    print('here')

    #checks to see if the request to the page is a post
    if request.method =="POST":
        #checks if the form is valid
        if form.is_valid():
            #creates the new user
            newuser=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])

            #checks to see if this is a valid user, if so return a user object
            login_created_author=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            #logs in the user after they register
            login(request,login_created_author)
            #looks for a get request and grabs the value of the key 'next'
            redirect_to = request.GET.get('next', None)
            #checks to see if the url is value to prevent user from being sent to a different site
            safe_url=is_safe_url(redirect_to,allowed_hosts=request.get_host())
            print(redirect_to)
            print(safe_url)
            print(request.get_host())
            #redirects user to index if there is no next request
            if redirect_to==None:
                return redirect('index')
            #if the url is save and there is a next request, directs user to the 'next' page
            if safe_url:
                return redirect(redirect_to)
            #else the site was not save and the user is redirected to register page to register again
            print('not save')
            return redirect('register')
        #If the form is somehow invalid
        else:
            form=UserForm(request.POST or None)
            context={'form':form,'errors':form.errors}
            return render(request,"passionProjectApp/register.html",context,)
    return render(request,"passionProjectApp/register.html",{"form":form, "randomquestion":randomquestion})

#test page for registration
def registerPass(request):
    return render(request,"passionProjectApp/registerPass.html")

# similar to index
def allquestions(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    questionlist=RealQuestion.objects.all().order_by('date_created')
    paginator=Paginator(questionlist,10)
    page=request.GET.get('page')
    range_limit=range(1,6)
    range_end=range(paginator.num_pages-4,paginator.num_pages+1)
    print('lastpage')
    questionpage=paginator.get_page(page)
    print("questions")
    print(questionpage)
    print("Count")
    print(paginator.num_pages)
    print("paginator")
    print(paginator)
    return render(request,'passionProjectApp/allquestions.html',{'questionlist':questionlist,'randomquestion':randomquestion,'questionpage':questionpage,'range_limit':range_limit,'range_end':range_end})

@login_required
def ask(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    form=RealQuestionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            RealQuestion.objects.create(title=request.POST['title'],question=request.POST['question'],topic=request.POST['topic'],author=request.user)
            return redirect('index')
        else:
            form=RealQuestionForm(request.POST or None)
            context={'form':form,'errors':form.errors, "randomquestion":randomquestion}
            return render(request,'passionProjectApp/ask.html',context)
    return render(request,"passionProjectApp/ask.html",{"form":form, "randomquestion":randomquestion})
@login_required
def ask_edit(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    questionID=get_object_or_404(RealQuestion,pk=ID)
    print(questionID.author)
    form=RealQuestionForm(instance=questionID)
    if request.method=='POST':
        print(form)
        form=RealQuestionForm(request.POST,instance=questionID)
        print("new form")
        print(form)
        if form.is_valid():
            print('form was valid')
            questionID.last_update=datetime.datetime.utcnow()
            form.save()
            return redirect("ask_read",questionID.id)
        else:
            print("i'm on else")
            form=RealQuestionForm(request.POST,instance=questionID)
            context={"form":form,"errors":form.errors,"question":questionID, "randomquestion":randomquestion}
            return render(request,"passionProjectApp/ask_edit.html",context)
    return render(request,"passionProjectApp/ask_edit.html",{'form':form,"question":questionID, "randomquestion":randomquestion})
@login_required
def ask_del(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    questionID=get_object_or_404(RealQuestion,pk=ID)
    form=RealQuestionForm(instance=questionID)
    if request.method=='POST':
        if 'delete' in request.POST:
            questionID.delete()
            return redirect('index')
        else:
            return redirect('ask_read',questionID.id)
    context={'form':form,'question':questionID, "randomquestion":randomquestion}
    return render(request,"passionProjectApp/ask_del.html",context)
def ask_read(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    question=get_object_or_404(RealQuestion,pk=ID)
    allAnswers=Answer.objects.filter(parent=ID)
    totalAnswers=len(allAnswers)
    allQuestionComments=RealQuestionComment.objects.filter(parent=ID)
    allAnswerComments=AnswerComment.objects.all()
    answercomment_child=[]
    for x in allAnswers:
        for y in allAnswerComments:
            if (y.parent==x):
                answercomment_child.append(y)
    form=AnswerForm(request.POST or None)
    context={"question":question,"answers":allAnswers,"question_comment":allQuestionComments,"answer_comment":answercomment_child,"form":form,"totalAnswers":totalAnswers, "randomquestion":randomquestion}
    return render(request,"passionProjectApp/ask_read.html",context)


@login_required
def answer(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    parentquestionID=get_object_or_404(RealQuestion,pk=ID)
    if 'message' in request.COOKIES:
        print("cookies")
        print(request.COOKIES['message'])
        decode=urllib.request.unquote(request.COOKIES['message'])
        print(decode)
        if decode[-1] ==";":
            decode=decode[:-1]
        cookie={'message':decode}
        print(cookie)
        form=AnswerForm(cookie)
        if form.is_valid():
            Answer.objects.create(message=decode, parent=parentquestionID,author=request.user)
            print('the code works here')
            response=redirect('ask_read',parentquestionID.id)
            response.delete_cookie('message')
            return response
        else:
            print('not valid')
            form=AnswerForm(request.POST or None)
            context={'form':form,'errors':form.errors}
            response=render(request,"passionProjectApp/answer.html",context)
            response.delete_cookie('message')
            return response
    form=AnswerForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            Answer.objects.create(message=request.POST['message'],parent=parentquestionID,author=request.user)
            return redirect('ask_read',parentquestionID.id)
        else:
            form=AnswerForm(request.POST or None)
            context={'form':form,'errors':form.errors}
            return render(request,"passionProjectApp/answer.html",context)
    return render(request,"passionProjectApp/answer.html",{"form":form,"randomquestion":randomquestion,})
@login_required
def answer_edit(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    answerID=get_object_or_404(Answer,pk=ID)
    print(answerID.author)
    form=AnswerForm(None, instance=answerID)
    if request.method=='POST':
        print("new form")
        form=AnswerForm(request.POST,instance=answerID)
        print(form)
        if form.is_valid():
            form=AnswerForm(request.POST,instance=answerID)
            print('form was valid')
            answerID.last_update=datetime.datetime.utcnow()
            form.save()
            return redirect("ask_read",answerID.parent.id)
        else:
            form=AnswerForm(request.POST,instance=answerID)
            context={"form":form,"errors":form.errors,"answer":answerID,"randomquestion":randomquestion,}
        return render(request,"passionProjectApp/answer_edit.html",context)
    return render(request,"passionProjectApp/answer_edit.html",{'form':form,"answer":answerID,"randomquestion":randomquestion,})
@login_required
def answer_del(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    answerID=get_object_or_404(Answer,pk=ID)
    print(answerID)
    tempanswerID=answerID
    form=AnswerForm(instance=answerID)
    if request.method=='POST':
        if 'delete' in request.POST:
            answerID.delete()
            return redirect('ask_read',tempanswerID.parent.id)
        else:
            return redirect('ask_read',tempanswerID.parent.id)
    context={'form':form,'answer':answerID, "randomquestion":randomquestion}
    print(request.method)
    return render(request,"passionProjectApp/answer_del.html",context)

@login_required
def comment_ask(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    parentquestionID=get_object_or_404(RealQuestion,pk=ID)
    form=CommentQuestionForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            RealQuestionComment.objects.create(message=request.POST['message'],parent=parentquestionID,author=request.user)
            return redirect("ask_read",parentquestionID.id)
        else:
            form=CommentQuestionForm(request.POST or None)
            context={"form":form,"errors":form.errors}
            return render(request,'passionProjectApp/comment_ask.html',context)
    return render(request,'passionProjectApp/comment_ask.html',{"form":form, "randomquestion":randomquestion})
@login_required
def comment_ask_edit(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    questionCommentID=get_object_or_404(RealQuestionComment,pk=ID)
    print(questionCommentID.author)
    form=CommentQuestionForm(instance=questionCommentID)
    if request.method=='POST':
        print(form)
        form=CommentQuestionForm(request.POST,instance=questionCommentID)
        print("new form")
        print(form)
        if form.is_valid():
            print('form was valid')
            questionCommentID.last_update=datetime.datetime.utcnow()
            form.save()
            return redirect("ask_read",questionCommentID.parent.id)
        else:
            print("i'm on else")
            form=CommentQuestionForm(request.POST,instance=questionCommentID)
            context={"form":form,"errors":form.errors,"questionComment":questionCommentID, "randomquestion":randomquestion}
        return render(request,"passionProjectApp/comment_ask_edit.html",context)
    return render(request,"passionProjectApp/comment_ask_edit.html",{'form':form,"questionComment":questionCommentID, "randomquestion":randomquestion})
@login_required
def comment_ask_del(request,ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    questionCommentID=get_object_or_404(RealQuestionComment,pk=ID)
    tempquestionCommentID=questionCommentID
    form=AnswerForm(instance=questionCommentID)
    context={'form':form,'questionComment':questionCommentID, "randomquestion":randomquestion}
    print('comment_ask_del')
    if request.method=='POST':
        if 'delete' in request.POST:
            questionCommentID.delete()
            return redirect('ask_read',tempquestionCommentID.parent.id)
        else:
            return redirect('ask_read',tempquestionCommentID.parent.id)
    return render(request,"passionProjectApp/comment_ask_del.html",context)
@login_required
def comment_answer(request, ID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    parentanswerID=get_object_or_404(Answer,pk=ID)
    form=CommentAnswerForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            AnswerComment.objects.create(message=request.POST['message'],parent=parentanswerID,author=request.user)
            return redirect("ask_read",parentanswerID.parent.id)
        else:
            form=CommentAnswerForm(request.POST or None)
            context={"form":form,"errors":form.errors, "randomquestion":randomquestion}
            return render(request,"passionProjectApp/comment_answer.html",context)
    return render(request,'passionProjectApp/comment_answer.html',{"form":form, "randomquestion":randomquestion})
@login_required
def comment_answer_edit(request, commentID, grandparentID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    answerCommentID=get_object_or_404(AnswerComment,pk=commentID)
    questionID=get_object_or_404(RealQuestion,pk=grandparentID)
    print(answerCommentID.author)
    form=CommentAnswerForm(instance=answerCommentID)
    if request.method=='POST':
        print(form)
        form=CommentAnswerForm(request.POST,instance=answerCommentID)
        print("new form")
        print(form)
        if form.is_valid():
            print('form was valid')
            answerCommentID.last_update=datetime.datetime.utcnow()
            form.save()
            return redirect("ask_read",questionID.id)
        else:
            print("i'm on else")
            form=CommentAnswerForm(request.POST,instance=answerCommentID)
            context={"form":form,"errors":form.errors,"answerComment":answerCommentID, "randomquestion":randomquestion}
        return render(request,"passionProjectApp/comment_ask_edit.html",context)
    return render(request,"passionProjectApp/comment_answer_edit.html",{'form':form,"answerComment":answerCommentID})
@login_required
def comment_answer_del(request,commentID,grandparentID):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    answerCommentID=get_object_or_404(AnswerComment,pk=commentID)
    questionID=get_object_or_404(RealQuestion,pk=grandparentID)
    print(questionID)
    print(answerCommentID)
    form=CommentAnswerForm(instance=answerCommentID)
    context={'form':form,'answerComment':answerCommentID,"question":questionID}
    if request.method=='POST':
        if 'delete' in request.POST:
            answerCommentID.delete()
            return redirect('ask_read',questionID.id)
        else:
            return('ask_read',questionID.id)
    return render(request,"passionProjectApp/comment_answer_del.html",context)



# def annotate(request):
#     count=RealQuestion.objects.all().order_by()


def search (request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    search=request.GET['search']
    newsearch='' + search + " "
    print(search)
    print(newsearch)
    questionsearch=RealQuestion.objects.filter(Q(title__icontains=search) | Q(question__icontains=search)|Q(topic__icontains=search)).distinct().annotate(count=Count('answer')).order_by('-count')
    print(questionsearch)
    paginator=Paginator(questionsearch,10)
    print(paginator)
    range_limit=range(1,6)
    range_end=range(paginator.num_pages-4,paginator.num_pages+1)
    page=request.GET.get('page')
    searchpage=paginator.get_page(page)
    print(searchpage)
    sum=len(questionsearch)
    context={ 'search':search,'searchpage':searchpage,'sum':sum,'randomquestion':randomquestion,'range_limit':range_limit,'range_end':range_end}
    file_ = open(os.path.join(settings.BASE_DIR,  'common'))
    a=file_.read().split()
    for x in a:
        if x == search.lower():
            return render(request,'passionProjectApp/broadsearch.html',context)
    if sum == 0:
        return render(request,'passionProjectApp/broadsearch.html',context)
    return render(request,"passionProjectApp/search.html",context)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def questionUpvote(request,ID):
    like=get_object_or_404(RealQuestion,pk=ID)
    upvote=False
    update=False
    if request.user.is_authenticated:
        if request.user in like.upvote.all():
            like.upvote.remove(request.user)
            like.downvote.remove(request.user)
        else:
            like.upvote.add(request.user)
            like.downvote.remove(request.user)
            upvote=True
        update=True
        voteTotal=(len(like.upvote.all())-len(like.downvote.all()))
        print(voteTotal)
        data={'upvote':upvote,"update":update,"voteTotal":voteTotal}
        return Response(data)
        # return redirect('index')
    else:
        print('hi')
        # return Response(context)
        return redirect ('index')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def questionDownvote(request,ID):
    dislike=get_object_or_404(RealQuestion,pk=ID)
    downvote=False
    update=False
    if request.user.is_authenticated:
        if request.user in dislike.downvote.all():
            dislike.downvote.remove(request.user)
            dislike.upvote.remove(request.user)
            print('remove')
        else:
            downvote=True
            dislike.downvote.add(request.user)
            dislike.upvote.remove(request.user)
            downvote=True
            print('add')
        update=True
        voteTotal=(len(dislike.upvote.all())-len(dislike.downvote.all()))
        data={'downvote':downvote,"update":update,"voteTotal":voteTotal}
        print(data)
        return Response(data)
        # return redirect('index')
    else:
        print('hi')
        # return Response(context)
        return redirect ('index')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def answerUpvote(request,ID):
    like=get_object_or_404(Answer,pk=ID)
    upvote=False
    update=False
    if request.user.is_authenticated:
        if request.user in like.upvote.all():
            like.upvote.remove(request.user)
            like.downvote.remove(request.user)
        else:
            like.upvote.add(request.user)
            like.downvote.remove(request.user)
            upvote=True;
        update=True
        voteTotal=(len(like.upvote.all())-len(like.downvote.all()))
        print(voteTotal)
        data={'upvote':upvote,"update":update,"voteTotal":voteTotal}
        return Response(data)
        # return redirect('index')
    else:
        print('hi')
        # return Response(context)
        return redirect ('index')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def answerDownvote(request,ID):
    dislike=get_object_or_404(Answer,pk=ID)
    downvote=False
    update=False
    if request.user.is_authenticated:
        if request.user in dislike.downvote.all():
            dislike.downvote.remove(request.user)
            dislike.upvote.remove(request.user)
            print('remove')
        else:
            downvote=True
            dislike.downvote.add(request.user)
            dislike.upvote.remove(request.user)
            print('add')
        update=True
        voteTotal=(len(dislike.upvote.all())-len(dislike.downvote.all()))
        data={'downvote':downvote,"update":update,"voteTotal":voteTotal}
        print(data)
        return Response(data)
        # return redirect('index')
    else:
        print('hi')
        # return Response(context)
        return redirect ('index')
