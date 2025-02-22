"""
URL configuration for foodapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Food API",
        default_version="v1",
        description="Food APP description",
        terms_of_service="",
        contact=openapi.Contact(email="risenboy23@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # noqa
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("backend.user.urls")),
    path("api/store/", include("backend.store.urls")),
    path("api/items/", include("backend.item.urls")),
    path("api/cart/", include("backend.cart.urls")),
    path("api/order/", include("backend.order.urls")),
]


doc_patterns = [
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="api-docs",
    ),
    path(
        "api/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc",
    ),
]

urlpatterns += doc_patterns

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT,
#     )
