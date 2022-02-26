from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users_api import serializers
from rest_framework import viewsets
from users_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from users_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserApiView(APIView):
    """API View for the operations to manage users"""
    serializer_class = serializers.HelloSerializer

    def get(self, requset, format=None):
        """Returns a list of features of this APIView"""
        description = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello from UserApiView', 'description': description})

    def post(self, request):
        """Create a with given details"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            email = serializer.validated_data.get('email')
            message = f'Hello {first_name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class UserViewSet(viewsets.ViewSet):
    """View set for the operations to manage users"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a list of users"""
        user_list = [
            'ismail', 'bulut', 'gönülalan',
        ]

        return Response({'message': 'success', 'users': user_list})

    def create(self, request):
        """Create a new user"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            email = serializer.validated_data.get('email')
            message = f'Hello from viewset {first_name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': f'GET {pk}'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'first_name')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
