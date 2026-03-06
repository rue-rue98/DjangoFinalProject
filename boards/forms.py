from django import forms


class NewTopicForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea, max_length=4000)

class PostForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=4000)
