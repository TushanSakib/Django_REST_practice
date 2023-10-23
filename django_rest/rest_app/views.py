from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
# Create your views here.


@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj,many=True)
    return Response({'status':200,'payload':serializer.data})



class StudentAPI(APIView):
    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs,many=True)
        return Response({'status':200,'payload':serializer.data})
    def post(self,request):
        data = request.data
        serializer = StudentSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'error':serializer.errors,'message':"something went wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})

    def put(self,request):
        pass
    def patch(self,request):
        student_obj = Student.objects.get(id=request.data['id'])
        try:
            serializer = StudentSerializer(student_obj,data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'error':serializer.errors,'message':"something went wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})
    def delete(self,request):
        try:
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status':200,'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})



























#@api_view(['POST'])
#def post_student(request):
#    data = request.data
#    serializer = StudentSerializer(data = request.data)
#
#    if not serializer.is_valid():
#        print(serializer.errors)
#        return Response({'status':403,'error':serializer.errors,'message':"something went wrong"})
#
#    serializer.save()
#    return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})
#
#@api_view(['PUT'])
#def update_student(request,id):
#    student_obj = Student.objects.get(id=id)
#    try:
#        serializer = StudentSerializer(student_obj,data = request.data,partial=True)
#
#        if not serializer.is_valid():
#            print(serializer.errors)
#            return Response({'status':403,'error':serializer.errors,'message':"something went wrong"})
#
#        serializer.save()
#        return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})
#    except Exception as e:
#        print(e)
#        return Response({'status':403,'message':'invalid id'})
#
#@api_view(['DELETE'])
#def delete_student(request,id):
#    try:
#        student_obj = Student.objects.get(id=id)
#        student_obj.delete()
#        return Response({'status':200,'message':'deleted'})
#    except Exception as e:
#        print(e)
#        return Response({'status':403,'message':'invalid id'})
#
#@api_view(['GET'])
#def get_book(request):
#    book_obj = Book.objects.all()
#    serializer = BookSerializer(book_obj,many=True)
#    return Response({'status':200,'payload':serializer.data})
#@api_view(['GET'])
#def home(request):
#    student_objs = Student.objects.all()
#    serializer = StudentSerializer(student_objs,many=True)
#    return Response({'status':200,'payload':serializer.data})