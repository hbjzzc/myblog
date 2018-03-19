from django.db import models

# Create your models here.


# 创建用户模型
class User(models.Model):

    name = models.CharField(max_length=20, verbose_name="姓名")
    desc = models.CharField(max_length=100, verbose_name="个人简历")
    password = models.CharField(max_length=20, verbose_name="密码")

    class Meta:
        db_table = "users"

    def __repr__(self):
        return self.name


# 创建文章模型
class Title(models.Model):

    headline = models.CharField(max_length=20, verbose_name='标题')
    author = models.CharField(max_length=20, verbose_name='作者')
    contents = models.CharField(max_length=10000, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    user= models.ForeignKey(User,verbose_name='文章作者')

    class Meta:
        db_table = "titles"

    def __repr__(self):
        return self.headline






