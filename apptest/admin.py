from django.contrib import admin
from .models import Kategori, Status, Produk

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_kategori')  # Use 'id' instead of 'id_kategori'

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_status')  # Use 'id' instead of 'id_status'

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_produk', 'harga', 'kategori', 'status')  # Use 'id' instead of 'id_produk'