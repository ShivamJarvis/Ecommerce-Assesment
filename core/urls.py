from django.urls import path,re_path
from core import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce Assesment API",
      default_version='v1',
      description="Ecommerce Assesment",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

app_name = "core"

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('product-create',views.ProductCreateView.as_view()),
    path('product-list',views.ProductListView.as_view()),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view()),
    path('product-delete/<int:pk>',views.ProductDeleteView.as_view()),
]