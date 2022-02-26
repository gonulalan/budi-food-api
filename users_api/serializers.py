from rest_framework import serializers
from users_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    email = serializers.EmailField()
    first_name = serializers.CharField(min_length=2, max_length=255)
    last_name = serializers.CharField(min_length=2, max_length=255)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'identity_id', 'company_sign_name', 'company_official_name', 'company_address', 'company_city', 'company_district', 'company_neighborhood', 'company_tax_id', 'company_tax_administration',
                  'yemeksepeti_subscription', 'yemeksepeti_api_secret', 'yemeksepeti_api_key', 'getiryemek_subscription', 'getiryemek_api_secret', 'getiryemek_api_key', 'trendyolyemek_subscription', 'trendyolyemek_api_secret', 'trendyolyemek_api_key', 'mobile_application_subscription')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input-type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """Create and return new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            identity_id=validated_data['identity_id'],
            password=validated_data['password'],
            company_sign_name=validated_data['company_sign_name'],
            company_official_name=validated_data['company_official_name'],
            company_address=validated_data['company_address'],
            company_city=validated_data['company_city'],
            company_district=validated_data['company_district'],
            company_neighborhood=validated_data['company_neighborhood'],
            company_tax_id=validated_data['company_tax_id'],
            company_tax_administration=validated_data['company_tax_administration'],
            yemeksepeti_subscription=validated_data['yemeksepeti_subscription'],
            yemeksepeti_api_secret=validated_data['yemeksepeti_api_secret'],
            yemeksepeti_api_key=validated_data['yemeksepeti_api_key'],
            getiryemek_subscription=validated_data['getiryemek_subscription'],
            getiryemek_api_secret=validated_data['getiryemek_api_secret'],
            getiryemek_api_key=validated_data['getiryemek_api_key'],
            trendyolyemek_subscription=validated_data['trendyolyemek_subscription'],
            trendyolyemek_api_secret=validated_data['trendyolyemek_api_secret'],
            trendyolyemek_api_key=validated_data['trendyolyemek_api_key'],
            mobile_application_subscription=validated_data['mobile_application_subscription']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class UserFeedItemSerializer(serializers.ModelSerializer):
    """Serialize user feed items"""

    class Meta:
        model = models.UserFeedItem
        fields = ('id', 'user_profile', 'platform',
                  'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class PlatformSerializer(serializers.ModelSerializer):
    """Serializes platforms"""

    class Meta:
        model = models.Platform
        fields = ('id', 'platform_name', 'platform_short_name')
