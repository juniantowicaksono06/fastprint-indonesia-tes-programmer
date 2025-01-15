# serializers.py
from rest_framework import serializers
from .models import Produk, Status, Kategori

class ProdukSerializer(serializers.ModelSerializer):
    kategori = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), source='status')
    kategori_id = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all(), source='kategori')

    class Meta:
        model = Produk
        fields = ['id', 'nama_produk', 'harga', 'kategori_id', 'kategori', 'status_id', 'status']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'nama_status']

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id', 'nama_kategori']