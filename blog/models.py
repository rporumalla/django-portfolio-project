from django.db import models

# Create a blog model
class Blog(models.Model):
    # title
    title = models.CharField(max_length=255)

    # pub_date
    pub_date = models.DateTimeField()

    # body
    body = models.TextField()

    # image
    image = models.ImageField(upload_to='images/')

# Add the blog app to the settings

# Create a migration
# python manage.py makemigrations

# Migrate
# python manage.py migrate

# Add to the admin
