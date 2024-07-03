from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView,FormView,DeleteView
from .forms import ContactForm,TaskUploadForm
from .models import Student,Grades,Contact,Tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login_required
from django.contrib.auth import logout
from django.views import View
import json
from django.core.exceptions import ValidationError
# Create your views here.
class HomeView(TemplateView):
    template_name = "students/home.html"


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['num_students'] =  Student.objects.all().count()
        context['number_of_classes'] = Student.objects.values('class_number').distinct().count()
        return context

class ThankYou(TemplateView):
    template_name = "students/thank_you.html"




class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "students/contact.html"
    success_url = reverse_lazy("students:thankyou")

    def form_valid(self, form):
        form.save()  # Save the form data to the database
        return super().form_valid(form)



class CreateStudentView(LoginRequiredMixin,CreateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("students:thankyou")

class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

    success_url = reverse_lazy("students:thankyou")


    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        grades = Grades.objects.filter(student=self.object)
        context['Grades'] = [{'name': grade.get_subject_display(), 'value': grade.grade, "explanation": grade.explanation} for grade in grades]
        return context

class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("students:list_students")

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy("students:list_students")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'students/signup.html'

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})

class AddGrageView(CreateView):
    model = Grades
    fields = "__all__"
    success_url = reverse_lazy("students:list_students")

class ContactListView(ListView):
    model = Contact
    template_name = "students/contacts_list.html"
    context_object_name = "contacts"

def search_students(request):
    if request.method == 'POST':
        searched = request.POST["searched"]
        students = Student.objects.filter(first_name__contains=searched)
        return render(request,"students/search_page.html",{'searched':searched,
                                                           'students':students})
    else:
        return render(request, "students/search_page.html", {})

class TaskListView(ListView):
    model = Tasks
    #context_object_name = 'tasks'
    success_url = reverse_lazy("students:thankyou")

    def get_queryset(self) :
        pk = self.kwargs.get('pk')
        if pk is None :
            raise ValueError("pk is missing from URL parameters")
        return Tasks.objects.filter(student_id=pk)

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk is None :
            raise ValueError("pk is missing from URL parameters")
        context['student'] = get_object_or_404(Student, pk=pk)
        return context
class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Tasks
    fields = "__all__"
    success_url = reverse_lazy("students:thankyou")

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Tasks
    fields = "__all__"
    success_url = reverse_lazy("students:thankyou")

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Tasks
    template_name = 'students/tasks_confirm_delete.html'
    success_url = reverse_lazy("students:list_students")

class TasksDetailView(DetailView):
    model = Tasks
    success_url = reverse_lazy("students:thankyou")



class TaskUploadView(View) :
    form_class = TaskUploadForm
    template_name = 'task_upload.html'
    success_url = reverse_lazy("students:thankyou")


    def get(self, request, *args, **kwargs) :
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs) :
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid() :
            file = form.cleaned_data['file']
            try :
                data = json.load(file)
                student_id = kwargs.get('pk')
                student = Student.objects.get(pk=student_id)

                tasks = [
                    Tasks(
                        student=student,
                        tsk_due_date=task['tsk_due_date'],
                        subject=task['subject'],
                        status=task.get('status', 'o'),
                        start_date=task['start_date'],
                        close_date=task.get('close_date', None),
                    )
                    for task in data
                ]
                Tasks.objects.bulk_create(tasks)
                return redirect("thankyou")
            except (json.JSONDecodeError, ValidationError) as e :
                form.add_error(None, f"Invalid file format or data: {e}")
        return render(request, self.template_name, {'form' : form})