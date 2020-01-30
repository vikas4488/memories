from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from . serializers import meq,med
from .models import MhqEmp,MhqEmpData,Theme,MhqEmpFeedback as mef

class ReactHandler:
    @staticmethod
    def reg(request):
        #serializer = meq(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #print(serializer.data)
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return "register"
    @staticmethod
    def login(request):
        d=request.data
        uid=d['userId']
        password=d['password']
        email=d['email']
        fname=d['name']
        msg="login_i"
        if password == "gpass" and email != "nomail":
            try:
                empg=MhqEmp.objects.get(userid=uid)
                msg="login_success_google"
                sg = meq(empg)
                print(msg)
                return Response(sg.data)
            except:
                empn=MhqEmp()
                empn.userid=uid
                empn.fname=fname
                empn.user_type='local'
                empn.lan='en'
                empn.theme=1
                empn.email=email
                empn.ui_type='diary'
                empn.password='gpass'
                empn.save()   
                msg="reg_success_google"
                sn = meq(empn)
                print(msg)
                return Response(sn.data)     
        try:
            emp=MhqEmp.objects.get(userid=uid)
            if emp.password==password:
                msg="login_success"
                s1 = meq(emp)
                print(msg)
                return Response(s1.data)
            else:
                msg="login_failed" 
                print (msg)
                return Response( status=status.HTTP_206_PARTIAL_CONTENT)   
        except:
            msg="user_does_not_exist"  
            print (msg)
            return Response( status=status.HTTP_204_NO_CONTENT)
        return Response( status=status.HTTP_400_BAD_REQUEST)  

    @staticmethod
    def fetchr(request):
        d=request.data
        uid=d['userId']
        msg="login_i"
        try:
            d=request.data
            uid=d['userId']
            msg="login_i"
            mdata=MhqEmpData.objects.filter(userid=uid)
            msg="data fetched"
            print(uid)
            s1 = med(mdata, many=True)
            print(msg)
            return Response(s1.data)
        except:
            msg="some problem while fetching data"  
            print (msg)
            return Response( status=status.HTTP_204_NO_CONTENT)
        return Response( status=status.HTTP_400_BAD_REQUEST)  

