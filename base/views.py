from base.models import UninorteUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from base.serializers import UninorteUserSerializer, UsersSerializer, RegisterSerializer


@api_view(['POST'])
def register_view(request):

    """
    Register a new uninorte user with his string schedule

    """

    register_serializer = RegisterSerializer(data = request.data)

    if register_serializer.is_valid():

        user_data = register_serializer.save()

        return Response(
            user_data,
            status = status.HTTP_201_CREATED
        ) 
    else:
        return Response(
            register_serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def results_view(request):

    """
    Return all possible gaps according to the users and filters provided 
    
    """

    users_serializers = UsersSerializer(data = request.data)

    if users_serializers.is_valid():

        results = users_serializers.save()

        return Response(
            results,
            status = status.HTTP_200_OK
        ) 
    else:
        return Response(
            users_serializers.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class UninorteUserDetail(generics.RetrieveAPIView):

    queryset = UninorteUser.objects.all()
    serializer_class = UninorteUserSerializer
    name = "uninorteuser-detail"
    lookup_field = 'username'
    
  
