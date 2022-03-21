
from django.db import models
from django.conf import settings

# Create your models here.

class Knowledge (models.Model):
    title = models.CharField('タイトル', max_length=128)
    category = models.CharField('カテゴリ', max_length=128)
    description =  models.TextField('説明',blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name='投稿者',
                                    on_delete=models.CASCADE)
    regist_date = models.DateTimeField('投稿日', auto_now_add=False)
    update_date = models.DateTimeField('更新日',auto_now=True)
    
    def __str__(self) :
        return self.title
