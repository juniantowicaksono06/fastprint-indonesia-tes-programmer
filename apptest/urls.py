from django.urls import path
from . import api
from . import views

urlpatterns = [
    path('api/produk/', api.ProdukList.as_view(), name='produk-list-api'),
    path('api/produk/<int:pk>/', api.ProdukDetail.as_view(), name='produk-detail-api'),
    path('api/produk/create/', api.ProdukCreate.as_view(), name='produk-create-api'),
    path('api/status/', api.StatusList.as_view(), name='status-list-api'),
    path('api/kategori/', api.KategoriList.as_view(), name='kategori-list-api'),
    path('', views.Produk, name='produk'),
]