from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('detail/', views.register, name="detail"),
    path('registrationpage/', views.registerPage, name="registrationpage"),
    path('login/', views.loginUser, name="login"),
    path('loginpage/', TemplateView.as_view(template_name="registration/login.html")),
    path('account/logout/', views.logout, name="logout"),
    

]