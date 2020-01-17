from tastypie.resources import ModelResource
from diary.models import MhqEmp


class EntryResource(ModelResource):
    class Meta:
        queryset = MhqEmp.objects.all()
        resource_name = 'entry'
        excludes = [ 'password']