import io_helpers
from invoke import task

@task
def csvsToExcel(c, csv_path, excel_filename):
    io_helpers.csvs_to_excel(csv_path, excel_filename)