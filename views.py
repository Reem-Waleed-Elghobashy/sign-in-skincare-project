from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
   
    if len(password)< 8:
        return Response({"error":"password must be at least 8 characters long"},status=400)
    user = authenticate(username=username, password=password)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key, "message":"Login Successful!"}, status=200)
    else:
        return Response({"error": "Invalid email or password"}, status=400)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    return Response({"message": "Welcome to your protected skin care profile!"})