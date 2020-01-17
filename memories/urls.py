from django.conf.urls import url, include
from diary.api import EntryResource
from django.contrib import admin
from django.urls import include, path
entry_resource = EntryResource()
urlpatterns = [
    path('',include('diary.urls')),
    path('admin/', admin.site.urls),
    url(r'^api/', include(entry_resource.urls)),
]
