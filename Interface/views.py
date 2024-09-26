from django.shortcuts import render
from .forms import FileUploadForm, AnalyzerForm
import os

# Function to handle file uploads
def handle_uploaded_file(file, destination):
    upload_dir = os.path.dirname(destination)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    with open(destination, 'wb+') as destination_file:
        for chunk in file.chunks():
            destination_file.write(chunk)

# View to handle file uploads, to be replace with Natasha's processing code
def file_upload_view(request):
    if request.method == 'POST':
        analyzer_form = AnalyzerForm(request.POST)
        file_form = FileUploadForm(request.POST, request.FILES)

        if analyzer_form.is_valid() and file_form.is_valid():
            analyzer_choice = analyzer_form.cleaned_data['analyzer_choice']
            folder_or_txt_file = file_form.cleaned_data.get('folder_or_txt_file')
            if folder_or_txt_file:
                file_path = os.path.join('uploads', folder_or_txt_file.name)
                handle_uploaded_file(folder_or_txt_file, file_path)

            xlsx_file = file_form.cleaned_data['xlsx_file']
            xlsx_file_path = os.path.join('uploads', xlsx_file.name)
            handle_uploaded_file(xlsx_file, xlsx_file_path)

            response = {
                'analyzer_choice': analyzer_choice,
                'folder_or_txt_file': folder_or_txt_file.name if folder_or_txt_file else None,
                'xlsx_file': xlsx_file.name,
            }

            return render(request, 'formSuccess.html', response)

    else:
        analyzer_form = AnalyzerForm()
        file_form = FileUploadForm()

    context = {
        'analyzer_form': analyzer_form,
        'file_form': file_form,
    }
    
    return render(request, 'analyzerForm.html', context)


