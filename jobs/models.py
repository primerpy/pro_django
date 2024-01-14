from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

DEGREE_TYPE = (("Bachelor", "Bachelor"), ("Master", "Master"), ("Doctor", "Doctor"))


JobTypes = [
    (0, "engineer"),
    (1, "product"),
    (2, "operation"),
    (3, "design"),
]

Cities = [
    (0, "NYC"),
    (1, "DC"),
    (2, "SF"),
]


# Create your models here.
class Job(models.Model):
    job_type = models.SmallIntegerField(
        blank=False, choices=JobTypes, verbose_name="Job Type"
    )

    job_name = models.CharField(max_length=250, blank=False, verbose_name="Job Name")
    job_city = models.SmallIntegerField(
        choices=Cities, blank=False, verbose_name="Job Location"
    )

    job_responsibilities = models.TextField(
        max_length=1024, verbose_name="Job Responsibilites"
    )
    job_requirements = models.TextField(max_length=200, verbose_name="Job Requirements")
    creator = models.ForeignKey(
        User, verbose_name="Creator", on_delete=models.SET_NULL, null=True
    )
    created_date = models.DateTimeField(
        verbose_name="Creation Time", default=datetime.now
    )
    modified_date = models.DateTimeField(
        verbose_name="Modified Time", default=datetime.now
    )
