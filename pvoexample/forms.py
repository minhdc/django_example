from django.forms import ModelForm,Form

from .models import Word, Example

'''
class WordForm(Form):
    id          = ModelForm.Bi
    word        = ModelForm.CharField(max_length=50)
    definition  = ModelForm.CharField(
        max_length  = 2000,
        widget      = ModelForm.Textarea(),
        help_text   = "Write ur definition here..."   
    )
    pic_url     = ModelForm.URLField(
        help_text   = "paste the URL of the picture of this word here"
    )

    def clean(self):
        cleaned_data    = super(WordForm,self).clean()
        word            = cleaned_data.get('word')            
        definition      = cleaned_data.get('definition')
        pic_url         = cleaned_data.get('pic_url')
        
        if not word and not definition and not pic_url:
            raise forms.ValidationError('You have to fill in something...')
'''
class WordForm(ModelForm):
    class Meta:
        model       = Word
        fields      = ['id','word','definition','pic']
    
           
class ExampleForm(ModelForm):
    class Meta:
        model       = Example
        fields      = ['id','example_desc','keywords','source']

