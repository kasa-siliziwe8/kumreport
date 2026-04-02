from django.shortcuts import render
import uuid
from .models import Report


def report_submission(request):
    if request.method == 'POST':
        street_address = request.POST.get('street_address', '')
        issue_type = request.POST.get('issue_type', '')
        details = request.POST.get('details', '')

        ref_number = 'KMR-2026-' + str(uuid.uuid4())[:5].upper()

        report = Report.objects.create(
            ref_number=ref_number,
            street_address=street_address,
            issue_type=issue_type,
            details=details,
            status='Submitted',
        )

        context = {
            'ref_number': ref_number,
            'street_address': street_address,
            'issue_type': issue_type,
            'submitted_at': report.submitted_at.strftime('%d %b %Y, %H:%M'),
            'success': True,
        }
        return render(request, 'reports/submission.html', context)

    return render(request, 'reports/submission.html', {'success': False})
