from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contact
from .serializers import ContactSerializer


@api_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Контакт успешно добавлен'}, status=status.HTTP_201_CREATED)

        # Добавим вывод ошибок
        return Response({
            'success': False,
            'message': 'Ошибка при добавлении контакта',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
