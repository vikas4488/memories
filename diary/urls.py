from django.urls import path

from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('dataentry',views.dataentry,name='dataentry'),
    path('viewrecords',views.viewrecords,name='viewrecords'),
    path('contactadmin',views.contactadmin,name='contactadmin'),
    path('logout',views.logout,name='logout'),
    path('help',views.help,name='help'),
    path('about',views.about,name='about'),
    path('theme',views.theme,name='theme'),
    path('home',views.navigation,name='navigation'),
    path('updaterecords',views.updaterecords,name='updaterecords'),
    path('createtheme',views.createtheme,name='createtheme'),
    path('settheme',views.settheme,name='settheme'),
    #path('theme/(?P<msg>\w+)/$',views.theme,name='theme'),
    #path('<int:h_id>/details', views.details, name='details'),
]

