from django.shortcuts import render, redirect, get_object_or_404
from reports.models import Report

ADMIN_PASSWORD = 'kumreport2026'


def admin_login(request):
    error = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('admin_dashboard')
        else:
            error = 'Incorrect password. Please try again.'
    return render(request, 'adminpanel/login.html', {'error': error})


def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    reports = Report.objects.all().order_by('-submitted_at')
    return render(request, 'adminpanel/dashboard.html', {'reports': reports})


def update_status(request, report_id):
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    if request.method == 'POST':
        report = get_object_or_404(Report, id=report_id)
        new_status = request.POST.get('status')
        if new_status in ['Submitted', 'Assigned', 'In Progress', 'Resolved']:
            report.status = new_status
            report.save()

    return redirect('admin_dashboard')


def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')
