from django.urls import path
from accounts import views

urlpatterns = [
	path('', views.home, name='home'),
	path('signup', views.signup, name='signup'),
	path('signin', views.signin, name='signin'),
	path('logout', views.signout, name='logout'),
	path('data', views.CompleteSignup, name='CompleteSignup'),
]