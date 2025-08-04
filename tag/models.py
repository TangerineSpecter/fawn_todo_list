from django.db import models
from django.utils import timezone


# Create your models here.
class Tag(models.Model):
    """标签表（表名 t_tag）"""
    name = models.CharField(
        max_length=50,
    unique=True,
        verbose_name="标签名称",
        help_text="标签的名称，如紧急、重要、会议等，不可重复"
    )
    color = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="显示颜色",
        help_text="用于前端展示的颜色值，如#FF5733，可选填"
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
