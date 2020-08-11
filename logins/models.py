from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=600)
    photo_number = models.CharField(max_length=26)

    class Meta:
        verbose_name = "用户管理"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
