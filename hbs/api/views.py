from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import DetailView
from datetime import datetime, timedelta
from .models import Hotel, Room, Reservation, RoomPhoto, Transaction, HotelPhoto, Comment,\
    star_numbers
from .serializers import HotelSerializer, HotelSerializerShort, HotelPhotoSerializer, \
    TransactionSerializer, CommentSerializer, RoomSerializerShort, RoomPhotoSerializer, ReservationSerializer, \
    RoomSerializer, ReservationSerializerShort


# Create your views here.


class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelSerializerShort
        elif self.action == 'retrieve':
            return HotelSerializer
        elif self.action == 'create':
            return HotelSerializer
        elif self.action == 'update':
            return HotelSerializer
        elif self.action == 'destroy':
            return HotelSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RoomSerializerShort

    def get_serializer_class(self):
        # if self.action == 'list':
        #     return RoomSerializerShort
        # elif self.action == 'retrieve':
        #     return RoomSerializer
        if self.action == 'create':
            return RoomSerializer
        elif self.action == 'update':
            return RoomSerializer
        elif self.action == 'destroy':
            return RoomSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def rooms_by_hotel(self, request, pk):
        queryset = Room.objects.filter(hotel=pk)
        serializer = RoomSerializerShort(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def room_details_by_hotel(self, request, pk, rk):
        queryset = Room.objects.filter(id=rk)
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)


class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ReservationSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ReservationSerializerShort
        elif self.action == 'retrieve':
            return ReservationSerializer
        elif self.action == 'create':
            return ReservationSerializer
        elif self.action == 'update':
            return ReservationSerializer
        elif self.action == 'destroy':
            return ReservationSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def reservations_by_hotel(self, request, pk):
        queryset = Reservation.objects.filter(hotel=pk)
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)


class RoomPhotoListApiView(generics.ListCreateAPIView):
    # queryset = RoomPhoto.objects.filter()
    serializer_class = RoomPhotoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser, JSONParser, MultiPartParser]

    def get_queryset(self):
        queryset = RoomPhoto.objects.all()
        return queryset
    # @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    # def reservations_by_room(self, request, pk):
    #     queryset1 = Hotel.objects.get()
    #     queryset = Reservation.objects.filter(room=pk)
    #     serializer = RoomSerializer(queryset, many=True)
    #     return Response(serializer.data)

# def reserve(request, pk):
#     try:
#         queryset = Reservation.objects.filter(room=pk)
#     except Reservation.DoesNotExist as e:
#         return Response({'error': str(e)})
#
#     if request.method == 'PUT':
#         serializer = ReservationSerializer