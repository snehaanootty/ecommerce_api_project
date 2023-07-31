from rest_framework import serializers
from product.models import Product,Category,CartProduct,Cart



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_category(self, obj):
        return obj.category.name if obj.category else None
    
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

