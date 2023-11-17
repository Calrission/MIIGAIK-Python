import urllib.request
import re
import csv

regex = r"""
(?:org-widget-header__title\">[^\/]+)(?P<url>[^\"]+)(?:[^>]+>)(?P<title>[^<]+)
(?:[^\n]+)(?:(?:(?:[^>]+>){2}\n[^<]+<\/span>\n[^<]+
<span class=\"org-widget-header__meta org-widget-header__meta--location\">\n|
(?:[^>]+>){2}\n))(?:\s+)(?P<address>[^\n]+)(?:[^+Т]+)Телефон(?:(?:[^>]+>){3})(?P<phones>[\d (),+-]+)
(?:[^\n]+\n){4}(?:[^>]+>)(?P<time_work>[^<]+|)"""

with open("results.csv", "a+") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(("url_spravker", "title", "address", "phones", "work_time"))
    for page in range(1, 6):
        response = urllib.request.urlopen(
            f"https://msk.spravker.ru/avtoservisy-avtotehcentry/?page={page}").read().decode()
        results = re.findall(regex, response)
        writer.writerows(results)
        print(f"Страница №{page} спаршена")
