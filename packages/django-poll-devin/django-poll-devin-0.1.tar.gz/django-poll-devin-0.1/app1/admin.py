from django.contrib import admin
from .models import   Question,Choice



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('问题', {'fields': ['question_text']}),
        ('添加时间', {'fields': ['pub_date'], 'classes': ['collapse']}), # 字典第二项不可省略
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]







admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)