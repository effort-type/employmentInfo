import csv
import openpyxl as op

def save_to_file_xlsx(jobs):
    wb = op.Workbook()
    sheet = wb.active
    sheet.append(["title", "company", "location", "link"])

    for job in jobs:
        sheet.append(list(job.values()))

    wb.save("job.xlsx")
    return

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return