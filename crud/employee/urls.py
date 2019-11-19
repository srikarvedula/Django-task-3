from django.contrib import admin
from django.urls import path
from employee import views
from login import views
urlpatterns = [
    path('', views.home,name="home"),
    path('admin/', admin.site.urls),
    path('login/home/emp', views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]