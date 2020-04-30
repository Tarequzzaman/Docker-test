from django.conf.urls import url,include




from .views import  news

urlpatterns=[
url(r'^news/', news),
]