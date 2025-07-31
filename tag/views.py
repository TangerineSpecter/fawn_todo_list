from django.http import JsonResponse
from django.views import View

from tag.models import Tag


# Create your views here.
class TagListView(View):

    def get(self, request):
        result = Tag.objects.values('id', 'name')
        return JsonResponse({
            'code': 200,
            'msg': '成功',
            'data': list(result)
        })
