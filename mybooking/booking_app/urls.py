from django.urls import path, include
from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    CityListAPIView, CityDetailAPIView,
                    HotelListAPIView,
                    HotelDetailAPIView,
                    RoomListAPIView, RoomDetailAPIView, ReviewViewSet,
                    BookingViewSet)
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('cities/', CityListAPIView.as_view(), name='city_list'),
    path('cities/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('hotels/', HotelListAPIView.as_view(), name='hotels_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail')
]