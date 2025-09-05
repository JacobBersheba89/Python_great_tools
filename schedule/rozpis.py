import itertools
from openpyxl import Workbook
from datetime import datetime, timedelta
from collections import defaultdict

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
long_days = ["Pondělí", "Středa"]  # dlouhé směny

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

# 🔹 Funkce pro generování spravedlivého rozpisu
def generate_fair_schedule(pairs, extra, start_date):
    schedule = []
    pair_cycle = itertools.cycle(pairs)
    extra_index = 0

    # sledujeme počet dlouhých směn pro každého účastníka
    long_shift_count = defaultdict(int)

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
                schedule.append((cz_weekdays[date.strftime('%a')], date.strftime('%d.%m.%Y'),
                                 f"STÁTNÍ SVÁTEK – {holiday_name}", f"STÁTNÍ SVÁTEK – {holiday_name}"))
                continue

            pair = next(pair_cycle)

            # každý sudý týden otočíme role (telefon ↔ osobně)
            if (week + 1) % 2 == 0:
                phone, desk = pair[1], pair[0]
            else:
                phone, desk = pair[0], pair[1]

            # Spravedlivé vměšování Jakuba – střídá role a páry rovnoměrně
            if day_name in ["Úterý", "Čtvrtek"]:
                if extra_index % 2 == 0:
                    phone = extra
                else:
                    desk = extra
                extra_index += 1

            # Vyvážení dlouhých směn
            if day_name in long_days:
                # vybereme toho z dvojice s menším počtem dlouhých směn pro telefon
                if long_shift_count[phone] > long_shift_count[desk]:
                    phone, desk = desk, phone
                long_shift_count[phone] += 1
                long_shift_count[desk] += 1

            schedule.append((cz_weekdays[date.strftime('%a')], date.strftime('%d.%m.%Y'), phone, desk))

        week += 1
        current_date = start_date + timedelta(weeks=week)
    return schedule

# 🔹 Generování rozpisu do konce roku
schedule = generate_fair_schedule(pairs, extra, start_date)

# 🔹 Export do Excelu s prázdným řádkem mezi týdny
wb = Workbook()
ws = wb.active
ws.title = "Rozpis služeb"

# Hlavička
ws.append(["Den", "Datum", "Telefon", "Osobně"])

current_week = 0
for row_index, row in enumerate(schedule):
    week_number = row_index // 5 + 1
    if current_week and week_number != current_week:
        ws.append([])  # prázdný řádek mezi týdny
    ws.append(row)
    current_week = week_number

# Uložení souboru
wb.save("rozpis_infolinka_fair.xlsx")
print("✅ Rozpis vygenerován do souboru rozpis_infolinka_fair.xlsx")
