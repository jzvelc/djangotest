from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api(request, format=None):
    return Response({
        'users': {
            'list': reverse('api.users:user-list', request=request, format=format),
            'login': reverse('api.users:login', request=request, format=format),
            'refresh': reverse('api.users:refresh', request=request, format=format),
            'me': reverse('api.users:me', request=request, format=format),
        },
    })
