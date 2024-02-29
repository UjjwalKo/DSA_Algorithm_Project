from django import forms

ALGORITHM_CHOICES = [
    ('', 'Choose one algorithm'),  # Empty default choice
    ('bubbleSort', 'Bubble Sort'),
    ('insertionSort', 'Insertion Sort'),
    ('selectionSort', 'Selection Sort'),
]

class NameForm(forms.Form):
    your_name = forms.CharField(
        label='Enter a Number:', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Number'})
    )
    algorithm = forms.ChoiceField(
        label='Select an Algorithm:',
        choices=ALGORITHM_CHOICES,
        initial='',  # Set default value to empty
        required=True,
        widget=forms.Select(attrs={'class': 'algorithm-select'})
    )
