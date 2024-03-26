from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .models import User
from .serializers import UserSerializer, UserPassChangeSerializer


class UserCreate(generics.CreateAPIView):
    """
    API endpoint to create a new user.

    Attributes:
        serializer_class (Serializer): Serializer class used for serializing/deserializing user creation data.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(APIView):
    """
    API endpoint to retrieve details of a specific user.

    Methods:
        get_object: Retrieves the user instance by primary key.
        get: Retrieves the serialized data of the user.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class UserProfileRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve and update the profile of the authenticated user.

    Attributes:
        queryset (QuerySet): Queryset representing all users.
        serializer_class (Serializer): Serializer class used for serializing/deserializing user data.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    """
    API endpoint to change the password of the authenticated user.

    Attributes:
        queryset (QuerySet): Queryset representing all users.
        serializer_class (Serializer): Serializer class used for serializing/deserializing user password change data.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    queryset = User.objects.all()
    serializer_class = UserPassChangeSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminUserDetailView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to retrieve and update the details of a specific user by the admin.

    Attributes:
        queryset (QuerySet): Queryset representing all users.
        serializer_class (Serializer): Serializer class used for serializing/deserializing user data.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class AdminChangeUserStatusView(APIView):
    """
    API endpoint to change the status of a user by the admin.

    Attributes:
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = not user.is_active
        user.save()
        return Response({"message": "User status updated successfully."})
