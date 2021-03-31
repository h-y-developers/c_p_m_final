from django_filters import CharFilter,AllValuesFilter
from .models import Achievement,User
import django_filters


class AchievementFilter(django_filters.FilterSet):
    class Meta:
        model = Achievement
        fields = ['certificate_name','field_type','issuer_name']



# class AchievementFilter(django_filters.FilterSet):
#     name = CharFilter(field_name='name', lookup_expr='icontains', label='', )
#     type = AllValuesFilter(field_name='type', choices=Achievement.objects.values_list('type', flat=True).distinct(), label='', )

#     class Meta:
#         model = Achievement
#         fields = ''
#         exclude = ['']
