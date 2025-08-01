# tag/services.py
from .models import Tag


def get_tags_by_ids(tag_ids):
    """根据标签ID列表查询标签信息（供其他模块调用）"""
    if not tag_ids:
        return []
    tags = Tag.objects.filter(id__in=tag_ids)
    return [{"tag_id": tag.id, "tag_name": tag.name} for tag in tags]


def get_all_tags():
    """获取所有标签（供标签自身接口使用）"""
    tags = Tag.objects.all()
    return [{"tag_id": tag.id, "tag_name": tag.name} for tag in tags]
