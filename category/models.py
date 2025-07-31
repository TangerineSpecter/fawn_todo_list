from django.db import models
from django.utils import timezone


# Create your models here.
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
