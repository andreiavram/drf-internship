from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

import todolist.urls as todo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todo/', include(todo_urls, namespace="todo")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
