from django.http import JsonResponse
from django.views import View

from todo.models import Category


# Create your views here.
class CategoryListView(View):

    def get(self, request):
        result = Category.objects.values('id', 'name', 'color')
        return JsonResponse({
            'code': 200,
            'msg': '成功',
            'data': list(result)
        })
