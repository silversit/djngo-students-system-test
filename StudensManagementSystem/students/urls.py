from django.urls import  path
from . import  views
app_name = "students"

urlpatterns = [
    path("", views.HomeView.as_view(),name="home"),
    path("thank_you/", views.ThankYou.as_view(),name="thankyou"),
    path("contact/", views.ContactFormView.as_view(),name="contact"),
    path("create_student/", views.CreateStudentView.as_view(),name="create_student"),
    path("list_students/", views.StudentListView.as_view(), name="list_students"),
    path("list_students/student_detail/<int:pk>", views.StudentDetailView.as_view(), name="student_detail"),
    path("student_update/<int:pk>",views.StudentUpdateView.as_view(), name="update_student"),
    path("student_delete/<int:pk>",views.StudentDeleteView.as_view(),name="student_delete"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('logout/',views.user_logout,name='logout'),
    path("grades_add/",views.AddGrageView.as_view(),name="grades_add"),
    path('contacts/', views.ContactListView.as_view(), name='contacts_list'),
]