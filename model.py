from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# ������
class Score(models.Model):
    user = models.CharField(verbose_name='�û���', max_length=16, unique=True)
    score = models.IntegerField(verbose_name='����', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(1)])

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = '������'
        verbose_name_plural = verbose_name


# ���α�
class Ranking(models.Model):
    id = models.OneToOneField(Score, on_delete=models.CASCADE, primary_key=True)
    rank = models.IntegerField(verbose_name='����', validators=[MinValueValidator(1)])
