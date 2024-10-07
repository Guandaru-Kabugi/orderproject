import django_filters

#working on filtering my orders using django filters
class OrderFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(field_name='job_title',lookup_expr='icontains')
    student_name = django_filters.CharFilter(field_name='student_name',lookup_expr='icontains')
    sent_date = django_filters.DateFilter(field_name='sent_date',lookup_expr='iexact')
    due_date = django_filters.DateFilter(field_name='due_date',lookup_expr='iexact')
    additional_notes = django_filters.CharFilter(field_name='additional_notes',lookup_expr='icontains')