from django.http import JsonResponse
from django.views import View


# Create your views here.

class DashboardView(View):

    def get(self, request):
        return JsonResponse({
            'code': 200,
            'msg': '成功',
            'data': list()
        })
