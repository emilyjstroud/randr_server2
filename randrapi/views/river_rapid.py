from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from randrapi.models import River_Rapid, River, Rapid

class RiverRapidView(ViewSet):
  
  def retrieve(self, request, pk):
    river_rapid = River_Rapid.objects.get(pk=pk)
    # river = River.objects.get(pk=pk)

    serializer = RiverRapidSerializer(river_rapid)
    print('retrieve')
    return Response(serializer.data)
  
  def list(self, request):
    river_rapids = River_Rapid.objects.all()
    # new_river_rapids = river_rapids.filter(river_id = river)
    # new_river_rapids = River_Rapid.objects.all()

    # new_river_rapids = request.query_params.get = ('river_rapids', None)
    # if new_river_rapids is not None:
    # new_river_rapids = river_rapids.filter(river_id = river)

    # if new_river_rapids is not None:
    #  river = river.filter(river = river)
    
    river = request.query_params.get('river', None)
    new_river_rapids = river_rapids.filter(river_id = river)

    if river is not None:
      # new_river_rapids = river_rapids.filter(river_id = river)
      serializer = RiverRapidSerializer(new_river_rapids, many = True)

    return Response(serializer.data)
  
  def create(self, request):
    river = River.objects.get(pk=request.data["river"])
    rapid = Rapid.objects.get(pk=request.data["rapid"])
    
    river_rapid = River_Rapid.objects.create(
      river = river,
      rapid = rapid
    )
    serializer = RiverRapidSerializer(river_rapid)
    return Response(serializer.data)
  
  def update(self, request, pk):
    river_rapid = River_Rapid.objects.get(pk=pk)
    
    river = River.objects.get(pk=request.data["river"])
    rapid = Rapid.objects.get(pk=request.data["rapid"])
    
    river_rapid.river = river
    river_rapid.rapid = rapid
    river_rapid.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    river_rapid = River_Rapid.objects.get(pk=pk)
    river_rapid.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class RiverRapidSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = River_Rapid
    fields = ('river', 'rapid', 'id')
    depth = 1
