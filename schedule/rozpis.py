import itertools
from openpyxl import Workbook
from datetime import datetime, timedelta
import random

# 🔹 Zadání vstupních dat
pairs = [
    ("Irena", "Alča"),
    ("Kristina", "JanaD"),
    ("Víťa", "Michal"),
    ("Filip", "Zdeněk"),
    ("Petra", "Lucka"),
    ("Miloš", "JanaG")
]

extra = "Jakub"   # extra osoba
start_date = datetime(2025, 9, 8)  # první pondělí
days = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]
long_days = ["Pondělí", "Středa"]
cz_weekdays = {"Mon":"Pondělí","Tue":"Úterý","Wed":"Středa","Thu":"Čtvrtek","Fri":"Pátek"}

holidays_2025 = {
    (1,1):"Nový rok",(1,5):"Svátek práce",(8,5):"Den vítězství",
    (5,7):"Den slovanských věrozvěstů Cyrila a Metoděje",
    (6,7):"Den upálení mistra Jana Husa",(28,9):"Den české státnosti",
    (28,10):"Den vzniku samostatného československého státu",(17,11):"Den boje za svobodu a demokracii",
    (24,12):"Štědrý den",(25,12):"1. svátek vánoční",(26,12):"2. svátek vánoční"
}

def generate_schedule_random_jakub(pairs, extra, start_date):
    schedule = []
    pair_cycle = itertools.cycle(pairs)
    end_date = datetime(start_date.year, 12, 31)
    week = 0

    while True:
        monday = start_date + timedelta(weeks=week)
        for i, day_name in enumerate(days):
            date = monday + timedelta(days=i)
            if date > end_date:
                return schedule

            # státní svátek
            if (date.day, date.month) in holidays_2025:
                holiday_name = holidays_2025[(date.day, date.month)]
                schedule.append((cz_weekdays[date.strftime('%a')], date.strftime('%d.%m.%Y'),
                                 f"STÁTNÍ SVÁTEK – {holiday_name}", f"STÁTNÍ SVÁTEK – {holiday_name}"))
                continue

            pair = next(pair_cycle)

            # role otočeny každým sudým týdnem
            if (week + 1) % 2 == 0:
                phone, desk = pair[1], pair[0]
            else:
                phone, desk = pair[0], pair[1]

            # Jakub se vmísí náhodně jen do každého druhého týdne
            if (week + 1) % 2 == 0:
                if random.choice([True, False]):  # náhodně vyber, zda se Jakub objeví tento den
                    if random.choice([True, False]):
                        phone = extra
                    else:
                        desk = extra

            # vyvážení dlouhých směn (pro přehlednost)
            if day_name in long_days:
                # prosté otočení, aby se střídaly role
                if week % 2 == 0:
                    phone, desk = desk, phone

            schedule.append((cz_weekdays[date.strftime('%a')], date.strftime('%d.%m.%Y'), phone, desk))

        week += 1

# 🔹 Generování rozpisu do konce roku
schedule = generate_schedule_random_jakub(pairs, extra, start_date)

# 🔹 Export do Excelu s prázdným řádkem mezi týdny
wb = Workbook()
ws = wb.active
ws.title = "Rozpis služeb"
ws.append(["Den","Datum","Telefon","Osobně"])

current_week = 0
for row_index, row in enumerate(schedule):
    week_number = row_index // 5 + 1
    if current_week and week_number != current_week:
        ws.append([])
    ws.append(row)
    current_week = week_number

wb.save("rozpis_infolinka_random_jakub.xlsx")
print("✅ Rozpis vygenerován do souboru rozpis_infolinka_random_jakub.xlsx")
