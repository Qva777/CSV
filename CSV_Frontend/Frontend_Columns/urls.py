from django.urls import path
from CSV_Frontend.Frontend_Columns.views import GenerateColumnsView

urlpatterns = [
    # Generate column for Schema
    path('generate_columns/', GenerateColumnsView.as_view(), name='generate_columns'),
]
