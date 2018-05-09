from django.db import models

# Create your models here.
# class details(models.Model):
#     Name = models.CharField(max_length=100)
#     USN = models.CharField(max_length=100)
#     Sem = models.CharField(max_length=100)
#     Branch = models.CharField(max_length=100)
#     clgVisited = models.CharField(max_length=100)
#     EventDate = models.CharField(max_length=100)
#     EventName = models.CharField(max_length=100)
#     Description = models.CharField(max_length=100)

class table(models.Model):
    Name = models.CharField(max_length=100)
    USN = models.CharField(max_length=100)
    Sem = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    clgVisited = models.CharField(max_length=100)
    EventDateStart = models.CharField(max_length=100)
    EventDateEnd = models.CharField(max_length=100)
    EventName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)


class StuRecord(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    sem = models.CharField(max_length=5, blank=True, null=True)
    department_id = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_record'
