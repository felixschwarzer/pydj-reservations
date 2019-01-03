from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # /api/
    url(r'^$', views.list, name='list'),
    url(r'^login/$', views.loginView, name='loginView'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    #url(r'^edit', views.list, name='list'),
    #url(r'^seat', views.seat, name='seat'),
    url('^(?P<date>\d{4}-\d{2}-\d{2})/$', views.list, name="list"),
    path('remove/<int:id>', views.remove),
    #path('<int:date>/edit', views.list),
]
