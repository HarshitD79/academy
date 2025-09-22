from django.shortcuts import render
from academy_app.serializers.user_serializer import UserSerializer , categorySerializer, musicSerializer, carSerializer, laptopSerializer, mobileSerializer, registerSerializer, loginSerializer, ContactSerializer, InquirySerializer
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import user, category, music, car, laptop, mobile,Contact, Inquiry
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()       
    serializer_class = UserSerializer   
    
# createAPIView (generic view)
class registerViewSet(CreateAPIView):
    serializer_class = registerSerializer

    def create(self, request, *args, **kwargs):
        print("---- Data came from postman ----",request.data)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()

        return Response(
            {"message": "User registered! successfully"},
            status=status.HTTP_201_CREATED)

# APIView method for login page
class loginAPIView(APIView):
    def post(self,request):
        serializer = loginSerializer(data = request.data)
        # print(request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            userData = user.objects.get(email= email)
        except user.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        if userData.password!=password:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"meassage": 'login Successfully'}, status=status.HTTP_200_OK)
    
# category CRUD
class categoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = categorySerializer


# music
class musicViewSet(viewsets.ModelViewSet):
    queryset = music.objects.all()
    serializer_class = musicSerializer


# car
class carViewSet(viewsets.ModelViewSet):
    queryset = car.objects.all()
    serializer_class = carSerializer


# Laptop
class laptopViewSet(viewsets.ModelViewSet):
    queryset = laptop.objects.all()
    serializer_class = laptopSerializer


# Mobile
class mobileViewSet(viewsets.ModelViewSet):
    queryset = mobile.objects.all()
    serializer_class = mobileSerializer

# ContactUs
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# ------------------------------------------------- ---------------------------------
# Inquiry 
class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer