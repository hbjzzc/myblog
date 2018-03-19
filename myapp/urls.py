from django.conf.urls import include, url
from myapp import views

urlpatterns = [

    url(r'^$', views.Index.as_view(), name='index'),

    url(r'^publish/$', views.Publish.as_view(), name='publish'),

    url(r'^artical/$', views.Artical.as_view(), name='artical'),

    url(r'^newArtical$', views.NewArtical.as_view(), name='newArtical'),

    url(r'^register/$', views.RegisterView.as_view(), name='register'),

    url(r'^login/$', views.LoginView.as_view(), name='login')
]
