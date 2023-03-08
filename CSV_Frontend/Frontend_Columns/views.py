from faker import Faker
from django.views import View
from django.shortcuts import render, redirect

from CSV_Backend.Columns.models import Column
from CSV_Backend.Schemas.models import Schema

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

fake = Faker()


@method_decorator(csrf_exempt, name='dispatch')
class GenerateColumnsView(View):
    """ Generate Column for Schema """
    template_name = 'schema/generate_columns.html'

    def get(self, request, *args, **kwargs):
        schemas = Schema.objects.all()
        return render(request, self.template_name, {'schemas': schemas})

    def post(self, request, *args, **kwargs):
        schemas = Schema.objects.all()
        from_age = request.POST.get('from_age')
        to_age = request.POST.get('to_age')
        num_fields = request.POST.get('num_fields')
        selected_fields = request.POST.getlist('fields[]')
        if from_age and to_age and num_fields:
            try:
                from_age = int(from_age)
                to_age = int(to_age)
                num_fields = int(num_fields)
                columns = []
                for i in range(num_fields):
                    column = Column()

                    if 'schema' in request.POST:
                        schema_id = request.POST.get('schema')
                        schema = Schema.objects.get(pk=schema_id)
                        column.schema = schema

                    if 'full_name' in selected_fields:
                        column.full_name = fake.name()
                    if 'age' in selected_fields:
                        column.age = fake.random_int(min=from_age, max=to_age)
                    if 'job' in selected_fields:
                        column.job = fake.job()
                    if 'email' in selected_fields:
                        column.email = fake.email()
                    if 'domain' in selected_fields:
                        column.domain = fake.domain_name()
                    if 'phone' in selected_fields:
                        column.phone = fake.phone_number()
                    if 'company' in selected_fields:
                        column.company = fake.company()
                    if 'text' in selected_fields:
                        column.text = fake.text()
                    if 'integer' in selected_fields:
                        column.integer = fake.random_int(min=-100000, max=100000, step=1)
                    if 'address' in selected_fields:
                        column.address = fake.address()
                    if 'date' in selected_fields:
                        column.date = fake.date_this_century()
                    column.save()
                    columns.append(column)
                return redirect('home')
            except ValueError:
                pass
        return render(request, self.template_name, {'schemas': schemas})
