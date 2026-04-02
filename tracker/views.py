from django.shortcuts import render
from reports.models import Report


STATUS_STEPS = ['Submitted', 'Assigned', 'In Progress', 'Resolved']


def track_report(request):
    ticket = None
    error = None

    if request.method == 'POST':
        ref_number = request.POST.get('ref_number', '').strip().upper()
        try:
            report = Report.objects.get(ref_number=ref_number)
            current_index = STATUS_STEPS.index(report.status) if report.status in STATUS_STEPS else 0

            steps = []
            for i, step in enumerate(STATUS_STEPS):
                steps.append({
                    'label': step if step != 'Assigned' else 'Assigned to Field Team',
                    'done': i <= current_index,
                    'date': report.updated_at.strftime('%d %b %Y, %H:%M') if i == current_index else
                            report.submitted_at.strftime('%d %b %Y, %H:%M') if i == 0 else '',
                })

            ticket = {
                'ref': report.ref_number,
                'issue': report.issue_type,
                'address': report.street_address,
                'submitted': report.submitted_at.strftime('%d %b %Y, %H:%M'),
                'status': report.status,
                'steps': steps,
            }
        except Report.DoesNotExist:
            error = f'No report found for "{ref_number}". Please check and try again.'

    return render(request, 'tracker/track.html', {
        'ticket': ticket,
        'error': error,
    })
