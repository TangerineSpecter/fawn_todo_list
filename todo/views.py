from django.http import JsonResponse
from django.views import View

from todo.models import Todo


# Create your views here.
class TestView(View):

    def get(self, request):
        todo_list = Todo.objects.values()
        return JsonResponse({'code': 200, 'msg': '成功', 'data': list(todo_list)})
