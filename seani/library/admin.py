from django.contrib import admin

from .models import Module, Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question_text', 'module', 'correc']
    list_filter = ['module']
# admin.site.register(Question, QuestionAdmin)

class QuestioninLine(admin.StackedInline):
    model = Question
    
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    inlines = [QuestioninLine]
#admin.site.register(Module)