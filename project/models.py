from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField() #cm
    weight = models.PositiveIntegerField() #kg
    age = models.PositiveIntegerField()
    biological_sex_is_male = models.BooleanField()
    override_calorie_goal = models.PositiveIntegerField(null = True, blank= True) #kcal

    def bmi(self):
        return self.weight / (self.height / 100) ** 2
    
    def __str__(self):
        return self.user.username
    
class Food(models.Model):
    name = models.CharField(max_length=50)
    serving_size = models.PositiveIntegerField() #g
    calories = models.PositiveIntegerField() #kcal

    def __str__(self):
        return self.name

class Entry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    create_time = models.DateTimeField()
    serving_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.user.username} {self.food.name} {self.create_time}'
    


class DailyReport(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    calories_intake = models.PositiveIntegerField()
    calories_excess_or_deficency = models.IntegerField()

    def __str__(self):
        return f'{self.user.user.username} {self.date}'



