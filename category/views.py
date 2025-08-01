from django.views import View

from utils.response_utils import success_result
from todo.models import Category


# Create your views here.
class CategoryListView(View):

    def get(self, request):
        result = Category.objects.values('id', 'name', 'color')
        return success_result(list(result))
