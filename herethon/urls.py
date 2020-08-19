from django.contrib import admin
from django.urls import path
from ootdapp import views
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = "main"),
    path('create/', views.create, name="create"),
    path('login/', account.views.login, name = 'login'),
    path('signup/', account.views.signup, name = 'signup'),
    path('logout/', account.views.logout, name ='logout'),
    path('detail/<int:pk>', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
