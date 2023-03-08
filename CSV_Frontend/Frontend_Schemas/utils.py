# import csv
# import os
#
# def generate_csv_file(schema, from_age, to_age, num_fields, fields):
#     # Define the filename for the CSV file
#     filename = f'{schema.name}_{from_age}-{to_age}_{num_fields}fields.csv'
#     filepath = os.path.join('media', filename)
#
#     # Generate the rows of data for the CSV file
#     rows = []
#     for i in range(int(num_fields)):
#         row = [f'field_{i+1}']
#         for age in range(int(from_age), int(to_age)+1):
#             row.append(f'{age}')
#         rows.append(row)
#
#     # Write the rows of data to the CSV file
#     with open(filepath, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['field_name'] + [f'age_{i}' for i in range(int(from_age), int(to_age)+1)])
#         for row in rows:
#             writer.writerow(row)
#
#     return filename
