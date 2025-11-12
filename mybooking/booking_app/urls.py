from django.urls import path, include
from .views import (CountryViewSet, UserProfileViewSet,
                    CityListAPIView, CityDetailAPIView,
                    ServicesViewSet, HotelListAPIView,
                    HotelDetailAPIView, HotelImageViewSet,
                    RoomViewSet, RoomImageViewSet, ReviewViewSet,
                    BookingViewSet)
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'countries', CountryViewSet)
router.register(r'users', UserProfileViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'hotel_images', HotelImageViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'room_images', RoomImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = [
    path('cities/', CityListAPIView.as_view(), name='city_list'),
    path('cities/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('hotels/', HotelListAPIView.as_view(), name='hotels_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),

]