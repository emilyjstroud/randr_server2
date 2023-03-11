from randrapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
  
    '''Checks to see if User has Associated user

    Method arguments:
      request -- The full HTTP request object
    '''
  
    uid = request.data['uid']
    
    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    
    try:
      user = User.objects.get(uid=uid)
      
      # If authentication was successful, respond with their token
      
      data = {
        'id': user.id,
        'uid': user.uid,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
      }
      print(data)
      return Response(data)
    except:
      # Bad login details were provided. So we can't log the user in.
      data = { 'valid': False }
      return Response(data)
    
@api_view(['POST'])
def register_user(request):
  
  '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
  # Now save the user info in the artist_collective_ink_serverapi table
  user = User.objects.create(
      first_name = request.data['first_name'],
      last_name = request.data['last_name'],
      email = request.data['email'],
      uid = request.data['uid'],
  )
  
    # Return the user info to the client
  data = {
    'id': user.id,
    'uid': user.uid,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'email': user.email
  }
  print(data)
  return Response(data)
