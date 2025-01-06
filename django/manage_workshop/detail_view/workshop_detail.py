from django.shortcuts import get_object_or_404, render
from ..models import Workshop


def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    other_workshops = Workshop.objects.exclude(id=pk)[:5]
    return render(request, 'manage_workshop/workshop_detail.html', {
        'workshop': workshop,
        'other_workshops': other_workshops,})
