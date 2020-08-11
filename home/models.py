from django.db import models
from logins.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=70, verbose_name="项目名", unique=True)
    founder = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建人", related_name="founder")
    status = models.BooleanField(default=True, verbose_name="是否归档")

    class Meta:
        verbose_name = "项目管理"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project_name


class Edition(models.Model):
    project_name = models.ForeignKey(to=Project, on_delete=models.DO_NOTHING,
                                     verbose_name="所属项目")
    edition = models.CharField(max_length=30, verbose_name="版本")

    def __str__(self):
        return self.edition


class Modular(models.Model):
    project_name = models.ForeignKey(to=Project, on_delete=models.DO_NOTHING,
                                     verbose_name="所属项目")
    modular = models.CharField(max_length=30, verbose_name="模块")

    def __str__(self):
        return self.modular


class BugList(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    founder = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建人", related_name="founder_bug")
    project_name = models.ForeignKey(Project, on_delete=models.DO_NOTHING, verbose_name="所属项目")
    edition = models.ForeignKey(Edition, on_delete=models.DO_NOTHING, verbose_name="所属版本")
    modular = models.ForeignKey(Modular, on_delete=models.DO_NOTHING, verbose_name="所属模块")
    priority = models.CharField(max_length=150, default='', verbose_name="优先级")
    handler = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="处理人")
    describe = models.CharField(max_length=150, default='', verbose_name="描述")
    state = models.CharField(max_length=10, verbose_name="状态", default="未解决")
    create_time = models.DateTimeField(verbose_name="创建时间")

    class Meta:
        verbose_name = "bug列表"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class History(models.Model):
    bug = models.ForeignKey(BugList, on_delete=models.DO_NOTHING, verbose_name="关联bug")
    handler = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="处理人")
    handler_time = models.DateTimeField(verbose_name="处理时间")
    describe = models.CharField(max_length=150, default='', verbose_name="描述")
    operation = models.CharField(max_length=150, verbose_name="操作")

    class Meta:
        verbose_name = "bug处理记录"  # 表名改成中文名
        verbose_name_plural = verbose_name
