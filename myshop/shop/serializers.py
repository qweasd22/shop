from rest_framework import serializers


from .models import Product, Profile, User

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category','image']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','id','email']

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()








    
