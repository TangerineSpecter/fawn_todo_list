from django.db import models
from django.utils import timezone

from category.models import Category
from tag.models import Tag


class Todo(models.Model):
    """待办事项表（表名 t_todo）"""
    STATUS_CHOICES = (
        (0, "未完成"),
        (1, "已完成"),
        (2, "已取消"),
    )
    PRIORITY_CHOICES = (
        (1, "低"),
        (2, "中"),
        (3, "高"),
    )

    title = models.CharField(
        max_length=200,
        verbose_name="标题",
        help_text="待办事项的标题，简要描述任务内容"
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name="详情",
        help_text="待办事项的详细描述，可选填"
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=0,
        verbose_name="状态",
        help_text="待办事项的状态：0-未完成，1-已完成，2-已取消"
    )
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES,
        null=True,
        blank=True,
        verbose_name="优先级",
        help_text="待办事项的优先级：1-低，2-中，3-高，可选填"
    )
    due_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="截止时间",
        help_text="待办事项的截止时间，可选填"
    )
    # 将category定义为外键，替代手动的category_id + @property
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # 分类删除时，待办的category设为null
        null=True,
        related_name="todos",  # 允许通过Category查询关联的待办
        verbose_name="所属分类"
    )
    created_at = models.DateTimeField(
        default=timezone.now,  # 新增时自动生成
        verbose_name="创建时间",
        help_text="待办事项的创建时间，自动生成，不可修改"
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # 更新时自动刷新
        verbose_name="更新时间",
        help_text="待办事项最后更新的时间，自动更新"
    )

    class Meta:
        verbose_name = "待办事项"
        verbose_name_plural = "待办事项"
        ordering = ["-created_at"]
        db_table = "t_todo"
        db_table_comment = "待办事项主表，存储所有待办任务的基本信息"

    def __str__(self):
        return self.title


class TodoTag(models.Model):
    """待办-标签关联表（表名 t_todo_tag）"""
    # 改用外键关联，替代BigIntegerField
    todo = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,  # 当Todo删除时，关联的TodoTag也删除
        related_name="todotags",  # 定义反向关联名称，供Todo查询关联的标签
        verbose_name="待办事项",
        help_text="关联的待办事项，对应t_todo表"
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,  # 当Tag删除时，关联的TodoTag也删除
        related_name="todotags",  # 定义反向关联名称，供Tag查询关联的待办
        verbose_name="标签",
        help_text="关联的标签，对应t_tag表"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="创建时间"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间"
    )

    class Meta:
        verbose_name = "待办-标签关联"
        verbose_name_plural = "待办-标签关联"
        unique_together = ("todo", "tag")  # 避免重复关联
        ordering = ["-created_at"]
        db_table = "t_todo_tag"
        db_table_comment = "待办事项与标签的关联表，实现多对多关系"

    def __str__(self):
        return f"Todo {self.todo.id} - Tag {self.tag.id}"
