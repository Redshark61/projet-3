from django.db import models
from django.contrib.auth.models import User as UserAuth
# Create your models here.


class Diseases(models.Model):

    name = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=1000)
    cures = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"


class RPPS(models.Model):

    rpps_id = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rpps_id} : {self.firstname} {self.lastname}"


class Job(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return f"{self.address}, {self.city} {self.postal_code}"


class User(models.Model):

    class Genders(models.TextChoices):
        MASCULIN = "M"
        FEMININ = "F"

    user = models.ForeignKey(UserAuth, on_delete=models.CASCADE, related_name="user", null=True)
    mail = models.EmailField(null=True)
    gender = models.CharField(max_length=1, choices=Genders.choices, null=True)
    main_doctor = models.ForeignKey("self", on_delete=models.SET_NULL,
                                    null=True, related_name="User_main_doctor")
    parent1 = models.ForeignKey("self", on_delete=models.SET_NULL, null=True,
                                blank=True, related_name="User_parent1")
    parent2 = models.ForeignKey("self", on_delete=models.SET_NULL, null=True,
                                blank=True, related_name="User_parent2")
    address = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField()


class TrustedPerson(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20)


class UserDisease(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_id = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    isCurrent = models.BooleanField(default=True)


class Doctor(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rpps = models.ForeignKey(RPPS, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)


class Appointment(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    description = models.TextField()


class Treatment(models.Model):

    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    prescription = models.TextField()
    end_date = models.DateField(null=True, blank=True)
    is_permanent = models.BooleanField(default=False)
