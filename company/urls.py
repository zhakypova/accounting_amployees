
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from emp.views import PositionViewSet, EmployeesViewSet


emp_router = DefaultRouter()
emp_router.register('position', PositionViewSet)
emp_router.register('employees', EmployeesViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Compsny API",
      default_version='v0.1',
      description="API для учета сотрудников и их должностей",
      terms_of_service="-",
      contact=openapi.Contact(email="zulyawayne@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/account/', include('account.urls')),
    path('', include(emp_router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui')
]
