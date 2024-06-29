from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView,ListView,TemplateView,FormView,DeleteView
from .forms import ContactForm
from .models import Student,Grades,Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login_required
from django.contrib.auth import logout
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