from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from randrapi.models import River, Location, Rapid, River_Rapid
from rest_framework.decorators import action
from rest_framework import generics

class RiverView(ViewSet):
  
  def retrieve(self, request, pk):
    river = River.objects.get(pk=pk)
    serializer = RiverSerializer(river)
    return Response(serializer.data)
  
  def list(self, request):
    rivers= River.objects.all()
    
    location = request.query_params.get('location', None)
    if location is not None:
      rivers = rivers.filter(location_id=location)
      
    serializer = RiverSerializer(rivers, many = True)
    return Response(serializer.data)
  
  def create(self, request):
    
    location = Location.objects.get(pk=request.data["location"])
    rapids = request.data["rapids"]
    
    river = River.objects.create(
      name = request.data["name"],
      blurb = request.data["blurb"],
      photo = request.data["photo"],
      location = location,
    )
    for rapid in rapids:
      River_Rapid.objects.create(
        river = river,
        rapid = Rapid.objects.get(pk=rapid)
      )
      
    serializer = RiverSerializer(river)
    return Response(serializer.data)
  
  def update(self, request, pk):
    
    location = Location.objects.get(pk=request.data["location"])
    rapid = request.data["rapids"]
    
    river = River.objects.get(pk=pk)
    river.location = location
    river.name = request.data["name"]
    river.blurb = request.data["blurb"]
    river.photo = request.data["photo"]
    
    river.save()
    
    river_rapid = River.objects.filter(river)
    
    if river_rapid is not None:
      for rapid in river_rapid:
        rapid.delete()
        
    if rapid is not None:
      for rapid in rapid:
        Rapid.objects.create(river, river = River.get(pk = rapid))
        
    return Response(None, status=status.HTTP_204_NO_CONTENT)
      
  def destroy(self, request, pk):
    river = River.objects.get(pk=pk)
    river.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class RiverSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = River
    fields = ('id', 'name', 'blurb', 'photo', 'location')
    depth = 1
