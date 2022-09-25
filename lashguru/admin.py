from django.contrib import admin
from .models import ManageSocialIcons, CatManageTasks, AddBrandFields, CatManageTemplates


# Register your models here.

class CatManageTaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'change_button',
                    'delete_button']
    search_fields = ['task_name']
    # ordering = ("-created_at",)


class CatManageTemplatesAdmin(admin.ModelAdmin):
    list_display = ['set_service_widget', 'content_cat', 'change_button', 'delete_button']
    search_fields = ['content_cat', 'content', 'template_files']
    # ordering = ("-created_at",)


class AddBrandFieldAdmin(admin.ModelAdmin):
    list_display = ['title', 'change_button', 'delete_button']
    search_fields = ['title']


class ManageSocialIconsAdmin(admin.ModelAdmin):
    list_display = ['title', 'change_button', 'delete_button']


admin.site.register(CatManageTasks, CatManageTaskAdmin)
admin.site.register(ManageSocialIcons, ManageSocialIconsAdmin)
admin.site.register(CatManageTemplates, CatManageTemplatesAdmin)
admin.site.register(AddBrandFields, AddBrandFieldAdmin)
