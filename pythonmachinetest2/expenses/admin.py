from django.contrib import admin
from .models import Category, Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'expense_count')
    search_fields = ('name',)
    
    def expense_count(self, obj):
        return obj.expense_set.count()
    expense_count.short_description = 'Number of Expenses'

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date', 'formatted_date')
    list_filter = ('category', 'date')
    search_fields = ('title',)
    date_hierarchy = 'date'
    ordering = ('-date',)
    
    def formatted_date(self, obj):
        return obj.date.strftime('%b. %d, %Y')
    formatted_date.short_description = 'Date'
