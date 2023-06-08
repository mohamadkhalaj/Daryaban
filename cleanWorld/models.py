from io import BytesIO
from random import randint

from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.files import File
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.html import mark_safe
from PIL import Image

from account.models import User
from extentions.utils import jalali_convertor


class garbageTypes(models.Model):
    title = models.CharField(max_length=200, verbose_name="نوع", null=False)

    class Meta:
        verbose_name = "دسته بندی آلودگی"
        verbose_name_plural = "دسته بندی آلودگی ها"

    def __str__(self):
        return self.title


class placeImages(models.Model):
    imageUrl = models.CharField(max_length=256, null=True, verbose_name="آدرس دراپ باکس")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=True, null=True, verbose_name="آپلود کننده")
    image = models.ImageField(
        upload_to="images/", verbose_name="تصویر", validators=[FileExtensionValidator(["png", "jpg", "jpeg"])]
    )

    def save(self, *args, **kwargs):
        new_image = self.reduce_image_size(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def reduce_image_size(self, profile_pic):
        ext = profile_pic.name.split(".")[-1].lower()
        if ext == "jpg":
            ext = "jpeg"
        img = Image.open(profile_pic)
        thumb_io = BytesIO()
        img.save(thumb_io, ext, quality=50)
        new_image = File(
            thumb_io, name=".".join(profile_pic.name.split(".")[:-1]) + str(randint(0, 100000)) + "." + ext
        )
        return new_image

    def image_tag(self):
        url = self.image.url
        if self.imageUrl:
            url = self.imageUrl
        return mark_safe(f'<img src="{url}" width="150" height="150" />')

    image_tag.short_description = "تصویر"

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"

    def __str__(self):
        return self.image.name


class reports(models.Model):
    reportedAt = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ گزارش")
    coordinates = models.CharField(max_length=200, verbose_name="مختصات")
    address = models.CharField(max_length=200, verbose_name="آدرس")
    cleanedStatus = models.BooleanField(default=False, verbose_name="پاکیزه شده است؟")
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, default=True, null=True, verbose_name="گزارش کننده")
    garbageType = models.ManyToManyField(garbageTypes, verbose_name="دسته بندی", related_name="category")
    images = models.ManyToManyField(placeImages, verbose_name="تصاویر")

    def humanizeTime(self):
        return naturaltime(self.reportedAt)

    humanizeTime.short_description = "زمان"

    class Meta:
        verbose_name = "گزارش"
        verbose_name_plural = "گزارشات"

    def __str__(self):
        return f"{self.reporter}, {self.address}"

    def jreportedAt(self):
        return jalali_convertor(self.reportedAt)

    jreportedAt.short_description = "تاریخ گزارش"


class cleans(models.Model):
    cleanedAt = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ تمیزشدن")
    cleaner = models.ForeignKey(User, on_delete=models.SET_NULL, default=True, null=True, verbose_name="تمیز کننده")
    report = models.OneToOneField(
        reports, on_delete=models.SET_NULL, null=True, verbose_name="مشخصات گزارش دهنده و محل آلودگی"
    )

    def humanizeTime(self):
        return naturaltime(self.cleanedAt)

    humanizeTime.short_description = "زمان"

    class Meta:
        verbose_name = "تمیز شده"
        verbose_name_plural = "تمیز شده ها"

    def __str__(self):
        return f"{self.cleaner}"

    def jcleanedAt(self):
        return jalali_convertor(self.cleanedAt)

    jcleanedAt.short_description = "تاریخ تمیزشدن"


class contactus(models.Model):
    text = models.TextField(verbose_name="متن پیام")
    reportedAt = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    email = models.EmailField(verbose_name="ایمیل")
    name = models.CharField(max_length=200, verbose_name="نام")

    def humanizeTime(self):
        return naturaltime(self.reportedAt)

    humanizeTime.short_description = "زمان"

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

    def __str__(self):
        return self.email

    def jreportedAt(self):
        return jalali_convertor(self.reportedAt)

    jreportedAt.short_description = "تاریخ گزارش"


class visitor(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")
    time = models.DateTimeField(auto_now=True, verbose_name="زمان")
    userAgent = models.CharField(max_length=256, null=True, verbose_name="یوزر ایجنت")
    path = models.CharField(max_length=256, null=True, verbose_name="مسیر")
    isAdminPanel = models.BooleanField(default=False, verbose_name="پنل ادمین")
    responseTime = models.FloatField(default=None, verbose_name="زمان پاسخ (ثانیه)")

    def humanizeTime(self):
        return naturaltime(self.time)

    humanizeTime.short_description = "زمان"

    class Meta:
        verbose_name = "بازدید کننده"
        verbose_name_plural = "بازدید کنندگان"

    def __str__(self):
        return f"{self.ip_address}, {self.userAgent}"
