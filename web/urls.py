from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^submit/student/$',views.submit_student,name='submit_student')
]
