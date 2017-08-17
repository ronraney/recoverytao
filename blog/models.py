from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #Post class defines a Post object or model, specifically a Django model 
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save() #this method will assign the current time to the published_date field in the Post model, and run the save method
        
    def __str__(self):
        return self.title #this method returns a string - the title
        
        