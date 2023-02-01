from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
 
class Table(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='المعلم')
    name = models.CharField(max_length=150, verbose_name='اسم نشاط التطوير المهني')
    auth = models.CharField(max_length=150, verbose_name='الجهة')
    start_date = models.DateField(verbose_name='تاريخ البداية')
    end_date = models.DateField(verbose_name='تاريخ النهاية')
    type = models.CharField(max_length=150, verbose_name='نوع النشاط')
    t_dur = models.CharField(max_length=150, verbose_name='نوع المدة')
    dur = models.PositiveSmallIntegerField(verbose_name='مدة النشاط')

    def __str__(self):
        return f'الجدول {self.pk} الخاص بالمعلم: ' + self.teacher.name
