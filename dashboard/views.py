from django.views import View

from utils.response_utils import success_result


# Create your views here.

class DashboardView(View):

    def get(self, request):
        return success_result(list())
