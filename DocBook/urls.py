from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Docbook Api",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('token-auth', obtain_jwt_token),
    # path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('api/', include('articles.api.urls')),
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    ]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root = settings.MEDIA_ROOT)