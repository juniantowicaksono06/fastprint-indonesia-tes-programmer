# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produk, Status, Kategori
from .serializers import ProdukSerializer, StatusSerializer, KategoriSerializer
from rest_framework.pagination import PageNumberPagination

class ProdukList(APIView):
    def get(self, request, format=None):
        status_id = request.query_params.get('status_id', None)
        if status_id:
            produk = Produk.objects.filter(status_id=status_id)
        else:
            produk = Produk.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = 10  # Jumlah item per halaman
        result_page = paginator.paginate_queryset(produk, request)

        serializer = ProdukSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class ProdukCreate(APIView):
    def post(self, request, format=None):
        serializer = ProdukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdukDetail(APIView):
    def get_object(self, pk):
        try:
            return Produk.objects.get(pk=pk)
        except Produk.DoesNotExist:
            return None
    
    def put(self, request, pk, format=None):
        produk = self.get_object(pk)
        if produk is None:
            return Response({"error": "Produk tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)
        print(request.data)
        serializer = ProdukSerializer(produk, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        produk = self.get_object(pk)
        if produk is None:
            return Response({"error": "Produk tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)
        
        produk.delete()
        return Response({"message": "Produk berhasil dihapus"}, status=status.HTTP_204_NO_CONTENT)
    
class StatusList(APIView):
    def get(self, request, format=None):
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return Response(serializer.data)
    
class KategoriList(APIView):
    def get(self, request, format=None):
        status = Kategori.objects.all()
        serializer = KategoriSerializer(status, many=True)
        return Response(serializer.data)