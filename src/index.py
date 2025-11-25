from services.weather_service import WeatherService


def main():
    service = WeatherService()

    while True:
        print("\n1 - Lisää paikka")
        print("2 - Näytä paikat")
        print("3 - Poista paikka")
        print("4 - Näytä sää")
        print("0 - Lopeta")

        choice = input("Valinta: ")

        if choice == "1":
            location = input("Paikka: ")
            if service.add_location(location):
                print("Lisätty!")
            else:
                print("Oli jo listalla")

        elif choice == "2":
            locations = service.get_locations()
            print("Paikat:", ", ".join(locations) if locations else "Tyhjä")

        elif choice == "3":
            location = input("Poista: ")
            if service.remove_location(location):
                print("Poistettu!")
            else:
                print("Ei löytynyt")

        elif choice == "4":
            location = input("Paikka: ")
            print(service.get_weather(location))

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
