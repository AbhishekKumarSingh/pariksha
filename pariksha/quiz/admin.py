from django.contrib import admin
from quiz.models import Choice, Question, Quiz
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

    inlines = [ChoiceInline]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Add Description', {'fields': ['question_desc']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Quiz Details', {'fields':['title', 'author']}),
        #('Author', {'fields':['author']}),
        #('Date created', {'fields':['date_created']}),
    ]

    inlines = [QuestionInline]
    # fields to be displayed while listing all Quiz objects
    list_display = ('title', 'author', 'maxPossibleScore', 'date_created')
    # filter Quiz objects on the basis of items provided in list
    list_filter = ['date_created']
    # Search Quiz objects on the basis of items provided in list
    search_fields = ['title', 'author']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)