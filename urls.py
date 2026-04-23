from django.contrib import admin
from django.urls import path
from accounts.views import login_view,user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('profile/', user_profile),
]