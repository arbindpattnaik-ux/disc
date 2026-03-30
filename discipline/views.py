from django.shortcuts import render
from .models import DisciplineRecord

def dashboard(request):
    records = DisciplineRecord.objects.all().order_by('-incident_date')
    return render(request, 'dashboard.html', {'records': records})
