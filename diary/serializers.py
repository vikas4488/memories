from rest_framework import serializers
from diary.models import MhqEmp

class meq(serializers.ModelSerializer):
    class Meta:
        model = MhqEmp
        fields='__all__'