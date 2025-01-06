import django_filters
from .models import Student
from django.db.models import Q
class StudentFilter(django_filters.FilterSet):
    # Lọc theo search_query (tìm kiếm theo tên, email, địa chỉ)
    search_query = django_filters.CharFilter(method='filter_by_search_query', label='Search')

    # Lọc theo năm học (academic_year)
    academic_years = django_filters.MultipleChoiceFilter(
        field_name='academic_year',
        choices=[(year, year) for year in Student.objects.values_list('academic_year', flat=True).distinct()],
        label='Select Academic Years',
    )

    def filter_by_search_query(self, queryset, name, value):
        if value:
            search_terms = value.split()
            query = Q()
            for term in search_terms:
                query |= Q(name__icontains=term) | Q(email__icontains=term) | Q(address__icontains=term)
            queryset = queryset.filter(query)
        return queryset

    class Meta:
        model = Student
        fields = ['academic_years', 'search_query']
