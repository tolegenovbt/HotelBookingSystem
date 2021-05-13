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
class HotelSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'city', 'number_of_stars']
        # fields = ['__all__']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomPhotoSerializer(serializers.ModelSerializer):
    room_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RoomPhoto
        fields = ['photo', 'room_id']


class RoomSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'cost', 'area', 'king_bed', 'queen_bed', 'tv', 'wifi', 'kitchen', 'extra_bed',
                  'room_photos']


class RoomSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'type', 'cost', 'area']


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'


class ReservationSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'room', 'check_in', 'check_out']


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MainUser
#         fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
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
