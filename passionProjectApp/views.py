from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from .forms import RealQuestionForm,RealQuestion,UserForm,AnswerForm,Answer,RealQuestionComment,AnswerComment,CommentAnswerForm,CommentQuestionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils.http import is_safe_url
from django.db.models import Count

import datetime
import urllib.request

# Create your views here.

def index(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    allquestions=RealQuestion.objects.annotate(count=Count('answer')).order_by('count').reverse()[:20]
    context={"allquestions":allquestions, "randomquestion":randomquestion,}
    return render(request,"passionProjectApp/index.html",context)
def register(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    form=UserForm(request.POST or None)
    print('here')
    if request.method =="POST":
        if form.is_valid():
            newuser=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
            login_created_author=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password']) #checks to see if this is a valid user, if so return a user object
            login(request,login_created_author) #request that this user is logged in
            redirect_to = request.GET.get('next', None) # use get or Post as per your requirement
            safe_url=is_safe_url(redirect_to,allowed_hosts=request.get_host())
            print(redirect_to)
            print(safe_url)
            print(request.get_host())
            if redirect_to==None:
                return redirect('index')
            if safe_url:
                return redirect(redirect_to)
            print('not save')
            return redirect('register')
        else:
            form=UserForm(request.POST or None)
            context={'form':form,'errors':form.errors}
            return render(request,"passionProjectApp/register.html",context,)
    return render(request,"passionProjectApp/register.html",{"form":form, "randomquestion":randomquestion})
def registerPass(request):
    return render(request,"passionProjectApp/registerPass.html")
def allquestions(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    questionlist=RealQuestion.objects.all()
    return render(request,'passionProjectApp/allquestions.html',{'questionlist':questionlist,'randomquestion':randomquestion})

@login_required
def ask(request):
    randomquestion=RealQuestion.objects.all().order_by('?')[:10]
    form=RealQuestionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            RealQuestion.objects.create(title=request.POST['title'],question=request.POST['question'],author=request.user)
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
        questionID.delete()
        return redirect('index')
    context={'form':form,'question':questionID, "randomquestion":randomquestion}
    return render(request,"passionProjectApp/ask_del.html",context)
@login_required
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
            return redirect('ask_read',parentquestionID)
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
        answerID.delete()
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
        questionCommentID.delete()
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
        answerCommentID.delete()
        return redirect('ask_read',questionID.id)
    return render(request,"passionProjectApp/comment_answer_del.html",context)



# def annotate(request):
#     count=RealQuestion.objects.all().order_by()


def search (request):
    return render(request,"passionProjectApp/search.html")

