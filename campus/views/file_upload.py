from django.shortcuts import render,redirect
from django.http import HttpResponse
from .resources import studentResource
from tablib import Dataset
from ..models import student_data
from django.contrib import messages




def export(request):
    student_resource1 = studentResource()
    dataset = student_resource1.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="student.xls"'
    return response

def simple_upload(request):
    if request.method == 'POST' and 'xl_data' in request.FILES:
        # template = "c_admin/student_id.html"
        student_resource = studentResource()
        dataset = Dataset()
        new_persons = request.FILES['xl_data']
        # doc = new_persons

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
        	# print(data[0])
        	value = student_data(
        		data[0],
        		data[1],
        		 data[2],
                 data[3]
                 
                
        		 
        		)
        	value.save()       
        
        # result = student_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    student_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'c_admin/admin.html')
    # return redirect('c_admin/add_student')


    