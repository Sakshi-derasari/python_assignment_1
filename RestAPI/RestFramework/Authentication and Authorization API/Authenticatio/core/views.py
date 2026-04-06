from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .permissions import IsStudent, IsFaculty
from .serializer import UserSerializer

@api_view(['GET'])
@permission_classes([IsStudent])
def get_student(request):
    return Response({"message": "student api calling"})


@api_view(['GET'])
@permission_classes([IsFaculty])
def get_faculty(request):
    return Response({"message": "faculty api calling"})


@api_view(['POST'])
@permission_classes([AllowAny])
def reg(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data})
    else:
        return Response({"errors": serializer.errors})