from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import StoreUser
from .serializers import StoreUserCreateSerializer

class StoreUserCreateAPIView(CreateAPIView):
    queryset = StoreUser.objects.all()
    serializer_class = StoreUserCreateSerializer

# class StoreUserDeleteAPIView(DestroyAPIView):
#     queryset = StoreUser.objects.all()
#     serializer_class = StoreUserSerializer
#     lookup_url_kwarg = 'pk'  # Define the lookup URL keyword argument

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
