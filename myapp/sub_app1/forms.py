from django import forms


class GetContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('john', 'John'),
                                          ('paul', 'Paul'),
                                          ('george', 'George'),
                                          ('ringo', 'Ringo')])
    comments = forms.CharField(widget=forms.Textarea, required=False)
