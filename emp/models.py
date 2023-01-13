from django.db import models
from account.models import User

class Position(models.Model):
    name_position = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name_position}'

class Employees(models.Model):
    fullname = models.CharField(max_length=40)
    birth_date = models.DateField()
    position = models.ForeignKey(Position ,on_delete=models.CASCADE)
    salary = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fullname} - {self.position.name_position}'


