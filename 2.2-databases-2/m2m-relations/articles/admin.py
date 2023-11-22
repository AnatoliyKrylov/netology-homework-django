from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_exists = -1
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['is_main']:
                is_main_exists += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if is_main_exists == 1:
                raise ValidationError('Должно быть не более одного основного раздела')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ['name',]
