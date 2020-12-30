from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.serializers import UsersSerializer, RegisterSerializer

@api_view(['POST'])
def register_view(request):

    register_serializer = RegisterSerializer(data = request.data)

    if register_serializer.is_valid():

        user_data = register_serializer.save()

        return Response(
            user_data,
            status = status.HTTP_200_OK
        ) 
    else:
        return Response(
            register_serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
def results_view(request):

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

  