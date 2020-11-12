
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('adminindex/', views.adminindex, name='adminindex'),

    #Path for welcome url
    path('adminwelcome/', views.adminwelcome, name='adminwelcome'),
    path('welcome/', views.welcome, name='welcome'),
    path('adminleadership/', views.adminleadership, name='adminleadership'),
    path('leadership/', views.leadership, name='leadership'),
    path('runonews/<int:news_id>/', views.runonews, name='runonews'),
    path('adminrunonews/<int:news_id>/', views.adminrunonews, name='adminrunonews'),
    path('adminaboutus/', views.adminaboutus, name='adminaboutus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('admission/', views.admission, name='admission'),
    path('adminadmission/', views.adminadmission, name='adminadmission'),
    path('footerUpdate/', views.footerUpdate, name='footerUpdate'),

    # This point below is related to the pupils and teachers
   
    path('teacher/', views.teacher, name='teacher'),
    path('result/', views.result, name='result'),
    path('remark/', views.principalRemark, name='principalRemark'),
    path('approval/', views.principalApproval, name='principalApproval'),
    path('pupil/', views.pupil, name='pupil'),
    path('regpupil', views.regpupil, name='regpupil'),
    path('basicdata/', views.basicdata, name='basicdata'),
    path('teacherprofile/', views.teacherprofile, name='teacherprofile'),
    path('pupildetails/', views.pupildetails, name='pupildetails'),
    path('changepass/', views.changepass, name='changepass'),
    path('forgotpass/', views.forgotpass, name='forgotpass'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('editStudent/', views.editStudentProfile, name='editStudentProfile'),
    path('editstudProfile', views.editstudProfile, name='editstudProfile')
]