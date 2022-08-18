from django.contrib import admin
from .models import Question  , Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
    ]
    inlines=[ChoiceInline]
    list_display = ('question_text' , 'pub_date' , 'was_published_recently')

    #変更点
    list_display_links = ('pub_date' , )
    list_editable = ('question_text' , )
    actions = ['change_title_action']

    def change_title_action(self , request , queryset):
        queryset.update(question_text='other')
    change_title_action.short_description = 'QUESTION TEXTをotherに変更'
    #ここまで

    list_filter = ['pub_date']
    search_fields = ['question_text' , 'pub_date']


class Question1(Question):
    class Meta:
        proxy =  True

admin.site.register(Question1 ,  QuestionAdmin)


class Question2(Question):
    class Meta:
        proxy =  True

admin.site.register(Question2 ,  QuestionAdmin)