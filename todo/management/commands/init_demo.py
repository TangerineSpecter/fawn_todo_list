from django.core.management.base import BaseCommand
from django.utils import timezone

from category.models import Category
from tag.models import Tag
from todo.models import Todo
from todo.models import TodoTag


class Command(BaseCommand):
    help = '初始化演示数据（会先清空现有数据）'

    def handle(self, *args, **options):
        # 清空旧数据（按依赖顺序删除）
        self.stdout.write("清空旧数据...")
        TodoTag.objects.all().delete()
        Todo.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        # 创建演示数据
        self.stdout.write("创建演示数据...")

        # 分类
        work_cat = Category.objects.create(name="工作")
        life_cat = Category.objects.create(name="生活")
        study_cat = Category.objects.create(name="学习")

        # 标签
        urgent_tag = Tag.objects.create(name="紧急")
        daily_tag = Tag.objects.create(name="日常")
        important_tag = Tag.objects.create(name="重要")

        # 待办
        todo1 = Todo.objects.create(
            title="完成Django模型设计",
            content="优化Todo和Tag的关联逻辑",
            status=0,
            priority=3,
            due_time=timezone.now() + timezone.timedelta(days=1),
            category=work_cat
        )

        todo2 = Todo.objects.create(
            title="健身",
            content="跑步30分钟",
            status=1,
            priority=2,
            due_time=timezone.now() + timezone.timedelta(hours=3),
            category=life_cat
        )

        # 关联标签
        TodoTag.objects.create(todo=todo1, tag=urgent_tag)
        TodoTag.objects.create(todo=todo1, tag=important_tag)
        TodoTag.objects.create(todo=todo2, tag=daily_tag)

        self.stdout.write(self.style.SUCCESS("演示数据初始化完成！"))
