from django.shortcuts import render
from .forms import ReportForm, ProblemReportedForm

# Create your views here.


def report_view(request):
    r_form = ReportForm()
    pr_form = ProblemReportedForm()

    context = {
        'r_form': r_form,
        'pr_form': pr_form,
    }

    return render(request, 'reports/report.html', context)
