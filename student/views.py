from django.shortcuts import render
from django.contrib import messages
from .models import Student
from django.shortcuts import redirect

def index(request): # Home
    return render(request, 'index.html')

def register(request): # Register
    return render(request, 'register.html')

def insert_student(request): # Create
    if request.method == 'POST':
        id = request.POST.get('id', '').strip()
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        contact_no = request.POST.get('contact_no', '').strip()

        if not id or not name or not email or not contact_no:
            messages.error(request, 'All fields are required!')
            return redirect('register')

        if Student.objects.filter(id=id).exists():
            messages.warning(request, 'Student with this ID already registered!')
        elif Student.objects.filter(email=email).exists():
            messages.warning(request, 'Student with this email already registered!')
        elif Student.objects.filter(contact_no=contact_no).exists():
            messages.warning(request, 'Student with this contact number already registered!')
        else:
            Student.objects.create(id=id, name=name, email=email, contact_no=contact_no)
            messages.success(request, 'Student registered successfully!')

            return redirect('index')  # Redirect to index.html after successful registration

    return render(request, 'register.html')


def view_students(request): # Read
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})


def delete_student(request, id): # Delete
    student = Student.objects.filter(id=id) # get / filter can be use if filter use multiple same records delete
    student.delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('view_students')


def update_student(request, id): # Update
    student = Student.objects.get(id=id)
    
    if request.method == 'POST':
        new_name = request.POST['name']
        new_email = request.POST['email']
        new_contact_no = request.POST['contact_no']
        
        if Student.objects.filter(email=new_email).exclude(id=id).exists():
            messages.error(request, 'This email is already registered with another student.')
            return render(request, 'update.html', {'student': student})
        if Student.objects.filter(contact_no=new_contact_no).exclude(id=id).exists():
            messages.error(request, 'This contact number is already registered with another student.')
            return render(request, 'update.html', {'student': student})

        student.name = new_name
        student.email = new_email
        student.contact_no = new_contact_no
        student.save()  
        
        messages.success(request, 'Student updated successfully!')
        return redirect('view_students')
    
    return render(request, 'update.html', {'student': student})

