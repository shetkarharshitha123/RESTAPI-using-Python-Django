from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
from RestApiapp.models import Employee
from RestApiapp.serializers import EmployeeSerializers
from django.contrib.auth.hashers import make_password, check_password


@api_view(['GET'])
def health_check(request):
    return Response({"status": 200, "message": "API is working"})


@api_view(['GET'])
def get_all_users(request):
    users = Employee.objects.all()
    serializer = EmployeeSerializers(users, many=True)
    return Response({"status": 200, "users": serializer.data})


@api_view(['GET'])
def get_user_by_id(request, id):
    user = get_object_or_404(Employee, id=id)
    serializer = EmployeeSerializers(user)
    return Response({"status": 200, "user": serializer.data})


@api_view(['POST'])
def create_user(request):
    serializer = EmployeeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(password=make_password(request.data['password']))
        return Response({"status": 201, "message": "User created successfully", "user": serializer.data})
    return Response({"status": 400, "errors": serializer.errors})


@api_view(['PUT'])
def update_user(request, id):
    user = get_object_or_404(Employee, id=id)
    serializer = EmployeeSerializers(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": 200, "message": "User updated successfully", "user": serializer.data})
    return Response({"status": 400, "errors": serializer.errors})


@api_view(['DELETE'])
def delete_user(request, id):
    user = get_object_or_404(Employee, id=id)
    user.delete()
    return Response({"status": 200, "message": "User deleted successfully"})


@api_view(['GET'])
def search_users(request):
    name_query = request.GET.get('name', '')
    users = Employee.objects.filter(Q(ename__icontains=name_query)) 
    serializer = EmployeeSerializers(users, many=True)
    return Response({"status": 200, "results": serializer.data})


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = Employee.objects.get(email=email)
        if check_password(password, user.password):  
            return Response({"status": "success", "user_id": user.id})
        else:
            return Response({"status": "fail", "message": "Incorrect password"}, status=400)
    except Employee.DoesNotExist:
        return Response({"status": "fail", "message": "User not found"}, status=404)

