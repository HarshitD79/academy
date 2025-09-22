from django.contrib import admin
from django.urls import path,include
from academy_app.views import UserViewSet, musicViewSet, carViewSet, laptopViewSet, mobileViewSet, registerViewSet, loginAPIView, ContactViewSet,InquiryViewSet, categoryViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'music', musicViewSet)
router.register(r'car', carViewSet)
router.register(r'laptop', laptopViewSet)
router.register(r'mobile', mobileViewSet)
router.register(r'Contact',ContactViewSet)
router.register(r'inquiry',InquiryViewSet)
router.register(r'category',categoryViewSet)



urlpatterns = [
   path('', include(router.urls)),
   path('signup',registerViewSet.as_view()),
   path('login',loginAPIView.as_view())
]