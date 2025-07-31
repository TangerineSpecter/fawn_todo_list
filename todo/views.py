from django.http import JsonResponse
from django.views import View

from todo.models import Todo, TodoTag, Tag


# Create your views here.
class TestView(View):

    def get(self, request):
        todo_list = Todo.objects.values()
        # 查询所有待办事项
        todo_list = Todo.objects.all()
        result = []

        for todo in todo_list:
            # 基础待办信息
            todo_data = {
                "id": todo.id,
                "title": todo.title,
                "content": todo.content,
                "status": todo.status,
                "priority": todo.priority,
                "due_time": todo.due_time.isoformat() + "Z" if todo.due_time else None,
                "category_id": todo.category_id,
                "tags": [],  # 用于存放标签信息
            }

            # 查询当前待办关联的所有标签ID
            todo_tag_relations = TodoTag.objects.filter(todo_id=todo.id)
            tag_ids = [relation.tag_id for relation in todo_tag_relations]

            # 查询标签详情并组装
            if tag_ids:
                tags = Tag.objects.filter(id__in=tag_ids)
                todo_data["tags"] = [
                    {"tag_id": tag.id, "tag_name": tag.name}
                    for tag in tags
                ]

            result.append(todo_data)

        return JsonResponse({
            'code': 200,
            'msg': '成功',
            'data': result
        })
