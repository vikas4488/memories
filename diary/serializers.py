from rest_framework import serializers
from .models import MhqEmp,MhqEmpData as ed,Theme,MhqEmpFeedback as mef

class meq(serializers.ModelSerializer):
    color = serializers.SerializerMethodField('themeColor')
    def themeColor(self,foo):
        return Theme.objects.get(pk=foo.theme).color 
    class Meta:
        model = MhqEmp
        fields = '__all__'
class tme(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields='__all__'


class med(serializers.ModelSerializer):
    class Meta:
        model = ed
        fields='__all__'