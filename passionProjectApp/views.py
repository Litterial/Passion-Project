from django.shortcuts import render,redirect,get_object_or_404
from .forms import RealQuestionForm,RealQuestion,UserForm,AnswerForm,Answer,RealQuestionComment,AnswerComment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
def ask_edit(request):
    return render(request,"passionProjectApp/ask_edit.html",)
def ask_del(request):
    return render(request,"passionProjectApp/ask_del.html")
def ask_read(request,ID):
    question=get_object_or_404(RealQuestion,pk=ID)
    print(question)
    print(type(question))
    allAnswers=Answer.objects.filter(parent=ID)
    allQuestionComments=RealQuestionComment.objects.filter(parent=ID)
    allAnswerComments=AnswerComment.objects.filter(parent_id=ID)
    print(allAnswers)
    context={"question":question,"answers":allAnswers,"question_comment":allQuestionComments,"answer_comment":allAnswerComments}
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
def answer_edit(request):
    return render(request,"passionProjectApp/answer_edit.html")
def answer_del(request):
    return render(request,"passionProjectApp/answer_del.html")

@login_required
def comment_ask(request):
    return render(request,'passionProjectApp/comment_ask.html')
def comment_ask_edit(request):
    return render(request,"passionProjectApp/comment_ask_edit.html")
def comment_ask_del(request):
    return render(request,"passionProjectApp/comment_ask_del.html")

@login_required
def comment_answer(request):
    return render(request,'passionProjectApp/comment_answer.html')
def comment_answer_edit(request):
    return render(request,"passionProjectApp/comment_answer_edit.html")
def comment_answer_del(request):
    return render(request,"passionProjectApp/comment_answer_del.html")


def search (request):
    return render(request,"passionProjectApp/search.html")