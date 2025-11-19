from django.urls import path, include
from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    CityListAPIView, CityDetailAPIView,
                    HotelListAPIView,
                    HotelDetailAPIView,
                    RoomListAPIView, RoomDetailAPIView,
                    ReviewCreateAPIView, ReviewEditAPIView,
                    BookingViewSet, HotelViewSet, RoomViewSet,
                    RegisterView, CustomLoginView, LogoutView)
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'hotel_create', HotelViewSet)
router.register(r'room_create', RoomViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('cities/', CityListAPIView.as_view(), name='city_list'),
    path('cities/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('hotels/', HotelListAPIView.as_view(), name='hotels_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]