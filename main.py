from datetime import datetime
# Wybralem liste slownikow, poniewaz liczba pomiarow może sie zmieniac,
# a slownik pozwala odwolywać się do danych za pomoca czytelnych nazw:
# "datetime" oraz "temperature".
measurements = []

def read_datetime():
    #pobiera i sprawdza poprawność daty/godziny
    while True:
        date_text = input("Podaj datę i godzinę [RRRR-MM-DD GG:MM]: ").strip()

        if not date_text:
            print("Data i godzina nie mogą byc puste.")
            continue

        try:
            measurement_datetime = datetime.strptime(
                date_text,
                "%Y-%m-%d %H:%M"
            )
            return measurement_datetime
        except ValueError:
            print("Niepoprawny format daty i godziny.")
            print("Przyklad poprawnej wartosci: 2026-10-17 18:30")


def read_temperature():
    #pobiera temperature i sprawdza czy jest liczba
    while True:
        temperature_text = input("Podaj temperature w °C: ").strip()

        if not temperature_text:
            print("Temperatura nie może byc pusta.")
            continue

        # Pozwala wpisac zarowno 7.5, jak i 7,5.
        temperature_text = temperature_text.replace(",", ".")

        try:
            return float(temperature_text)
        except ValueError:
            print("Niepoprawna temperatura. Podaj liczbe.")


def add_measurement():
    #Dodaje nowy pomiar do historii.
    measurement_datetime = read_datetime()
    temperature = read_temperature()

    measurement = {
        "datetime": measurement_datetime,
        "temperature": temperature
    }
    measurements.append(measurement)
    measurements.sort(key=lambda item: item["datetime"]) # Sortowanie pomiarow wedlug daty i godziny.
    print("Pomiar zostal dodany.")


def show_measurements():
    #Wyświetla wszystkie zapisane pomiary.
    if not measurements:
        print("Historia pomiarow jest pusta.")
        return

    print("\n--- HISTORIA POMIARÓW ---")

    for number, measurement in enumerate(measurements, start=1):
        date_text = measurement["datetime"].strftime("%Y-%m-%d %H:%M")
        temperature = measurement["temperature"]

        print(f"{number}. {date_text} | {temperature:.2f} °C")


def calculate_statistics():
    #Oblicza i wyswietla statystyki temperatur.
    if not measurements:
        print("Brak pomiarow do obliczenia statystyk.")
        return

    temperatures = [
        measurement["temperature"]
        for measurement in measurements
    ]

    number_of_measurements = len(temperatures)
    minimum = min(temperatures)
    maximum = max(temperatures)
    average = sum(temperatures) / number_of_measurements
    temperature_range = maximum - minimum

    print("\n--- STATYSTYKI ---")
    print(f"Liczba pomiarow: {number_of_measurements}")
    print(f"Minimum: {minimum:.2f} °C")
    print(f"Maksimum: {maximum:.2f} °C")
    print(f"Srednia: {average:.2f} °C")
    print(f"Zakres: {temperature_range:.2f} °C")


def calculate_changes():
    #Analizuje zmiany pomiędzy kolejnymi pomiarami.
    if len(measurements) < 2:
        print("Do analizy zmian potrzebne są co najmniej dwa pomiary.")
        return

    changes = []
    increases = 0
    decreases = 0
    no_changes = 0

    print("\n--- ZMIANY POMIĘDZY POMIARAMI ---")

    for index in range(1, len(measurements)):
        previous_measurement = measurements[index - 1]
        current_measurement = measurements[index]

        previous_temperature = previous_measurement["temperature"]
        current_temperature = current_measurement["temperature"]

        change = current_temperature - previous_temperature
        changes.append(change)

        previous_date = previous_measurement["datetime"].strftime(
            "%Y-%m-%d %H:%M"
        )
        current_date = current_measurement["datetime"].strftime(
            "%Y-%m-%d %H:%M"
        )

        if change > 0:
            increases += 1
            description = "wzrost"
        elif change < 0:
            decreases += 1
            description = "spadek"
        else:
            no_changes += 1
            description = "bez zmiany"

        print(
            f"{previous_date} -> {current_date}: "
            f"{change:+.2f} °C ({description})"
        )

    biggest_increase = max(changes)
    biggest_decrease = min(changes)

    print("\n--- PODSUMOWANIE ZMIAN ---")

    if biggest_increase > 0:
        print(f"Najwiekszy wzrost: {biggest_increase:.2f} °C")
    else:
        print("Najwiekszy wzrost: brak")

    if biggest_decrease < 0:
        print(f"Najwiekszy spadek: {biggest_decrease:.2f} °C")
    else:
        print("Najwiekszy spadek: brak")

    print(f"Liczba wzrostow: {increases}")
    print(f"Liczba spadkow: {decreases}")
    print(f"Liczba przypadkow bez zmiany: {no_changes}")

    if increases > 0 and decreases == 0:
        trend = "temperatura ogolnie rosnie"
    elif decreases > 0 and increases == 0:
        trend = "temperatura ogolnie spada"
    elif increases > 0 and decreases > 0:
        trend = "zmiany sa mieszane"
    else:
        trend = "temperatura pozostaje bez zmian"

    print(f"Trend: {trend}.")


def show_menu():
    #Wyświetla menu programu.
    print("\n=== DZIENNIK TEMPERATURY ===")
    print("1. Dodaj pomiar")
    print("2. Wyswietl historie")
    print("3. Pokaż statystyki")
    print("4. Analiza zmian temperatury")
    print("0. Zakoncz")


def main():
    while True:
        show_menu()
        choice = input("Wybierz opcje: ").strip()

        if choice == "1":
            add_measurement()
        elif choice == "2":
            show_measurements()
        elif choice == "3":
            calculate_statistics()
        elif choice == "4":
            calculate_changes()
        elif choice == "0":
            break
        else:
            print("Niepoprawna opcja. Wybierz wartosc od 0 do 4.")

if __name__ == "__main__":
    main()