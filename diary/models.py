from django.db import models

class MhqEmp(models.Model):
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)
    lan = models.CharField(max_length=200)
    ui_type = models.CharField(max_length=200)
    theme = models.CharField(max_length=100)

class MhqEmpData(models.Model):
    userid = models.CharField(max_length=200)
    edate = models.DateTimeField('entry date')
    udate = models.DateTimeField('update date')
    wdate = models.DateTimeField('work date')
    names = models.CharField(max_length=200)
    attendance = models.CharField(max_length=200)
    work = models.CharField(max_length=500)
    #IntegerField(default=0)
class Theme(models.Model):
    userid = models.CharField(max_length=200)
    color = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

class MhqEmpFeedback(models.Model):
    userid = models.CharField(max_length=200)
    touser=models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    status = models.CharField(max_length=200)
    edate = models.DateTimeField('entry date')





