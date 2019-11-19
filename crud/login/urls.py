from django.urls import path
from login import views
from . import views
from employee import views,urls


urlpatterns = [
    path('home/', views.home,name="home"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('emp', views.emp,name="emp"),
    path('show/', views.show,name="show"),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),

]