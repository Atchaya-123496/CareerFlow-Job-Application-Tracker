from .models import JobApplication


def notification_count(request):

    if request.user.is_authenticated:

        jobs = JobApplication.objects.filter(user=request.user)

        print("Unread:", jobs.filter(notification_read=False).count())

        return {
            "unread_notifications": jobs.filter(notification_read=False).count()
        }

    return {"unread_notifications": 0}