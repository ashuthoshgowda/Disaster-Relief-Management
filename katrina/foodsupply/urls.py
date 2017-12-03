from django.conf.urls import url
from . import views
app_name='foodsupply'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hub/$', views.hub, name='hub'),

    url(r'^household/$', views.household_main, name='household'),
    url(r'^view_household$', views.view_household, name='view_household'),
    url(r'^thankyou$', views.add_household, name='thankyou'),
    url(r'^report1$', views.report_1, name='report1'),
    url(r'^report2$', views.report_2, name='report2'),
    url(r'^report3$', views.report_3, name='report3'),
    url(r'^optimization$', views.optimization, name='optimization'),
]
