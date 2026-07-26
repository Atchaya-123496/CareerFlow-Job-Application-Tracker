from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    
    #hr dashboard
    path("hr/dashboard/", views.hr_dashboard, name="hr_dashboard"),

    

    # Job Management
    path("add-job/", views.add_job, name="add_job"),
    path("edit-job/<int:id>/", views.edit_job, name="edit_job"),
    path("delete-job/<int:id>/", views.delete_job, name="delete_job"),

    # HR
    path("view-candidate/<int:id>/", views.view_candidate, name="view_candidate"),

    # Notifications (Future)
    path("notifications/", views.notifications, name="notifications"),


]