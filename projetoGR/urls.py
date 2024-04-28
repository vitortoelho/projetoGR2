from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import CustomLoginView, home
from django.contrib.auth.views import LogoutView
from core import views


urlpatterns = [
    path('', CustomLoginView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', views.traduzir, name='traduzir'),
]

from django.contrib import admin
from django.urls import path
from core.views import CustomLoginView, home
