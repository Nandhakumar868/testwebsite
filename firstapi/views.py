from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Person
from .serializers import FirstSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def index(request):
    if request.method == 'GET':
        ob1 = Person.objects.all()
        serializers = FirstSerializer(ob1,many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        data = request.data
        serializers = FirstSerializer(data = data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    elif request.method == 'PUT':
        data = request.data
        serializers = FirstSerializer(data = data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        ob1 = Person.objects.get(id = data['id'])
        serializers = FirstSerializer(ob1, data = data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    else:
        data = request.data
        ob1 = Person.objects.get(id=data['id'])
        ob1.delete()
        return Response({'message': 'Person deleted'})