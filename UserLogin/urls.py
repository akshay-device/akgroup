
from django.contrib import admin
from django.urls import path
from cred import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login_user', views.login_user,name='login_user'),
    path('logout_user', views.logout_user,name='logout_user'),
    path('reg_user', views.reg_user,name='reg_user'),
    path('search', views.search,name='search'),
]
