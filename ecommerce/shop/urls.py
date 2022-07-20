
from django.urls import path
from shop.views import  detail,index,login,authlogin,logout_user
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>',detail, name='detail'),
    path('login', login, name='login'),
    path('authlogin', authlogin, name='authlogin'),
    path('logout', logout_user, name='logout'),



              
]
urlpatterns += staticfiles_urlpatterns()