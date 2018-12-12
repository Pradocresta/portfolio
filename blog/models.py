from django.db import models

# Create your models here.
    # title, pub_date, body, image
# Create A blog models
# Add the blog app to the settings
# migrate
#Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    b_content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def shortDetails(self):
        return self.b_content[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e %Y')
