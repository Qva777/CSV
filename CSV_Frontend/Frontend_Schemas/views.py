from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.forms import modelformset_factory
from django.views.generic import View

from CSV_Backend.Columns.models import Column
from CSV_Backend.Schemas.models import Schema
import csv


class CreateSchemaAjaxView(View):
    """ Create Schema Ajax """
    template_name = 'schema/create_schema.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        if name:
            schema = Schema(name=name)
            schema.save()
            return redirect('generate_columns')
        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(csrf_exempt, name='dispatch')
class EditSchemaAjaxView(View):
    """ Edit Schema Ajax """
    template_name = 'schema/edit_schema.html'

    def get(self, request, schema_id, *args, **kwargs):
        schema = get_object_or_404(Schema, pk=schema_id)
        columns = Column.objects.filter(schema=schema)
        ColumnFormSet = modelformset_factory(Column, fields=(
            'id', 'full_name', 'age', 'email', 'phone', 'job', 'company', 'address', 'domain', 'text', 'integer',
            'date'), extra=0)

        formset = ColumnFormSet(queryset=columns)
        context = {
            'formset': formset,
            'schemas': schema,
        }
        return render(request, self.template_name, context)

    @staticmethod
    def patch(request, schema_id, *args, **kwargs):
        schema = get_object_or_404(Schema, pk=schema_id)
        columns = Column.objects.filter(schema=schema)
        ColumnFormSet = modelformset_factory(Column, fields=(
            'id', 'full_name', 'age', 'email', 'phone', 'job', 'company', 'address', 'domain', 'text', 'integer',
            'date'), extra=0)

        formset = ColumnFormSet(request.POST, queryset=columns)

        if formset.is_valid():
            formset.save()
            return redirect('home')
        else:
            return JsonResponse({'success': False, 'errors': formset.errors})

    def post(self, request, schema_id, *args, **kwargs):
        return self.patch(request, schema_id, *args, **kwargs)


class ExportView(View):
    """ Download schema and column  """

    @staticmethod
    def get(request, schema_id):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="columns.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['Full name', 'Age', 'Email', 'Phone', 'Job', 'Company', 'Address', 'Text', 'Integer', 'Domain', 'Date'])

        columns = Column.objects.filter(schema__id=schema_id).values_list(
            'full_name', 'age', 'email', 'phone', 'job', 'company', 'address', 'text', 'integer', 'domain', 'date')
        for column in columns:
            writer.writerow(column)

        return response


class DeleteSchemaAjaxView(View):
    """Delete Schema Ajax"""

    @staticmethod
    def post(request, schema_id):
        schema = get_object_or_404(Schema, pk=schema_id)
        schema.delete()
        return redirect('home')
