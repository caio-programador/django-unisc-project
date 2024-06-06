from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'title', 'text', 'tags')
        widgets = {
            'user': forms.TextInput(attrs={
                'placeholder': 'Ex: João...'
                
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Adicione um título...'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Adicione conteúdo para seu artigo...'
            }),
            'tags': forms.TextInput(attrs={
                'placeholder': 'Adicione palavras-chave separadas por vírgulas...'
            }),
        }
        labels = {
            'user': 'Nome de usuário',
            'title': 'Título',
            'text': 'Conteúdo',
            'tags': 'Tags',
        }