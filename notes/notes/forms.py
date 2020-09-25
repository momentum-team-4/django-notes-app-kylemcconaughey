from django.forms import ModelForm
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]


class NoteSearchForm(Form):
    SEARCH_BY_CHOICES = [
        ('contains', 'contains'),
        ('exact match', 'exact match'),
    ]

    title = CharField()
    title_search_by = ChoiceField(choices=SEARCH_BY_CHOICES)
    body = CharField()
    body_search_by = ChoiceField(choices=SEARCH_BY_CHOICES)
