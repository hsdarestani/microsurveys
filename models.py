from django.db import models
from extensions.utils import jalali_converter
from apps.useraccount.models import Profile , Company,Position


class Question(models.Model):
    Title = models.CharField(max_length=2000, null=True, verbose_name="متن سوال")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"
        managed= True

    def __str__(self):
        return str(self.Title)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"




class Template(models.Model):
    Title = models.CharField(max_length=2000, null=True, verbose_name="عنوان")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    html = models.CharField(max_length=10000, null=True, verbose_name="قالب")
    MinAns = models.IntegerField(null=True, blank=True,verbose_name="حداقل امتیاز")
    MaxAns = models.IntegerField(null=True, blank=True,verbose_name="حداکثر امتیاز")

    class Meta:
        verbose_name = "قالب"
        verbose_name_plural = "قالب‌ها"
        managed= True

    def __str__(self):
        return str(self.Title)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class Event(models.Model):
    Title = models.CharField(max_length=2000, null=True, verbose_name="عنوان")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    question = models.ForeignKey(Question,  null=True, blank=True,on_delete=models.CASCADE, verbose_name="سوال")
    position = models.ForeignKey(Position,  null=True, blank=True,on_delete=models.CASCADE, verbose_name="نقش")
    template = models.ForeignKey(Template,  null=True, blank=True,on_delete=models.CASCADE, verbose_name="قالب")
    SecAfter = models.IntegerField(null=True, blank=True,verbose_name="زمان انتظار")

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"
        managed= True

    def __str__(self):
        return str(self.Title)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class Answer(models.Model):
    answer = models.IntegerField(null=True, blank=True,verbose_name="پاسخ")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    EntryAgent = models.ForeignKey(Profile,  null=True, blank=True,on_delete=models.CASCADE, verbose_name="ثبت کننده")
    event = models.ForeignKey(Event,  null=True, blank=True,on_delete=models.CASCADE, verbose_name="رویداد مربوطه")

    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ‌ها"
        managed= True

    def __str__(self):
        return str(self.Title)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"
