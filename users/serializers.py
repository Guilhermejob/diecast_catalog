from pickletools import read_long1
from rest_framework import serializers

class UsersSerializer(serializers.Serializer):
    id_user = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    email = serializers.CharField()
    profile_img = serializers.CharField()
    registered_diecasts = serializers.IntegerField()
    birth_date = serializers.DateTimeField()
    created_at = serializers.DateTimeField()    