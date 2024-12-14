from django.db import models

class IconsForDesktop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icons/')
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BottomSideIcons(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icons/')
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HandGest(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='hand_gestures_images')
    func = models.CharField(max_length=255 , default=" ")

    class Meta:
        verbose_name_plural = "HandGest"

    def __str__(self):
            return self.name


class CommandHistory(models.Model):
    command = models.CharField(max_length=200)
    output = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.command

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
