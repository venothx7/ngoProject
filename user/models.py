from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _



class CustomUser(AbstractUser):
    ADMIN = 'a'
    USER ='u'
    ROLE_CHOICES =(
        (ADMIN,'Admin'),
        (USER,'User'),
    )

    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    role = models.CharField(
        choices=ROLE_CHOICES, 
        max_length=5, 
        default =USER)

    username = None
    email = models.EmailField(_('email address'), unique=True)

    username = models.CharField( max_length=150, unique= True)
    def save(self, *args,**kwargs):
        self.set_password(self.password)
        self.username = self.email
        self.email = self.username
        if self.role is 'a':
            self.is_staff = True
            self.is_superuser = True
        super().save(*args,**kwargs)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return f'{self.first_name} ({self.id})'
        
    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user', args=[str(self.id)])
