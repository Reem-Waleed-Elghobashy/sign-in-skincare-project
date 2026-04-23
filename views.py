from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
   
    if len(password)< 8:
        return Response({"error":"password must be at least 8 characters long"},status=400)
    user = authenticate(username=username, password=password)
    
    if user is not None:
        return Response({"message": "Login Successful!"}, status=200)
    else:
        return Response({"error": "Invalid email or password"}, status=400)
