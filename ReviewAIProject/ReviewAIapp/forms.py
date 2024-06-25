from django import forms


class userpromptForm(forms.Form):
    reviewpers_1 = forms.BooleanField(label='信頼性',required=False)
    reviewpers_2 = forms.BooleanField(label='網羅性',required=False)
    reviewpers_3 = forms.BooleanField(label='妥当性',required=False)
    reviewpers_4 = forms.BooleanField(label='可読性',required=False)
    reviewpers_5 = forms.BooleanField(label='誤字脱字',required=False)
    reviewcont = forms.CharField(label='レビュー依頼',widget=forms.Textarea,required=True)

