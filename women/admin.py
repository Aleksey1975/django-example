from django.contrib import admin
from .models import *


class MarriedFilter(admin.SimpleListFilter):
    title = "Статус женщины"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        if self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women2)
class Women2Admin(admin.ModelAdmin):
    # fields = ('title', 'content', 'photo', 'is_published',)
    # exclude = ('title', 'content')
    # readonly_fields = ('title', 'content')
    filter_horizontal = ('tag',)
    list_display = ('title', 'husband', 'is_published', 'cat', 'id', 'brief_info')
    list_display_links = ('title',)
    list_editable = ('is_published', 'cat')
    list_filter = (MarriedFilter, 'is_published', 'time_created')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-time_created', 'title',)
    list_per_page = 10
    actions = ('set_published', 'set_unpublished')
    search_fields = ('title', 'cat__name',)

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    @admin.action(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        #  self.message_user(request, f'Опубликовано {queryset.count()} статьи')
        self.message_user(request, f'Опубликовано {count} статьи')

    @admin.action(description='Снять с публикации')
    def set_unpublished(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'Снято с публикации {count} статьи', messages.WARNING)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name',)
    prepopulated_fields = {'slug': ('name',)}


class HusbandAdmin(admin.ModelAdmin):
    list_display = ('id', 'm_count', 'name',)
    list_editable = ('m_count',)


admin.site.register(Tag, TagAdmin)

admin.site.register(Husband, HusbandAdmin)

# admin.site.register(Women2, Women2Admin)

admin.site.register(Category, CategoryAdmin)
