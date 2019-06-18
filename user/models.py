from django.db import models

class User(models.Model):
    
    ADMIN = 'a'
    USER ='u'
    ROLE_CHOICES =(
        (ADMIN,'Admin'),
        (USER,'User'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    role = models.CharField(
        choices=ROLE_CHOICES, 
        max_length=5, 
        default =USER)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return f'{self.first_name} ({self.id})'
        
    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user', args=[str(self.id)])
