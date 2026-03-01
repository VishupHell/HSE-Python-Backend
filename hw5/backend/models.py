import uuid

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    def __str__(self):
        return "User: {0}, birthday: {1}".format(self.name, self.birthday)

class Post(models.Model):
    post = models.TextField()
    post_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Post from user: {0}".format(self.user_id)

class Comment(Post):
    from_comment_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="parent_comment")

    def __str__(self):
        return "Comment from user: {0}".format(self.user_id)