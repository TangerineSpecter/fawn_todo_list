from django.db import transaction
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils.datetime_utils import format_datetime

from tag.models import Tag
from .models import Todo, TodoTag


def get_todos_with_tags(keyword=None, page=1, page_size=20):
    """
    获取所有待办事项，并关联标签信息
    支持根据keyword模糊查询title和content
    支持分页查询，默认每页20条
    """
    # 优化查询：使用prefetch_related减少数据库查询
    queryset = Todo.objects.prefetch_related(
        'todotags__tag'  # 关联查询TodoTag和Tag
    )

    # 如果提供了keyword，添加模糊查询条件
    if keyword:
        queryset = queryset.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword)
        )

    # 实现分页
    paginator = Paginator(queryset, page_size)
    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，返回第一页
        todos = paginator.page(1)
    except EmptyPage:
        # 如果page超出范围，返回最后一页
        todos = paginator.page(paginator.num_pages)

    result = []
    for todo in todos:
        # 组装标签数据
        tags = [
            {"tag_id": tt.tag.id, "tag_name": tt.tag.name}
            for tt in todo.todotags.all()
        ]

        # 组装待办数据
        todo_data = {
            "id": todo.id,
            "title": todo.title,
            "content": todo.content,
            "status": todo.status,
            "priority": todo.priority,
            "due_time": format_datetime(todo.due_time),
            "category_id": todo.category_id,
            "tags": tags,
            "created_at": format_datetime(todo.created_at),
            "updated_at": format_datetime(todo.updated_at)
        }
        result.append(todo_data)

    # 返回分页数据和总条数
    return {
        "total": paginator.count,
        "page": todos.number,
        "page_size": todos.paginator.per_page,
        "list": result
    }


def create_todo(title, content, status=0, priority=None, due_time=None, category_id=None, tags=None):
    """
    创建待办事项，并关联标签
    """
    with transaction.atomic():
        # 创建待办
        todo = Todo.objects.create(
            title=title,
            content=content,
            status=status,
            priority=priority,
            due_time=due_time,
            category_id=category_id
        )

        # 关联标签
        if tags:
            for tag_id in tags:
                TodoTag.objects.create(todo_id=todo.id, tag_id=tag_id)

        return todo


def get_todo_detail(todo_id):
    """获取单个待办的详情（包含标签）"""
    todo = Todo.objects.get(id=todo_id)

    # 查询标签
    tag_relations = TodoTag.objects.filter(todo_id=todo_id)
    tag_ids = [rel.tag_id for rel in tag_relations]
    tags = Tag.objects.filter(id__in=tag_ids)

    return {
        "id": todo.id,
        "title": todo.title,
        "content": todo.content,
        "status": todo.status,
        "priority": todo.priority,
        "due_time": format_datetime(todo.due_time),
        "category_id": todo.category_id,
        "tags": [{"tag_id": tag.id, "tag_name": tag.name} for tag in tags],
        "created_at": format_datetime(todo.created_at),
        "updated_at": format_datetime(todo.updated_at)
    }
