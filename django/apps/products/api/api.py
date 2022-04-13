import random
from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.products.models import *
from .serializers import *
from apps.products.api.producer import publish


class ProductViewSet(viewsets.GenericViewSet):
    model = Product
    serializer_class = ProductSerializer
    list_serializer_class = ProductSerializer
    queryset = None

    def get_object(self, pk=None):
        return self.model.objects.filter(id=pk).first()

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        products = self.get_queryset()
        if len(list(products)) > 0:
            products_serializer = self.list_serializer_class(products, many=True)
            content = {'message': 'success', 'products': products_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'products': 'Products not fund.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        product_serializer = self.serializer_class(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            content = {'message': 'success', 'product': product_serializer.data}
            publish('product_created', product_serializer.data)
            return Response(content, status=status.HTTP_201_CREATED)
        content = {'message': 'errors', 'product': product_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = self.get_object(pk)
        if product is not None:
            product_serializer = self.serializer_class(product)
            content = {'message': "success", 'product': product_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'product': 'Product not fund.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        product = self.get_object(pk)
        if product is not None:
            product_serializer = self.serializer_class(product, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                content = {'message': 'success', 'product': product_serializer.data}
                publish('product_updated', product_serializer.data)
                return Response(content, status=status.HTTP_200_OK)
            content = {'message': "errors", 'product': product_serializer.errors}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {'message': 'errors', 'product': 'Product not fund.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            product_destroy = self.model.objects.filter(id=pk).first()
            if product_destroy is not None:
                product_destroy.delete()
                content = {'message': 'success', 'product': 'Product deleted.'}
                publish('product_deleted', pk)
                return Response(content, status=status.HTTP_200_OK)
            content = {'message': 'errors', 'product': 'Product not fund.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except:
            content = {
                'message': "errors",
                'product': "Paso algo xD",
            }
            return Response(content, status=status.HTTP_409_CONFLICT)


class UserViewSet(viewsets.GenericViewSet):
    model = User

    def list(self, request):
        users = self.model.objects.all()
        if len(list(users)) > 0:
            user = random.choice(users)
            content = {'message': 'success', 'id': user.id}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'users': 'Users not fund.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
