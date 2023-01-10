from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductCategorySerializer
from django.http.response import StreamingHttpResponse

from .models import Product

# Create your views here.

@api_view(["GET", "POST"])
def index(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    

@api_view(["GET"])
def get_product(request, pk: int):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_product_category(request, pk: int):
    product = Product.objects.get(pk=pk)
    category = product.productcategory_set.get(pk=1)
    serializer = ProductCategorySerializer(category)
    return Response(serializer.data)
    
    


@api_view(["GET"])
def get_image_for(request, pk: int):
    """
    Gets the first image for product with pk
    """
    product = Product.objects.get(pk=pk)
    first_image = product.image_set.get(pk=1)
    # return Response(first_image.image.url)
    return StreamingHttpResponse(first_image.image, content_type="image/jpeg")
