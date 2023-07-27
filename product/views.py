
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import authentication,permissions
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    permission_classes = [IsAdminOrReadOnly]



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    permission_classes = [IsAdminOrReadOnly]

    # def get_permissions(self):
        
    #     if self.action == 'list':
    #         return [AllowAny()]
    #     else:
    #         return super().get_permissions()
        
    # def get_permissions(self):
        
    #     if self.action == 'create':
    #         return [IsAdminUser()]
    #     else:
    #         return super().get_permissions()
        
