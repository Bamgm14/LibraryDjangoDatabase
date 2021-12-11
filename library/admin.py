from django.contrib import admin


from .models import *


@admin.action(description='Mark selected stories as issued')
def search(modeladmin, request, queryset):
    queryset.update(status='p')



class bookslist_admin(admin.ModelAdmin):
    list_display = ('Title', 'Slug', 'ISBN', 'stock', 'shelf_number')
    ordering = ['Title']
    search_fields = ['Title']
    actions = [search]

class issued_list_admin(admin.ModelAdmin):
    list_display = ('ISBN', 'account_id', 'issued_time')
    ordering = ['issued_time']
    search_fields = ['ISBN', 'account_id', 'issued_time']
    actions = [search]
class reader_admin(admin.ModelAdmin):
    list_display = ( 'account_id', 'first_name', 'last_name')
    ordering = ['account_id']
    search_fields = ['account_id']
    actions = [search]

    

admin.site.register(bookslist, bookslist_admin) 
admin.site.register(issued_list, issued_list_admin) 
admin.site.register(reader, reader_admin) 
