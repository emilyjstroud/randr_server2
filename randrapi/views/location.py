from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from randrapi.models import Location

class LocationView(ViewSet):
  
  def retrieve(self, request, pk):
    
      location = Location.objects.get(pk=pk)
      serializer = LocationSerializer(location)
      return Response(serializer.data)
    
  def list(self, request):
    
    locations = Location.objects.all()
    
    uid_query = request.query_params.get('uid', None)
    if uid_query is not None:
      locations = locations.filter(uid_query)
    serializer = LocationSerializer(locations, many = True)
    return Response(serializer.data)
  
  def create(self, request):
    
    location = Location.objects.create(
      name = request.data['name'],
      blurb = request.data['blurb'],
      photo = request.data['photo'],
      uid = request.data['uid']
    )
    serializer = LocationSerializer(location)
    return Response(serializer.data)
  
  def update(self, request, pk):
    
    location = Location.objects.get(pk=pk)
    
    location.name = request.data['name']
    location.blurb = request.data['blurb']
    location.photo = request.data['photo']
    location.uid = request.data['uid']
    location.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
      location = Location.objects.get(pk=pk)
      location.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class LocationSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Location
    fields = ('id', 'name', 'blurb', 'photo', 'uid')
    depth = 1
    
    