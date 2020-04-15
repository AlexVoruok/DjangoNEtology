from django.contrib import admin
from .models import Article, Tags, TagRelation

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from pprint import pprint


class TagsInlinFormset(BaseInlineFormSet):
    def clean(self):

        main_tag_count = 0
        tag_list = []
        for form in self.forms:
            pprint(form.cleaned_data)

            if form.cleaned_data.get('main_tag'):
                main_tag_count += 1

            if main_tag_count > 1:
                raise ValidationError('У статьи может быть только один главный тэг')

            tag = form.cleaned_data.get('tags')
            if tag in tag_list:
                raise ValidationError('Уберите повторяющиеся тэги')

            else:
                tag_list.append(tag)

        if main_tag_count == 0:
            raise ValidationError('У статьи должен быть как минимум один главный тэг')

        return super().clean()


class TagsInline(admin.TabularInline):
    model = TagRelation
    extra = 1
    formset = TagsInlinFormset


class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsInline, ]
    exclude = ('tags', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags)
