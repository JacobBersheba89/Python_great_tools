import itertools
from openpyxl import Workbook
from datetime import datetime, timedelta

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

# Startovací pondělí
start_date = datetime(2025, 9, 8)  # první pondělí

# Dny týdne (Po–Pá)
days = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]

# Mapování anglických zkratek na české názvy
cz_weekdays = {
    "Mon": "Pondělí",
    "Tue": "Úterý",
    "Wed": "Středa",
    "Thu": "Čtvrtek",
    "Fri": "Pátek",
    "Sat": "Sobota",
    "Sun": "Neděle"
}

# 🔹 Seznam státních svátků v roce 2025 (den, měsíc) → název svátku
holidays_2025 = {
    (1, 1): "Nový rok",
    (1, 5): "Svátek práce",
    (8, 5): "Den vítězství",
    (5, 7): "Den slovanských věrozvěstů Cyrila a Metoděje",
    (6, 7): "Den upálení mistra Jana Husa",
    (28, 9): "Den české státnosti",
    (28, 10): "Den vzniku samostatného československého státu",
    (17, 11): "Den boje za svobodu a demokracii",
    (24, 12): "Štědrý den",
    (25, 12): "1. svátek vánoční",
    (26, 12): "2. svátek vánoční"
}

# 🔹 Funkce pro generování rozpisu
def generate_schedule(pairs, extra, start_date):
    schedule = []
    pair_cycle = itertools.cycle(pairs)
    extra_index = 0

    end_date = datetime(start_date.year, 12, 31)
    current_date = start_date
    week = 0

    while current_date <= end_date:
        monday = start_date + timedelta(weeks=week)
        for i, day_name in enumerate(days):
            date = monday + timedelta(days=i)
            if date > end_date:
                break

            # pokud je státní svátek, zaznačit ho s názvem
            if (date.day, date.month) in holidays_2025:
                holiday_name = holidays_2025[(date.day, date.month)]
                date_str = f"{date.strftime('%d.%m.%Y')} ({cz_weekdays[date.strftime('%a')]})"
                schedule.append((f"Týden {week+1}", date_str, f"STÁTNÍ SVÁTEK – {holiday_name}", f"STÁTNÍ SVÁTEK – {holiday_name}"))
                continue

            pair = next(pair_cycle)

            # každý sudý týden otočíme role (telefon ↔ osobně)
            if (week + 1) % 2 == 0:
                phone, desk = pair[1], pair[0]
            else:
                phone, desk = pair[0], pair[1]

            # Jakub se vměšuje cca 2× týdně (út, čt)
            if day_name in ["Úterý", "Čtvrtek"] and extra_index % len(pairs) == 0:
                if (week + 1) % 2 == 0:
                    desk = extra
                else:
                    phone = extra
                extra_index += 1

            date_str = f"{date.strftime('%d.%m.%Y')} ({cz_weekdays[date.strftime('%a')]})"
            schedule.append((f"Týden {week+1}", date_str, phone, desk))
        week += 1
        current_date = start_date + timedelta(weeks=week)
    return schedule

# 🔹 Generování rozpisu do konce roku
schedule = generate_schedule(pairs, extra, start_date)

# 🔹 Export do Excelu
wb = Workbook()
ws = wb.active
ws.title = "Rozpis služeb"

# Hlavička
ws.append(["Týden", "Datum", "Telefon", "Osobně"])

# Data
for row in schedule:
    ws.append(row)

# Uložení souboru
wb.save("rozpis_infolinka_do_konce_roku_s_svatky_nazvy.xlsx")
print("✅ Rozpis vygenerován do souboru rozpis_infolinka_do_konce_roku_s_svatky_nazvy.xlsx")
