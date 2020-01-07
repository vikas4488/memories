from .models import MhqEmpData,Theme,MhqEmpFeedback as mef,MhqEmp
from datetime import datetime
from django.contrib.sessions.models import Session
from django.db.models import Q
class Help:
    @staticmethod
    def colorhelp(allcolor):
        allcolor=allcolor.split(":")
        css={}
        style={}
        color={}
        i=0
        while i < len(allcolor)-1:
            classname=allcolor[i].replace("_","")
            i=i+1
            clr1=allcolor[i][:7]
            clr2=allcolor[i][-7:]
            i=i+1
            css[classname]='background-color:'+clr1+';color:'+clr2+';'
            style[classname]='style=background-color:'+clr1+';color:'+clr2+';'
        color["css"]=css
        color["style"]=style
        return  color

    @staticmethod
    def filterRecord(request):
        if 'specificdate' in request.POST:
            entries=MhqEmpData.objects.filter(userid=request.session['userid'],wdate__date=request.POST['specificdate'])
        elif 'date1' in request.POST:
            entries=MhqEmpData.objects.filter(userid=request.session['userid'],wdate__range=(request.POST['date1'], request.POST['date2']))
        elif 'searchkey' in request.POST:
            entries=MhqEmpData.objects.filter(userid=request.session['userid'],work__icontains=request.POST['searchkey']) | MhqEmpData.objects.filter(userid=request.session['userid'],names__icontains=request.POST['searchkey'])
        else:
            entries=MhqEmpData.objects.filter(userid=request.session['userid'])
        return entries

    @staticmethod
    def newrecord(request):
        w=MhqEmpData()
        w.userid=request.session['userid']
        w.edate=datetime.now()
        w.wdate=request.POST['wdate']
        w.udate=datetime.now()
        w.names=request.POST['names']
        w.work=request.POST['work']
        w.attendance=request.POST['attendance']
        w.save()
        return 'record added'
    @staticmethod
    def themeprocess(request):
        theme=Theme.objects.filter(userid=request.session['userid']) | Theme.objects.filter(type='system')
        color=[]
        for t in theme:
            tcolor={}
            allcolor=t.color.split(":")
            i=0
            c=[]
            while i < len(allcolor)-1:
                clr={}
                classname=allcolor[i].replace("_","")
                i=i+1
                clr1=allcolor[i][:7]
                clr2=allcolor[i][-7:]
                i=i+1
                clr['clr1']=clr1
                clr['clr2']=clr2
                clr['name']=classname
                c.append(clr)
            tcolor['name']=t.name
            tcolor['type']=t.type
            tcolor['clrstr']=c
            tcolor['id']=t.id
            color.append(tcolor)
        return color
    @staticmethod
    def updateRecord(request):
        w=MhqEmpData.objects.get(id=request.POST['wid'])
        w.wdate=request.POST['wdate']
        w.udate=datetime.now()
        w.name=request.POST['names']
        w.work=request.POST['work']
        w.attendance=request.POST['attendance']
        w.save()
        return 'record updated'

    @staticmethod
    def createtheme(request):
        msg="some error occured"
        if 'tid' in request.POST:
            th=Theme.objects.get(id=request.POST['tid'])
            th.delete()
            msg="theme deleted"
        else:
            if 'themeid' in request.POST:
                th=Theme.objects.get(id=request.POST['themeid'])
                msg="theme updated"
            else:
                th=Theme()
                msg="theme added"
            nclr=request.POST.getlist('nclr')
            fclr=request.POST.getlist('fclr')
            color="bgclr:navclr:cardclr:labelclr:popupclr:btncnf:btnpro:btnupd:btnrej:ipclr:loginborder:regborder:loginlabelclr:reglabelclr"
            c=color.split(":")
            cs=""
            i=0
            for n in nclr:
                cs=cs+c[i]+":"+nclr[i]+fclr[i]+":"
                i=i+1
            cs=cs[:-1]
            th.userid=request.session['userid']
            th.color=cs
            th.name=request.POST['themename']
            th.type="usertype"
            th.save()
        return msg

    @staticmethod
    def submitToAdmin(request):
        w=mef()
        w.userid=request.session['userid']
        w.message=request.POST['message']
        w.status='unread'
        w.touser='admin'
        w.edate=datetime.now()
        w.save()
        return 'message sent'

    @staticmethod
    def settheme(request):
        clr=Theme.objects.get(pk=request.POST['themeid'])
        request.session['color'] = clr.color
        emp=MhqEmp.objects.get(userid=request.session['userid'])
        emp.theme=request.POST['themeid']
        emp.save()
        return 'theme applied'
    @staticmethod
    def logout(request):
        Session.objects.all().delete()
        return "logged out sucess"

    @staticmethod
    def getmessages(request):
        m=mef.objects.filter(Q(userid=request.session['userid'])|Q(touser=request.session['userid']))
        return m




