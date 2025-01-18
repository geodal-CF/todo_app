from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class To_do(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()  # No character limit

  author = models.ForeignKey(User, on_delete=models.CASCADE)  # A foreign key to the User model, linking each To-Do item to its unique creator. If the associated user is deleted, their To-Do items are also deleted.

  created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is first created.
  updated_at = models.DateTimeField(auto_now=True)  # Automatically updated whenever the object is updated.

  def get_absolute_url(self):
        """
        Returns the URL to access the detail view of this To-Do item.
        """
        return reverse("project_detail", kwargs={"pk": self.pk})

  def __str__(self):
        """
        Returns a string representation of the To-Do item, displaying its title.
        """
        return self.title