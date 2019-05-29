from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path('register/',views.register,name='register'),
    path('registerpass/',views.registerPass,name='registerpass'),

    path("ask/",views.ask,name='ask'),
    path("ask/edit/",views.edit_ask,name="edit_ask"),
    path("ask/delete/",views.del_ask,name='del_ask'),



    path("answer/<int:ID>/",views.answer,name='answer'),
    path('answer/edit/',views.edit_ans,name="edit_ans"),
    path('answer/delete/',views.del_ans,name="del_ans"),




    path('search/',views.search,name='search'),
]