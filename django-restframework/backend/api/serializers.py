from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-detail-view',
        lookup_field='pk',
        )
    title= serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True) 
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self, obj):
    #     user = obj
    #     my_queryset = user.product_set.all()[:5]
    #     return UserProductInlineSerializer(my_queryset, many=True, context=self.context).data