from django.urls import path
from CSV_Frontend.Frontend_Schemas import views

urlpatterns = [
    # CRUD Schema and column model
    path('create_schema_ajax/', views.CreateSchemaAjaxView.as_view(), name='create_schema'),
    path('schema/<int:schema_id>/edit/', views.EditSchemaAjaxView.as_view(), name='edit_schema'),
    path('schema/<int:schema_id>/delete/', views.DeleteSchemaAjaxView.as_view(), name='delete_schema'),

    # Download Schema and column model
    path('schema/<int:schema_id>/export/', views.ExportView.as_view(), name='export'),
]
