from django import forms


class FileUploadForm(forms.Form):
    """Docstring for FileUploadForm"""
    file = forms.FileField(label="Upload Excel/CSV File")
