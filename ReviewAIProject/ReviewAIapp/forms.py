from django import forms


class userpromptForm(forms.Form):
    name = forms.CharField(label='レビュー依頼文面',max_length=100,required=True)
