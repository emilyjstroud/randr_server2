from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from randrapi.models import Rapid
from rest_framework import generics

class RapidView(ViewSet):
  
  def retrieve (self, request, pk):
    rapid = Rapid.objects.get(pk=pk)
    serializer = RapidSerializer(rapid)
    return Response(serializer.data)
  
  def list(self, request,):
    rapids = Rapid.objects.all()
    serializer = RapidSerializer(rapids, many = True)
    return Response(serializer.data)
  
  def create(self, request):
    rapid = Rapid.objects.create(
      level = request.data["level"]
    )
    serializer = RapidSerializer(rapid)
    return Response(serializer.data)
  
  def update(self, request,pk):
    rapid = Rapid.objects.get(pk=pk)
    rapid.level = request.data["level"]
    rapid.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    rapid = Rapid.objects.get(pk=pk)
    rapid.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class RapidSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Rapid
      fields = ('level', 'id')
      depth = 1

class RiverRapidsView(generics.ListCreateAPIView):
  serializer_class = RapidSerializer
  def get_queryset(self):
    river_id = self.kwargs('river_id')
    return Rapid.objects.filter(river__id=river_id)
