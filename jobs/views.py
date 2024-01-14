from re import template
from django.http import Http404, HttpResponse
from django.shortcuts import loader, render

from jobs.models import Cities, Job, JobTypes


# Create your views here.
def joblist(request):
    job_list = Job.objects.order_by("job_type")
    template = loader.get_template("joblist.html")
    context = {"job_list": job_list}

    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job Does Not Exist")

    return render(request, "job.html", {"job": job})
