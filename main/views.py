from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Teacher, Table

def home(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/home.html', {'teachers': teachers})

def teacher_view(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    tables = Table.objects.filter(teacher=teacher)

    
    return render(
        request,
        'main/teacher.html', 
        {'teacher': teacher, 'tables': tables}
    )
