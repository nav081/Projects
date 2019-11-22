
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('signin/',views.login),
    path('signup/',views.signup),
    path('store/',views.store,name="store"),
    path('signin/entry/',views.entry,name="entry"),
    path('storedata/',views.storedata,name='storedata'),
    path('check/',views.check,name='check'),
    path('date/',views.date,name='date'),
    path('back/',views.back)

]
