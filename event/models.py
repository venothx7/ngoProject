from django.db import models

# Create your models here.
class Event(models.Model):
    
    CONFERENCE = 'c'
    SEMINAR = 's'
    PRESENTATION = 'p'
    CATEGORY_CHOICES = [
        (CONFERENCE, 'Conference'),
        (SEMINAR, 'Seminar'),
        (PRESENTATION, 'Presentation'),
    ]
    

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default=CONFERENCE,
    )
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    start_time = models.TimeField(auto_now_add=False, blank = True)
    end_time = models.TimeField(auto_now_add=False, blank = True)
    location = models.CharField(max_length=100, blank = True)
    register = models.BooleanField(default=False)
    image = models.ImageField(default="img/no_image.png")
    adult_price = models.DecimalField(max_digits=10, decimal_places=2)
    child_price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ('start_date',)

    def __str__(self):
        return f'{self.name} ({self.id})'
        
    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user', args=[str(self.id)])