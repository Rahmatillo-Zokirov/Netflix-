from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class IndexAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "xabar": "Salom dunyo",
                "framework": "django rest framework"
            }
        )

    def post(self,request):
        pass

    def delete(self):
        pass


class AktyorlarAPIView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data, status=200)


    def post(self, request):
        serializers = AktyorSerializer(data=request.data)
        if serializers.is_valid():
            data = serializers.data
            Aktyor.objects.create(
                ism=data.get("ism"),
                davlat=data.get("davlat"),
                jins=data.get("jins"),
                t_yil=data.get("t_yil"),
            )
            return Response("Aktyor yaratildi", status=201)
        return Response(serializers.errors, status=400)


class AktyorTahrirlashAPIView(APIView):
    def put(self, request, pk):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            aktyor = Aktyor.objects.filter(id=pk).update(
                ism=serializer.data.get("ism"),
                davlat=serializer.data.get("davlat"),
                jins=serializer.data.get("jins"),
                t_yil=serializer.data.get("t_yil"),
            )
            return Response(
                {
                    "success": True,
                    "update_data": serializer.data,
                }, status=200
            )
        return Response(serializer.errors, status=400)

class AktyorDetailAPIView(APIView):
    def get(self, request, pk):
        aktyor = get_object_or_404(Aktyor, pk=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data, status=200)


class AktyordeleteAPIView(APIView):
    def delete(self, request, pk):
        aktyor = get_object_or_404(Aktyor, pk=pk)
        aktyor.delete()
        return Response(status=204)

class TarifTahrirlashAPIView(APIView):
    def put(self, request, pk):
        serializer = TarifSerializer(data=request.data)
        if serializer.is_valid():
            tarif = Tarif.objects.filter(id=pk).update(
                nom=serializer.data.get("nom"),
                narx=serializer.data.get("narx"),
                davomiylik=serializer.data.get("davomiylik"),
            )
            return Response(
                {
                    "success": True,
                    "update_data": serializer.data,
                }, status=200
            )
        return Response(serializer.errors, status=400)

class TarifdeleteAPIView(APIView):
    def delete(self, request, pk):
        tarif = get_object_or_404(Tarif, pk=pk)
        tarif.delete()
        return Response(status=204)

class TarifDetailAPIView(APIView):
    def get(self, request, pk):
        tarif = get_object_or_404(Tarif, pk=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data, status=200)

class TariflarAPIView(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(tariflar, many=True)
        return Response(serializer.data, status=200)


    def post(self, request):
        serializers = TarifSerializer(data=request.data)
        if serializers.is_valid():
            data = serializers.data
            Tarif.objects.create(
                nom=data.get("nom"),
                narx=data.get("narx"),
                davomiylik=data.get("davomiylik"),
            )
            return Response("Tarif yaratildi", status=201)
        return Response(serializers.errors, status=400)