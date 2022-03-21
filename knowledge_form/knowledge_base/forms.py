from dataclasses import field
from django import  forms

from knowledge_base.models import Knowledge

class KnowledgeForm (forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ('title','category','description')