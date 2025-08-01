from django.views import View

from utils.response_utils import success_result
from tag.models import Tag


# Create your views here.
class TagListView(View):

    def get(self, request):
        result = Tag.objects.values('id', 'name')
        return success_result(list(result))
