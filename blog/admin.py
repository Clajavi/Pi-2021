from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor', 'status')
    raw_id_fields = ('autor',)
    list_filter = ('titulo','autor', 'status', 'criado')
    date_hierarchy = ('publicado')
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)}
#admin.site.register(Post)

# Register your models here.
