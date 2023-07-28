from django.db import models

# Create your models here.
class BlogPost(models.Model):
    
    class Meta:
        app_label = 'blog'
    
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived") ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default="draft")
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Comment on {self.post.title}"
