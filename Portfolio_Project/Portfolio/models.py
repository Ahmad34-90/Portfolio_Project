from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField( max_length=100)
    intro = models.TextField()
    image = models.ImageField(upload_to= 'profile/')

    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description= models.TextField()

    def __str__(self):
        return self.title

    def duration(self):
        return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}" 

class Projects(models. Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    image = models.ImageField(upload_to="projects/")
    github_link = models.URLField(blank=True)
    live_link =  models.URLField(blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
