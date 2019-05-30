from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path('register/',views.register,name='register'),
    path('registerpass/',views.registerPass,name='registerpass'),

    path('ask/read/<int:ID>/',views.ask_read,name='ask_read'),

    path("ask/",views.ask,name='ask'),
    path("ask/edit/",views.ask_edit,name="ans_edit"),
    path("ask/delete/",views.ask_del,name='ask_del'),



    path("answer/<int:ID>/",views.answer,name='answer'),
    path('answer/edit/',views.answer_edit,name="answer_edit"),
    path('answer/delete/',views.answer_del,name="answer_del"),

    path('ask/comment/<int:ID>/',views.comment_ask,name='comment_ask'),
    path('ask/comment/<int:ID>/edit',views.comment_answer_edit,name='comment_answer_edit'),
    path('ask/comment/<int:ID>/delete',views.comment_answer_del,name='comment_answer_del'),

    path('answer/comment/<int:ID>/',views.comment_answer,name='comment_answer'),
    path('answer/comment/<int:ID>/edit',views.comment_answer_edit,name='comment_answer_edit'),
    path('answer/comment/<int:ID>/delete',views.comment_answer_del,name='comment_answer_del'),




    path('search/',views.search,name='search'),
]