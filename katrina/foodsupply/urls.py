from django.conf.urls import url
from . import views
app_name='foodsupply'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hub/$', views.hub, name='hub'),

    url(r'^household/$', views.household, name='household'),
    url(r'^view_household$', views.view_household, name='view_household'),
    url(r'^thankyou$', views.add_household, name='thankyou'),
    url(r'^report$', views.report, name='report'),
    url(r'^optimization$', views.optimization, name='optimization'),
]
