from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


# from utils.models import BaseModel


# Create your models here.

class CatManageTasks(models.Model):
    task_name = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    level_two = models.IntegerField(null=True, blank=True)
    level_three = models.IntegerField(null=True, blank=True)
    level_four = models.IntegerField(null=True, blank=True)
    level_five = models.IntegerField(null=True, blank=True)
    level_six = models.IntegerField(null=True, blank=True)

    def change_button(self):
        return format_html('<a class="btn" href="/admin/lashguru/catmanagetasks/{}/change/">Edit</a>', self.id)

    def delete_button(self):
        return format_html('<a class="btn" href="/admin/lashguru/catmanagetasks/{}/delete/">Delete</a>', self.id)

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

    def change_button(self):
        return format_html('<a class="btn" href="/admin/lashguru/managesocialicons/{}/change/">Edit</a>', self.id)

    def delete_button(self):
        return format_html('<a class="btn" href="/admin/lashguru/managesocialicons/{}/delete/">Delete</a>', self.id)

    def title(self):
        return format_html('<p>Social Icon Set 00{}</p>', str(self.id))

    class Meta:
        db_table = "cat-manage-social-icons"

    def __str__(self):
        return f"Social Icon Set 00" + str(self.id)


class CatManageTemplates(models.Model):
    class ContentCategory(models.TextChoices):
        service = "Service", _("Service")
        content = "Content", _("Content")
        Review = "Review", _("Review")

    content_cat = models.CharField(max_length=200, choices=ContentCategory.choices)
    content = models.JSONField(help_text="Json content in here!")
    template_files = models.ImageField(upload_to="template_content", null=True, blank=True)

    class Meta:
        db_table = "cat-manage.templates"

    def change_button(self):
        return format_html('<a class="btn" href="/admin/lashguru/catmanagetemplates/{}/change/">Edit</a>', self.id)

    def delete_button(self):
        return format_html('<a class="btn" href="/admin/lashguru/catmanagetemplates/{}/delete/">Delete</a>', self.id)

    def set_service_widget(self):
        return format_html('<p>Service Widget 00{}</p>',str(self.id))

    def __str__(self):
        return f"Service Widget 00" + str(self.id)


class AddBrandFields(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    positive_files = models.ImageField(upload_to="positive_files")
    negative_files = models.ImageField(upload_to="negative_files")
    colored_files = models.ImageField(upload_to="colored_files")

    class Meta:
        db_table = 'add_brand_fields'

    def change_button(self):
        return format_html('<a class="btn btn-primary" href="/admin/lashguru/addbrandfields/{}/change/">Edit</a>', self.id)

    def delete_button(self):
        return format_html('<a class="btn btn-danger" href="/admin/lashguru/addbrandfields/{}/delete/">Delete</a>', self.id)

    def __str__(self):
        return self.title
