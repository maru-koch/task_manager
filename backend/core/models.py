from django.db import models
from uuid import uuid4
from core.account.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

TASK_STATUS = (
    ("todo", "ToDo"),
    ("in progress", "In Progress"),
    ("completed", "Completed"),
)

class Task(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=200, default="todo", choices=TASK_STATUS)

    @property
    def total(self):
        return self.objects.count()
    
    # @property
    # def completed(self):
    #     """Returns the total number of completed tasks."""
    #     return self.objects.filter(completed=True).count()
    
    # @property
    # def pending(self):
    #     return self.objects.filter(completed=False).count()
    
    class Meta:
        ordering = ["-created_at"]

class Notification(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

@receiver(signal=post_save, sender=Notification)
def notify_task_completed(sender, instance, created, **kwargs):
    """Prints a notification when a new task is created. """
    print(f"Task-{instance.task.title} created by {instance.task.user.first_name}")