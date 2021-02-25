from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status')
    list_filter = ('publish','status','title')
    search_fields = ('title','description')

admin.site.register(Article,ArticleAdmin)