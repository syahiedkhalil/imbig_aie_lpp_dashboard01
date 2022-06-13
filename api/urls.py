from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='LPP API',
        default_version='v1',
    )
)

urlpatterns = [
    path('lpp_auth/', include('dj_rest_auth.urls')),
    path('lpp_auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]