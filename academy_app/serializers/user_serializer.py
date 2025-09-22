from rest_framework import serializers
from academy_app.models import user , category, music, car, laptop, mobile, Contact,Inquiry

# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"   # you can also list specific fields


# custom serializer for registration
class registerSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    country = serializers.CharField()
    is_instructor = serializers.BooleanField()

    def validate(self, data):
        if user.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError("email already exist")
        return data
    
    def create(self, validated_data):
        print("---- data come from views.py ----",validated_data)
        print("---- data come from views.py ----",validated_data['name'])
        names = validated_data['name']
        email = validated_data["email"]
        password = validated_data['password']
        country = validated_data['country']
        is_instructor = validated_data['is_instructor']

        # password = password+"sfsdfsdf"
        
        user_model = user()
        # user_model.name = validated_data['name']
        user_model.name = names
        user_model.email = email
        user_model.password = password
        user_model.country = country
        user_model.is_instructor = is_instructor
        user_model.save()
        return user_model


# Custom Login Serializer for Login Page
class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()





# category
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = "__all__"


# Music 
class musicSerializer(serializers.ModelSerializer):
    class Meta:
        model = music
        fields = "__all__"


# Car
class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = "__all__"


# Laptop
class laptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = laptop
        fields = "__all__"


# Mobile
class mobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = "__all__"


# ---------------------------------------------------- --------------------------------------------

# Inquiry
class  InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"


    # Field-level validation for phone_number
    def validate_phone(self, value):
        # Check: phone number 10 digits ka hi ho
        if len(str(value)) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")

        # Check: sirf digits (int me aayega but agar string aaya to bhi safe ho)
        if not str(value).isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")

        return value


# Contact Us 
class  ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


    # Field-level validation for phone_number
    def validate_phone_number(self, value):
        # Check: phone number 10 digits ka hi ho
        if len(str(value)) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")

        # Check: sirf digits (int me aayega but agar string aaya to bhi safe ho)
        if not str(value).isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")

        return value