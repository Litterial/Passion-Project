from django.shortcuts import render,redirect,get_object_or_404
from .forms import RealQuestionForm,RealQuestion,UserForm,AnswerForm,Answer,RealQuestionComment,AnswerComment,CommentAnswerForm,CommentQuestionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    allquestions=RealQuestion.objects.all()
    context={"allquestions":allquestions}
    return render(request,"passionProjectApp/index.html",context)
def register(request):
    form=UserForm(request.POST or None)
    print('here')
    if request.method =="POST":
        if form.is_valid():
            newuser=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
            return render(request,"passionProjectApp/registerPass.html")
        else:
            form=UserForm(request.POST or None)
            context={'form':form,'errors':form.errors}
            return render(request,"passionProjectApp/register.html",context)
    return render(request,"passionProjectApp/register.html",{"form":form})
def registerPass(request):
    return render(request,"passionProjectApp/registerPass.html")



@login_required
def ask(request):
    form=RealQuestionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            RealQuestion.objects.create(title=request.POST['title'],question=request.POST['question'],author=request.user)
            return redirect('index')
        else:
            form=RealQuestionForm(request.POST or None)
            context={'form':form,'errors':form.errors}
            return render(request,'passionProjectApp/ask.html',context)
    return render(request,"passionProjectApp/ask.html",{"form":form})
def ask_edit(request,ID):
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
            context={"form":form,"errors":form.errors,"question":questionID}
            return render(request,"passionProjectApp/ask_edit.html",context)
    return render(request,"passionProjectApp/ask_edit.html",{'form':form,"question":questionID})
def ask_del(request):
    return render(request,"passionProjectApp/ask_del.html")
def ask_read(request,ID):
    question=get_object_or_404(RealQuestion,pk=ID)
    allAnswers=Answer.objects.filter(parent=ID)
    allQuestionComments=RealQuestionComment.objects.filter(parent=ID)
    allAnswerComments=AnswerComment.objects.all()
    answercomment_child=[]
    for x in allAnswers:
        for y in allAnswerComments:
            if (y.parent==x):
                answercomment_child.append(y)
    context={"question":question,"answers":allAnswers,"question_comment":allQuestionComments,"answer_comment":answercomment_child}
    return render(request,"passionProjectApp/ask_read.html",context)


@login_required
def answer(request,ID):
    parentquestionID=get_object_or_404(RealQuestion,pk=ID)
    form=AnswerForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            Answer.objects.create(message=request.POST['message'],parent=parentquestionID,author=request.user)
            return redirect('index')
        else:
            form=AnswerForm(request.POST or None)
            context={'form':form,'errors':form.errors}
            return render(request,"passionProjectApp/answer.html",context)
    return render(request,"passionProjectApp/answer.html",{"form":form})
def answer_edit(request,ID):
    answerID=get_object_or_404(Answer,pk=ID)
    print(answerID.author)
    form=AnswerForm(instance=answerID)
    if request.method=='POST':
        print(form)
        form=AnswerForm(request.POST,instance=answerID)
        print("new form")
        print(form)
        if form.is_valid():
            print('form was valid')
            answerID.last_update=datetime.datetime.utcnow()
            form.save()
            return redirect("ask_read",answerID.parent.id)
        else:
            print("i'm on else")
            form=AnswerForm(request.POST,instance=AnswerForm)
            context={"form":form,"errors":form.errors,"answer":answerID}
        return render(request,"passionProjectApp/answer_edit.html",context)
    return render(request,"passionProjectApp/answer_edit.html",{'form':form,"question":answerID})
def answer_del(request):
    return render(request,"passionProjectApp/answer_del.html")

@login_required
def comment_ask(request,ID):
    parentquestionID=get_object_or_404(RealQuestion,pk=ID)
    form=CommentQuestionForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            RealQuestionComment.objects.create(message=request.POST['message'],parent=parentquestionID,author=request.user)
            return redirect("index")
        else:
            form=CommentQuestionForm(request.POST or None)
            context={"form":form,"errors":form.errors}
            return render(request,'passionProjectApp/comment_ask.html',context)
    return render(request,'passionProjectApp/comment_ask.html',{"form":form})
def comment_ask_edit(request):
    return render(request,"passionProjectApp/comment_ask_edit.html")
def comment_ask_del(request):
    return render(request,"passionProjectApp/comment_ask_del.html")

@login_required
def comment_answer(request,ID):
    parentanswerID=get_object_or_404(Answer,pk=ID)
    form=CommentAnswerForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            AnswerComment.objects.create(message=request.POST['message'],parent=parentanswerID,author=request.user)
            return redirect("index")
        else:
            form=CommentAnswerForm(request.POST or None)
            context={"form":form,"errors":form.errors}
            return render(request,"passionProjectApp/comment_answer.html",context)
    return render(request,'passionProjectApp/comment_answer.html',{"form":form})
def comment_answer_edit(request):
    return render(request,"passionProjectApp/comment_answer_edit.html")
def comment_answer_del(request):
    return render(request,"passionProjectApp/comment_answer_del.html")


def search (request):
    return render(request,"passionProjectApp/search.html")