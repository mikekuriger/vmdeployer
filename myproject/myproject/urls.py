from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_vm, name='create_vm'),  
    path('create-vm/', views.create_vm, name='create_vm'),
    path('check_dns/', views.check_dns, name='check_dns'),
    path('deployments/', views.deployment_list, name='deployment_list'),
    path('deployments/<int:deployment_id>/', views.deployment_detail, name='deployment_detail'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
