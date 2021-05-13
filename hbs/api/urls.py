from django.contrib import admin
from django.urls import path, include
from .views import HotelsViewSet, RoomsViewSet, ReservationsViewSet, RoomPhotoListApiView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    # path('auth_', include('auth_.urls'))
    path('hotels/', HotelsViewSet.as_view({'get': 'list',
                                           'post': 'create'})),
    path('hotels/<int:pk>/', HotelsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'post': 'create',
                                                    'put': 'update'})),
    path('hotels/<int:pk>/rooms/', RoomsViewSet.as_view({'get': 'rooms_by_hotel',
                                                         'post': 'create',
                                                         'delete': 'destroy',
                                                         'put': 'update'})),
    path('hotels/<int:pk>/rooms/<int:rk>/', RoomsViewSet.as_view({'get': 'room_details_by_hotel'})),
    # path('hotels/<int:pk>/rooms/<int:rk>/reservation/', RoomsViewSet.as_view({'get': 'room_details_by_hotel'})),
    # path('hotels/<int:pk>/reservations/', ReservationsViewSet.as_view({'get': 'list',
    #                                                                    'post': 'create}))
    path('hotels/<int:pk>/reservations/', ReservationsViewSet.as_view({'get': 'reservations_by_hotel'})),
    path('roomphotos/', RoomPhotoListApiView.as_view()),
]