from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea, Select

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "category", "task"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите назавание'}),
                   "category": Select(attrs={'class': 'select',}, choices=(('Магазин', 'Магазин'), ('Дом', 'Дом'))),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                   }
