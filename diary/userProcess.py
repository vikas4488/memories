from .models import MhqEmp,Theme
class UserProcess:
    @staticmethod
    def register(request):
        msg="register_i"
        try:
            emp=MhqEmp.objects.get(userid=request.POST['pnumber'])
            msg="user_alerady_exist"
        except:
            emp=MhqEmp()
            emp.fname=request.POST['fname']
            emp.lname=request.POST['lname']
            emp.gender=request.POST['gender']
            emp.phone=request.POST['pnumber']
            emp.userid=request.POST['pnumber']
            emp.user_type='local'
            emp.lan='en'
            emp.theme=1
            emp.address=request.POST['place']
            emp.ui_type=request.POST['ui_type']
            emp.password=request.POST['password']
            emp.save()
            msg="register_successful"
        return msg
    @staticmethod
    def login(request):
        uid=request.POST['userid']
        password=request.POST['password']
        msg="login_i"
        try:
            emp=MhqEmp.objects.get(userid=uid)
            if emp.password==password:
                msg="login_success"
                request.session['userid'] = emp.userid
                request.session['fname'] = emp.fname
                request.session['lname'] = emp.lname
                if emp.lan=="en":
                    request.session['lan'] = "हिंदी"
                else:
                    request.session['lan'] = "english"
                clr=Theme.objects.get(pk=emp.theme)
                request.session['color'] = clr.color
            else:
                msg="login_failed"
        except:
            msg="user_does_not_exist"
        return msg

    @staticmethod
    def updateUser(request):
        emp=MhqEmp.objects.get(userid=request.session['userid'])
        emp.fname=request.POST['fname']
        emp.lname=request.POST['lname']
        emp.address=request.POST['place']
        emp.save()
        return "updated_successfully"