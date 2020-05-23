from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializer import CompanySerializer, ProductSerializer
from .models import Company, Product


# Create your views here.
class ListCompany(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (AllowAny, )
    filterset_fields = ['name', ]

    def get(self, request):
        return Response(self.queryset.values('id', 'name'))

    def post(self, request):
        return self.create(request)


class CompanyDetail(generics.RetrieveAPIView):
    def get(self, request, cid):
        return Response()


class ListProduct(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('company')
    permission_classes = (AllowAny,)
    filterset_fields = ['name', 'price']

    def post(self, request):
        return self.create(request)


class ProductDetail(generics.RetrieveAPIView):
    def get(self, request, pid):
        return Response()
