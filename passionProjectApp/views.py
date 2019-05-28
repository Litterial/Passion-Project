from django.shortcuts import render
from .forms import RealQuestionForm,RealQuestion
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"passionProjectApp/index.html")
def ask(request):
    allquestions=RealQuestion.objects.all()
    context={"allquestions":allquestions}
    return render(request,"passionProjectApp/ask.html",context)
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