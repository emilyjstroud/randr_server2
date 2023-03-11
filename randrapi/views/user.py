from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from randrapi.models import User

class UserView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    
    users = User.objects.all()
    uid_query = request.query_params.get('uid', None)
    if uid_query is not None:
      users = users.filter(uid=uid_query)
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)
  
  def create(self, request):
    
    user = User.objects.create(
      first_name = request.data["first_name"],
      last_name = request.data["last_name"],
      email = request.data["email"],
      uid = request.data["uid"],
      id = request.data["id"]
    )
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
  def update(self, request, pk):
    
    user = User.objects.get(pk=pk)
    
    user.first_name = request.data["first_name"]
    user.last_name = request.data["last_name"]
    user.email = request.data["email"]
    user.uid = request.data["uid"]
    user.id = request.data["id"]
    user.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
      user = User.objects.get(pk=pk)
      user.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'uid', 'id')
    depth = 1
