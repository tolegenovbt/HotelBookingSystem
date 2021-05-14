import rest_framework.generics as generics
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from auth_.models import MainUser, Profile
from auth_.serializers import UserSerializer, ProfileSerializer


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def post_user(self, request):
        user = request.data
        queryset = MainUser.objects.create_user(email=user['email'], password=user['password'],
                                                first_name=user['first_name'], last_name=user['last_name'],
                                                role=user['role'])
        queryset.save()
        return Response(user, status=status.HTTP_201_CREATED)


class ProfileApiViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    parser_classes = [FormParser, JSONParser, MultiPartParser]
