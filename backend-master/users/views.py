
from rest_framework.viewsets import ModelViewSet

from .models import ShippingAddress

from .serializers import ShippingAddressSerializer, UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def partial_update(self, request, pk=None):
        if 'shipping_address' in request.data:
            if hasattr(request.user, 'shipping_address'):
                address = request.user.shipping_address
                address_serializer = ShippingAddressSerializer(
                    address, data={'user': request.user.id, **request.data['shipping_address']})
                address_serializer.is_valid(raise_exception=True)
                address_serializer.save()
            else:
                address = ShippingAddress.objects.create(user=request.user, **request.data['shipping_address'])

        return super().partial_update(request, pk)

