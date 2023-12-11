from django.urls import path
from .views import TaskList ,TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, TaskReorder, Logout_User
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.Logout_User , name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('create-task/',TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]