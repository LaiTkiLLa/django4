from django.contrib import admin

from .models import Article, Scope, Scope_Aricle


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass

class SectionInline(admin.TabularInline):
    model = Scope_Aricle
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


admin.site.register(Article,ArticleAdmin)
admin.site.register(Scope)
