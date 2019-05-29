from django.shortcuts import render,redirect
from .forms import RealQuestionForm,RealQuestion,UserForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"passionProjectApp/index.html")
def ask(request):
    allquestions=RealQuestion.objects.all()
    context={"allquestions":allquestions}
    return render(request,"passionProjectApp/ask.html",context)
def register(request):
    form=UserForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            newuser=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
            return redirect('registerPass')
    else:
        form=UserForm(request.POST)
        context={
            'form':form,
            'errors':form.errors
        }
        return render(request,"passionProjectApp/register.html",context)
    # return render(request,"passionProjectApp/register.html",{'form':form})

def registerPass(request):
    return render(request,"passionProjectApp/registerPass.html")
def edit_ask(request):
    form=RealQuestionForm(request.POST or None)
    return render(request,"passionProjectApp/edit_ask.html",{"form":form})
def del_ask(request):
    return render(request,"passionProjectApp/del_ask.html")
def answer(request):
    return render(request,"passionProjectApp/answer.html")
def edit_ans(request):
    return render(request,"passionProjectApp/edit_ans.html")
def del_ans(request):
    return render(request,"passionProjectApp/del_ans.html")
def search (request):
    return render(request,"passionProjectApp/search.html")