from django.db import models


# Create your models here.

class Article(models.Model):  # 글생성 데이터 베이스 생성과정
    title = models.CharField('제목', max_length=20, null=False)
    # title에 models에서 charfield형으로 최대길이 20로 받는다.
    content = models.TextField('내용', null=False)
    # content에 models에서 TextField형으로 자료를 받는다.
    create_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    image = models.ImageField(upload_to='images/',blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title
        # 해당 글의 제목을 title로 지정

    def summary(self):
        return self.content[:100]


"""
모델을 만들면 admin의 설정이 필요함.
makemigrations와 migrate를 한다.
확인을 하기위해서는 admin을 만든다.
python manage.py createsuperuser을 사용하여
runserver를 하고 나서 admin페이지로 가면
자신이 만든 모델이 있는것을 볼 수 있다.
"""

"""
모델을 만들고나면 view를 수정하고 templete을 만든다.
"""


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="contents")
    content = models.CharField("", max_length=100)

    def __str__(self):
        return self.content


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
