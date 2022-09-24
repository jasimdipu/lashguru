from django.db import models


# Create your models here.

class CatManageTasks(models.Model):
    task_name = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    level_two = models.IntegerField(null=True, blank=True)
    level_three = models.IntegerField(null=True, blank=True)
    level_four = models.IntegerField(null=True, blank=True)
    level_five = models.IntegerField(null=True, blank=True)
    level_six = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'cat_manage_svg_files'

    def __str__(self):
        return self.task_name


class ManageSocialIcons(models.Model):
    facebook = models.ImageField(upload_to="social", null=True, blank=True)
    google = models.ImageField(upload_to="social", null=True, blank=True)
    twitter = models.ImageField(upload_to="social", null=True, blank=True)
    instagram = models.ImageField(upload_to="social", null=True, blank=True)
    pinterest = models.ImageField(upload_to="social", null=True, blank=True)
    snapchat = models.ImageField(upload_to="social", null=True, blank=True)
    messenger = models.ImageField(upload_to="social", null=True, blank=True)
    tiktok = models.ImageField(upload_to="social", null=True, blank=True)
    whatsapp = models.ImageField(upload_to="social", null=True, blank=True)

    class Meta:
        db_table = "cat-manage-social-icons"

    def __str__(self):
        return self.facebook
