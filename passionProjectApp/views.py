from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from .forms import RealQuestionForm,RealQuestion,UserForm,AnswerForm,Answer,RealQuestionComment,AnswerComment,CommentAnswerForm,CommentQuestionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils.http import is_safe_url
import datetime

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
            login_created_author=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password']) #checks to see if this is a valid user, if so return a user object
            login(request,login_created_author) #request that this user is logged in
            redirect_to = request.GET.get('next', '') # use get or Post as per your requirement
            safe_url=is_safe_url(redirect_to,allowed_hosts=request.get_host())
            print(redirect_to)
            print(safe_url)
            print(request.get_host())
            if safe_url:
                return redirect(redirect_to)
            print('not save')
            return redirect('register')
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
    form=AnswerForm(request.POST or None)
    context={"question":question,"answers":allAnswers,"question_comment":allQuestionComments,"answer_comment":answercomment_child,"form":form}
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
            context={"form":form,"errors":form.errors,"answer":answerID}
        return render(request,"passionProjectApp/answer_edit.html",context)
    return render(request,"passionProjectApp/answer_edit.html",{'form':form,"answer":answerID})
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
def comment_ask_edit(request,ID):
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
            context={"form":form,"errors":form.errors,"questionComment":questionCommentID}
        return render(request,"passionProjectApp/comment_ask_edit.html",context)
    return render(request,"passionProjectApp/comment_ask_edit.html",{'form':form,"questionComment":questionCommentID})
def comment_ask_del(request):
    return render(request,"passionProjectApp/comment_ask_del.html")

@login_required
def comment_answer(request, ID):
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
def comment_answer_edit(request, commentID, grandparentID):
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
            context={"form":form,"errors":form.errors,"answerComment":answerCommentID}
        return render(request,"passionProjectApp/comment_ask_edit.html",context)
    return render(request,"passionProjectApp/comment_answer_edit.html",{'form':form,"answerComment":answerCommentID})
def comment_answer_del(request):
    return render(request,"passionProjectApp/comment_answer_del.html")

def test(request):
    name='Koichi'

    if 'name_change' in request.COOKIES:
        name=request.COOKIES['name_change']
    return HttpResponse(name)

def nameChange(request,name_change):
    response = redirect('test')
    response.set_cookie('name_change',name_change)
    return response
def nameReset(request):
    response=redirect('test')
    response.delete_cookie('name_change')
    return response
def search (request):
    return render(request,"passionProjectApp/search.html")