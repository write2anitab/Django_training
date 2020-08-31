from django.conf.urls import url
from myapp import views

app_name = 'myapp'

urlpatterns = [
    url(r'^user_auth/$',views.UserAuthView.as_view(),name='UserAuthView'),
    url(r'^roles/$',views.RoleView.as_view(),name='RoleView'),
    url(r'^drf_roles/$',views.RoleDRFView.as_view(),name='RoleDRFView'),
    url(r'^drf_users/$',views.UserDRFView.as_view(),name='UserDRFView'),
    url(r'^drf_users/(?P<pk>[\d]+)/$',views.UserDRFView.as_view(),name='UserDRFView'),
]
