from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import url, include
#from . import views
from .views import ReservationView


urlpatterns = [
    # /api/
    url(r'^$', login_required(ReservationView.as_view())),
    url(r'^login/$', ReservationView.loginView, name='loginView'),
    url(r'^logout/$', ReservationView.logout_view, name='logout_view'),
    #url(r'^edit', views.list, name='list'),
    #url(r'^seat', views.seat, name='seat'),
    url('^(?P<date>\d{4}-\d{2}-\d{2})/$', login_required(ReservationView.as_view())),
    path('remove/<int:id>', ReservationView.remove),
    #path('<int:date>/edit', views.list),
]
