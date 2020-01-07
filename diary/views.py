from django.shortcuts import render, redirect
from .models import MhqEmp,MhqEmpData
#from utils.userProcess import UserProcess
from .userProcess import UserProcess as up
from .helper import Help as hp
from django.http import HttpResponse

def index(request):
    if 'userid' not in request.session:
        return render(request, 'diary/index.html')
    else:
        return redirect(navigation)
def register(request):
    if 'userid' not in request.session:
        up.register(request)
        return render(request, 'diary/index.html')
    else:
        return redirect(navigation)
def login(request):
    if 'userid' not in request.session:
        status=up.login(request)
        if status=="login_success":
            return redirect(navigation)
        elif status=="user_does_not_exist":
            return render(request, 'diary/index.html')
        else:
            return render(request, 'diary/index.html')
    else:
        return redirect(navigation)

def userprofile(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        popmsg='empty'
        if request.method == 'POST':
            popmsg=up.updateUser(request)
        color=hp.colorhelp(request.session['color'])
        emp=MhqEmp.objects.get(userid=request.session['userid'])
        return render(request, 'diary/userprofile.html',{'emp':emp,'lan':request.session['lan'],'css':color["css"],'style':color["style"],'popmsg':popmsg})
def dataentry(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        popmsg='empty'
        if request.method == 'POST':
            popmsg=hp.newrecord(request)
        color=hp.colorhelp(request.session['color'])
        return render(request, 'diary/dataentry.html',{'lan':request.session['lan'],'css':color["css"],'style':color["style"],'popmsg':popmsg})
def viewrecords(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        if request.method == 'POST':
            entries=hp.filterRecord(request)
        else:
            entries=MhqEmpData.objects.filter(userid=request.session['userid'])
        color=hp.colorhelp(request.session['color'])
        return render(request, 'diary/viewrecords.html',{'entries':entries,'lan':request.session['lan'],'css':color["css"],'style':color["style"],'popmsg':'empty'})
def contactadmin(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        if request.is_ajax():
            message=hp.submitToAdmin(request)
            return HttpResponse(message)
        color=hp.colorhelp(request.session['color'])
        msg=hp.getmessages(request)
        return render(request, 'diary/contactadmin.html',{'lan':request.session['lan'],'css':color["css"],'style':color["style"],'popmsg':'empty','message':msg})
def help(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        color=hp.colorhelp(request.session['color'])
        return render(request, 'diary/help.html',{'lan':request.session['lan'],'css':color["css"],'style':color["style"],'popmsg':'empty'})
def about(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        color=hp.colorhelp(request.session['color'])
        return render(request, 'diary/about.html',{'lan':request.session['lan'],'css':color["css"],'style':color["style"],'popmsg':'empty'})
def createtheme(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        message=hp.createtheme(request)
        return redirect(theme)
def settheme(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        message=hp.settheme(request)
        return redirect(theme)
def theme(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        color=hp.colorhelp(request.session['color'])
        theme=hp.themeprocess(request)
        return render(request, 'diary/theme.html',{'theme':theme,'lan':request.session['lan'],'css':color["css"],'style':color["style"],'popmsg':'empty'})
def navigation(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        color=hp.colorhelp(request.session['color'])
        return render(request, 'diary/navigation.html',{'lan':request.session['lan'],'fname':request.session['fname'],'lname':request.session['lname'],'css':color["css"],'style':color["style"],'popmsg':'empty'})
def updaterecords(request):
    if 'userid' not in request.session:
        return redirect(index)
    else:
        if request.is_ajax():
            message=hp.updateRecord(request)
        else:
            message = "some error occured"
        return HttpResponse(message)
def logout(request):
    hp.logout(request)
    return redirect(index)