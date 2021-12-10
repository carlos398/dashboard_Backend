from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import UserProfile, UsersTests
from .serializers import UsersSerializer, UsersTestSerializer


@api_view(['GET', 'POST'])
def users_api_view(request):

    # users list
    if request.method == 'GET':
        # Queryset
        users = UserProfile.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    # Create User
    elif request.method == 'POST':
        users_serializer = UsersSerializer(data = request.data)
        #Validation
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status = status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    #QUERYSET 
    user = UserProfile.objects.filter(id=pk).first()

    #validation
    if user:

        #retrieve
        if request.method == 'GET':
            user_serializer = UsersSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)

        #UPDATE
        elif request.method == 'PUT':
            user_serializer = UsersSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response( user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


        #DELETE
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'User delete Succesfully'}, status = status.HTTP_200_OK)

    
    return Response({'message':'User not found'}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_detail_get(request, email=None):
    #QUERYSET 
    user = UserProfile.objects.filter(email=email).first()

    #validation
    if user:

        #retrieve
        if request.method == 'GET':
            user_serializer = UsersSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Test_api_view(request):

    if request.method == 'GET':
        usersTest = UsersTests.objects.all()
        testSerializer = UsersTestSerializer(usersTest, many = True)
        return Response(testSerializer.data, status = status.HTTP_200_OK)


    elif request.method == 'POST':
        testSerializer = UsersTestSerializer(data = request.data)

        if testSerializer.is_valid():
            testSerializer.save()
            return Response(testSerializer.data, status = status.HTTP_201_CREATED)
        return Response(testSerializer.errors, status = status.HTTP_400_BAD_REQUEST)