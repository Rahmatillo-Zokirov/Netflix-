from rest_framework import serializers


class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)
    ism = serializers.CharField(max_length=255)
    davlat = serializers.CharField(max_length=255)
    jins = serializers.CharField(max_length=10)
    t_yil = serializers.DateField(required=False)


class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)
    nom = serializers.CharField(max_length=255)
    narx = serializers.FloatField()
    davomiylik = serializers.CharField(max_length=50)


