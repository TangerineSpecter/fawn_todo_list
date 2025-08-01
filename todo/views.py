# todo/views.py
from django.shortcuts import get_object_or_404
from django.views import View

from utils.response_utils import success_result, error_result, list_result
from utils.validation_utils import validate_pagination_params, handle_validation_error, ValidationError
from .models import Todo
from .services import get_todos_with_tags, get_todo_detail


class TodoListView(View):
    """
    查询 todo列表
    """

    def get(self, request):
        try:
            # 获取查询参数
            keyword = request.GET.get('keyword', None)
            page = request.GET.get('page', 1)
            page_size = request.GET.get('pageSize', 20)

            # 使用参数验证工具验证分页参数
            validated_page, validated_page_size = validate_pagination_params(page, page_size)

            # 调用服务层获取数据
            result = get_todos_with_tags(keyword=keyword, page=validated_page, page_size=validated_page_size)
            return list_result(
                data=result['list'],
                total=result['total'],
                page=result['page'],
                page_size=result['page_size']
            )
        except ValidationError as e:
            return handle_validation_error(e)
        except Exception as e:
            return error_result(f'获取数据失败: {str(e)}', data=[])


class TodoDetailView(View):
    """
    查询 todo详情，pk 是 primary key的意思
    """

    def get(self, request, pk):
        try:
            # 验证待办是否存在
            get_object_or_404(Todo, id=pk)
            # 调用服务层获取详情
            detail_data = get_todo_detail(pk)
            return success_result(detail_data)
        except Exception as e:
            return error_result(f'获取详情失败: {str(e)}', data=None)
