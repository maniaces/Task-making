from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Avg,Sum,F
from rest_framework import status

class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        #todo_objs = Todo.objects.filter(user= request.user).order_by('score')[:10]
        todo_objs = Todo.objects.filter(user= request.user).annotate(avg=F('ease') + F('confidence')+ F('impact')).order_by("avg")[:10:-1]
        serializer = TodoSerializer(todo_objs,many=True)
        content = {
            'status' : True,
            'message': "To do fetched",
            'data': serializer.data
        }
        return Response(content, status=status.HTTP_200_OK)
    def post(self,request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()

                content= {
                'status' : True,
                'message': "Success created",
                'data' : serializer.data
                }
                return Response(content, status=status.HTTP_201_CREATED) 
            content={
                'status' : False,
                'message': "invalid data",
                'data' : serializer.errors
                }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            content= {
            'status' : False,
            'message': "Something went wrong"
        }   
            return Response(content, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request):
        try:
            data = request.data           
            if not data.get('uid'):
                status= {
                'status': 'False',
                'message': 'uid is important',
                'data': {}}
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            
            obj = Todo.objects.filter(user= request.user).get(uid= data.get('uid'))
            serializer = TodoSerializer(obj, data = data, partial=True)
            if serializer.is_valid():
                serializer.save()
                status= {
                'status': 'True',
                'message': 'UPDATED',
                'data': serializer.data}
                return Response(content, status=status.HTTP_201_CREATED)
            else:
                status = {
                'status': 'False',
                'message': 'todo not updated'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            
        
        except Exception as e:
            print(e)
            content= {
                'status': 'False',
                'message': 'either UId does not exist or you are not authorised'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
            
        

    def delete(self,request):
        try:
            data = request.data           
            if not data.get('uid'):
                content = {
                'status': 'False',
                'message': 'uid is important',
                'data': {}
                }
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            
            obj = Todo.objects.filter(user= request.user).get(uid= data.get('uid'))
            obj.delete()
            
            content= {
                'status': 'True',
                'message': 'todo item deleted'
            }
            return Response(content, status=status.HTTP_202_ACCEPTED)
        
        except Exception as e:
            print(e)
            content= {
                'status': 'False',
                'message': 'either UId does not exist or you are not authorised'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
            
    
