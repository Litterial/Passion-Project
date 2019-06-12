from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path('week/',views.weekResults,name='week'),
    path('month/',views.monthResults,name='month'),
    path('register/',views.register,name='register'),
    path('registerpass/',views.registerPass,name='registerpass'),
    path('allquestions/',views.allquestions,name='allquestions'),
    path('ask/read/<int:ID>/',views.ask_read,name='ask_read'),

    path("ask/",views.ask,name='ask'),
    path("ask/edit/<int:ID>/",views.ask_edit,name="ask_edit"),
    path("ask/delete/<int:ID>/",views.ask_del,name='ask_del'),



    path("answer/<int:ID>/",views.answer,name='answer'),
    path('answer/edit/<int:ID>/',views.answer_edit,name="answer_edit"),
    path('answer/delete/<int:ID>/',views.answer_del,name="answer_del"),

    path('ask/comment/<int:ID>/',views.comment_ask,name='comment_ask'),
    path('ask/comment/<int:ID>/edit/',views.comment_ask_edit,name='comment_ask_edit'),
    path('ask/comment/<int:ID>/delete/',views.comment_ask_del,name='comment_ask_del'),

    path('answer/comment/<int:ID>/',views.comment_answer,name='comment_answer'),
    path('answer/comment/<int:commentID>/edit/<int:grandparentID>/',views.comment_answer_edit,name='comment_answer_edit'),
    path('answer/comment/<int:commentID>/delete/<int:grandparentID>/',views.comment_answer_del,name='comment_answer_del'),



    path('search/',views.search,name='search'),

    path('upvote/question/<int:ID>/',views.questionUpvote,name='questionUpvote'),
    path('downvote/question/<int:ID>/',views.questionDownvote,name='questionDownvote'),
    path('upvote/answer/<int:ID>/',views.answerUpvote,name='answerUpvote'),
    path('downvote/answer/<int:ID>',views.answerDownvote,name='answerDownvote'),
]