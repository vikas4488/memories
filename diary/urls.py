from django.urls import path

from.import views
from rest_framework.urlpatterns import format_suffix_patterns
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
    path('superuser',views.superuser,name='superuser'),
    path('getnewmsg',views.getnewmsg,name='getnewmsg'),
    #path('theme/(?P<msg>\w+)/$',views.theme,name='theme'),
    #path('<int:h_id>/details', views.details, name='details'),
    path('react/login', views.login_react),
    #path('basic/<int:pk>/', views.API_objects_details.as_view()),
    path('react/fetchr', views.fetchr_react),
]

urlpatterns = format_suffix_patterns(urlpatterns)

