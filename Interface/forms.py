from django import forms

class AnalyzerForm(forms.Form):
    ANALYZERS = [
        ('adash', 'ADASH'),
        ('csi', 'CSI'),
    ]
    
    analyzer_choice = forms.ChoiceField(
        choices=ANALYZERS,
        widget=forms.RadioSelect,
        label=""
    )


class FileUploadForm(forms.Form):
    folder_or_txt_file = forms.FileField(label='Upload Folder (.zip) or .txt File', required=True)
    xlsx_file = forms.FileField(label='Upload .xlsx File', required=True)

    def clean_txt_file(self):
        txt_file = self.cleaned_data.get('txt_file')
        if txt_file and not txt_file.name.endswith('.txt'):
            raise forms.ValidationError("Please upload a valid .txt file.")
        return txt_file

    def clean_folder(self):
        folder = self.cleaned_data.get('folder')
        if folder and not folder.name.endswith('.zip'):
            raise forms.ValidationError("Please upload a valid .zip file.")
        return folder