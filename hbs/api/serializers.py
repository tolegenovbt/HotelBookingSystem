from rest_framework import serializers
from .models import Hotel, Room, Reservation, RoomPhoto, Transaction, HotelPhoto, Comment


# class HotelierSerializer(serializers.ModelSerializer):
#     # gender = serializers.ChoiceField(choices=gender)
#     # phone_number = serializers.CharField(max_length=11)
#     # alternative_phone_number = serializers.CharField(max_length=11)
#     class Meta:
#         model = MainUser
#         fields = '__all__'
#
#
# class HotelierSerializerShort(serializers.ModelSerializer):
#     class Meta:
#         model = MainUser
#         fields = ['first_name', 'last_name', 'email', 'phone_number']


# class HotelSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField(read_only=True)
#     name = serializers.CharField(max_length=20)
#     hotelier = HotelierSerializerShort()
#     number_of_stars = serializers.IntegerField(default=1)
#     number_of_ratings = serializers.IntegerField(default=0)
#     rating = serializers.FloatField(default=0)
#     account_number = serializers.IntegerField()
#     address = serializers.CharField(max_length=200)
#     city = serializers.CharField(max_length=20)
#     phone_number = serializers.CharField()
#     yard = serializers.BooleanField()
#     pool = serializers.BooleanField()
#     gym = serializers.BooleanField()
#     wifi = serializers.BooleanField()
#     parking = serializers.BooleanField()
#     restaurant = serializers.BooleanField()
#
#     def create(self, validated_data):
#         hotel = Hotel.objects.create(
#             name=validated_data.get('name'),
#             number_of_stars=validated_data.get('number_of_stars'),
#             number_of_ratings=validated_data.get('number_of_ratings'),
#             rating=validated_data.get('rating'),
#             account_number=validated_data.get('account_number'),
#             address=validated_data.get('address'),
#             city=validated_data.get('city'),
#             phone_number=validated_data.get('phone_number'),
#             yard=validated_data.get('yard'),
#             pool=validated_data.get('pool'),
#             gym=validated_data.get('gym'),
#             wifi=validated_data.get('wifi'),
#             parking=validated_data.get('parking'),
#             restaurant=validated_data.get('restaurant'),
#             hotelier=validated_data.get('hotelier')
#         )
#         return hotel

# class UserSerializer(serializers.)


class HotelPhotoSerializer(serializers.ModelSerializer):
    hotel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = HotelPhoto
        fields = '__all__'


class BaseHotelSerializer(serializers.ModelSerializer):
    hotel_photos = HotelPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'
        abstract = True


class HotelSerializerShort(BaseHotelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'city', 'number_of_stars', 'hotel_photos']
        # fields = ['__all__']


class HotelSerializer(BaseHotelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomPhotoSerializer(serializers.Serializer):
    room_id = serializers.IntegerField(write_only=True)
    photo = serializers.ImageField()

    def create(self, validated_data):
        room_photo = RoomPhoto()
        room_photo.room_id = validated_data.get('room_id')
        room_photo.photo = validated_data.get('photo')
        room_photo.save()
        return room_photo

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


# class RoomPhotoSerializer(serializers.ModelSerializer):
#     room_id = serializers.IntegerField(write_only=True)
#
#     class Meta:
#         model = RoomPhoto
#         fields = ['photo', 'room_id']


class BaseRoomSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'cost', 'area', 'king_bed', 'queen_bed', 'tv', 'wifi', 'kitchen', 'extra_bed',
                  'room_photos']
        abstract = True


class RoomSerializer(BaseRoomSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomSerializerShort(BaseRoomSerializer):
    class Meta:
        model = Room
        fields = ['id', 'type', 'cost', 'area', 'room_photos']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ReservationSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'room', 'hotel', 'check_in', 'check_out']


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MainUser
#         fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    reservation_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Transaction
        # fields = ['reservation_id', 'reference_number']
        fields = '__all__'


class BaseCommentSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(write_only=True)
    hotel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        abstract = True


class CommentSerializer(BaseCommentSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# class CommentSerializerShort(BaseCommentSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', ]
# class ListSerializerFull(serializers.ModelSerializer):
#     class Meta:
#         model = List
#         fields = '__all__'
#
#
# class TaskSerializerShort(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'name', 'mark']
#
#
# class TaskSerializerFull(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'
