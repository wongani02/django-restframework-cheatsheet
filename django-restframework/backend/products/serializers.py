from rest_framework import serializers
from .models import *
from rest_framework.reverse import reverse
from api.models import Blog
from .validators import validate_title, validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='api-detail-view',
        lookup_field='pk',
        )

    ''' using custom validations'''    
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # email = serializers.EmailField(source='user.email', write_only = True) #link email to the users email
    my_user_data = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['owner','url', 'edit_url', 'pk', 'title', 'content', 'price', 'sale_price', 'my_discount', 'my_user_data']
        
    ''' overiding the custom serializer create and update methods'''
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data) #what the defsault method does
    #     # email =  validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    '''custom validator'''
    # def validate_title(self, value):
    #     request = self.context.get('request)
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'the title {value} is already a product name')
    #     return value

    ''' get user data to related fields'''
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username, 
            "email" : obj.user.email,
        }

    def get_edit_url(self, obj):
        # return f'/api/products/{obj.pk}/'
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('api-update-view', kwargs={'pk': obj.pk}, request=request) 

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
 

class BlogSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog-detail-view',
        lookup_field='pk',
        )
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'author', 'url']