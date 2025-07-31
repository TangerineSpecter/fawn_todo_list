from django.db import models
from django.utils import timezone


class Category(models.Model):
    """分类表（表名 t_category）"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="分类名称",
        help_text="分类的名称，如工作、生活、学习等，不可重复"
    )
    color = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="显示颜色",
        help_text="用于前端展示的颜色值，如#FF5733，可选填"
    )
    created_at = models.DateTimeField(
        default=timezone.now,  # 新增时自动设置为当前时间
        verbose_name="创建时间",
        help_text="分类的创建时间，自动生成，不可修改"
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # 每次更新时自动刷新为当前时间
        verbose_name="更新时间",
        help_text="分类信息最后更新的时间，自动更新"
    )

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"
        ordering = ["name"]
        db_table = "t_category"
        db_table_comment = "待办事项的一级分类表，用于对todo进行归类管理"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签表（表名 t_tag）"""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="标签名称",
        help_text="标签的名称，如紧急、重要、会议等，不可重复"
    )
    created_at = models.DateTimeField(
        default=timezone.now,  # 新增时自动生成
        verbose_name="创建时间",
        help_text="标签的创建时间，自动生成"
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # 更新时自动刷新
        verbose_name="更新时间",
        help_text="标签信息最后更新的时间，自动更新"
    )

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"
        ordering = ["name"]
        db_table = "t_tag"
        db_table_comment = "待办事项的标签表，用于对todo进行更细致的标记，支持多标签"

    def __str__(self):
        return self.name


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
    category_id = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name="分类ID",
        help_text="关联的分类ID，对应t_category表的id字段，可选填"
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

    @property
    def category(self):
        """获取关联的分类对象（非数据库层面关联）"""
        if self.category_id:
            try:
                return Category.objects.get(id=self.category_id)
            except Category.DoesNotExist:
                return None
        return None


class TodoTag(models.Model):
    """待办-标签关联表（表名 t_todo_tag）"""
    todo_id = models.BigIntegerField(
        verbose_name="待办ID",
        help_text="关联的待办事项ID，对应t_todo表的id字段"
    )
    tag_id = models.BigIntegerField(
        verbose_name="标签ID",
        help_text="关联的标签ID，对应t_tag表的id字段"
    )
    created_at = models.DateTimeField(
        default=timezone.now,  # 新增时自动生成
        verbose_name="创建时间",
        help_text="关联关系的创建时间，自动生成"
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # 更新时自动刷新
        verbose_name="更新时间",
        help_text="关联关系最后更新的时间，自动更新"
    )

    class Meta:
        verbose_name = "待办-标签关联"
        verbose_name_plural = "待办-标签关联"
        unique_together = ("todo_id", "tag_id")  # 避免重复关联
        ordering = ["-created_at"]
        db_table = "t_todo_tag"
        db_table_comment = "待办事项与标签的关联表，实现多对多关系"

    def __str__(self):
        return f"Todo {self.todo_id} - Tag {self.tag_id}"

    @property
    def todo(self):
        """获取关联的待办对象"""
        try:
            return Todo.objects.get(id=self.todo_id)
        except Todo.DoesNotExist:
            return None

    @property
    def tag(self):
        """获取关联的标签对象"""
        try:
            return Tag.objects.get(id=self.tag_id)
        except Tag.DoesNotExist:
            return None
