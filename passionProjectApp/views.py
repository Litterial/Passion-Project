from django.shortcuts import render,redirect,get_object_or_404
from .forms import RealQuestionForm,RealQuestion,UserForm,AnswerForm,Answer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def index(request):
    allquestions=RealQuestion.objects.all()
    context={"allquestions":allquestions}
    return render(request,"passionProjectApp/index.html",context)
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
def edit_ask(request):
    return render(request,"passionProjectApp/edit_ask.html",)
def del_ask(request):
    return render(request,"passionProjectApp/del_ask.html")


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
def edit_ans(request):
    return render(request,"passionProjectApp/edit_ans.html")
def del_ans(request):
    return render(request,"passionProjectApp/del_ans.html")
def search (request):
    return render(request,"passionProjectApp/search.html")