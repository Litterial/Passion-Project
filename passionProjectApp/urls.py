from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path('register/',views.register,name='register'),
    path('registerpass/',views.registerPass,name='registerpass'),

    path('ask/read/<int:ID>/',views.ask_read,name='ask_read'),

    path("ask/",views.ask,name='ask'),
    path("ask/edit/<int:ID>",views.ask_edit,name="ask_edit"),
    path("ask/delete/<int:ID>",views.ask_del,name='ask_del'),



    path("answer/<int:ID>/",views.answer,name='answer'),
    path('answer/edit/<int:ID>/',views.answer_edit,name="answer_edit"),
    path('answer/delete/<int:ID>/',views.answer_del,name="answer_del"),

    path('ask/comment/<int:ID>/',views.comment_ask,name='comment_ask'),
    path('ask/comment/<int:ID>/edit',views.comment_ask_edit,name='comment_ask_edit'),
    path('ask/comment/<int:ID>/delete',views.comment_ask_del,name='comment_ask_del'),

    path('answer/comment/<int:ID>/',views.comment_answer,name='comment_answer'),
    path('answer/comment/<int:commentID>/edit/<int:grandparentID>/',views.comment_answer_edit,name='comment_answer_edit'),
    path('answer/comment/<int:ID>/delete',views.comment_answer_del,name='comment_answer_del'),

    path('test/',views.test,name='test'),
    path('changename/<str:name_change>/',views.nameChange,name='nameChange'),
    path('nameReset/',views.nameReset,name='nameReset'),

    path('search/',views.search,name='search'),
]