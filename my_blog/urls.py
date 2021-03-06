
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog_app.urls')),
    path('account/',include('login_app.urls')),
    path('',views.index,name='index')
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
