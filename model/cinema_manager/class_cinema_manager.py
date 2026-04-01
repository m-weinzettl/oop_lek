from model.movie.class_movie import Movie

class Cinema_Manager:
    def __init__(self):
        self.movies = []
        self.presentations = []

    def movie_catch(self):
        print("\n--- Neuen Film erfassen ---")
        title = input("Titel: ")
        try:
            duration = int(input("Dauer (Minuten): "))
            fsk = int(input("Altersfreigabe (FSK): "))

            new_movie = Movie(title, duration, fsk) 
            self.movies.append(new_movie)
            print(f"Erfolg: Film {new_movie} wurde gespeichert.")
        except ValueError:
            print("Fehler: Dauer und FSK müssen Zahlen sein!")

    def show_movies(self):
        print("\n--- Vorhandene Filme ---")
        if not self.movies:
            print("Keine Filme registriert.")
        else:
            for i, movies in enumerate(self.movies, 1):
                print(f"[{i}] {movies}")

    def presentation_catch(self):
        print("\n--- Neuen Vorstellung ---")

        if not self.movies:
            print("Fehler: Keine Filme vorhanden. Bitte zuerst Option [1] nutzen.")
            return

        for i, movie in enumerate(self.movies, 1):
            print(f"[{i}] {movie.title} (FSK: {movie.fsk})")

        try:
            choice = int(input("Welchen Film wollen Sie?: ")) -1
            if 0 <= choice < len(self.movies):
                selected_movie = self.movies[choice]
                date = input("Datum (TT.MM.JJJJ): ")
                time = input("Uhrzeit (HH:MM): ")
                capacity = int(input("Anzahl der verfügbaren Plätze: "))

                from model.cinema_presentation.class_presentation import Presentation
                new_presentation = Presentation(selected_movie, date, time, capacity)
                self.presentations.append(new_presentation)
                print(f"\nErfolg: Vorstellung für '{selected_movie.title}' am {date} um {time} wurde angelegt.")
            else:
                print("Fehler: Diese Filmnummer existiert nicht.")

        except ValueError:
            print("Fehler: Ungültige Eingabe. Bitte geben Sie Zahlen für die Auswahl und die Plätze ein.")

    def show_presentations_status(self):
        print("\n--- Vorstellungsstatus anzeigen ---")
        if not self.presentations:
            print("Keine Vorstellungen geplant.")
        else:
            for i, presentation in enumerate(self.presentations, 1):
                print(f"[{i}] {presentation}")

    def reservation_catch(self):
        print("\n--- Plätze reservieren ---")
        if not self.presentations:
            print("Fehler: Keine Vorstellungen vorhanden.")
            return

        for i, presentation in enumerate(self.presentations, 1):
            print(f"[{i}] {presentation}")

        try:
            choice = int(input("Wählen Sie eine Vorstellung (Nummer): ")) - 1
            if 0 <= choice < len(self.presentations):
                selected_presentation = self.presentations[choice]

                occupants = int(input(f"Wie viele Plätze für '{selected_presentation.movie.title}' reservieren? "))

                reserved, date = selected_presentation.reserve_seats(occupants)

                if reserved:
                    print(f"Erfolg: {occupants} Plätze reserviert am {date}.")
                    print(f"Verbleibende Plätze: {selected_presentation.free_seats}")
                else:
                    print(f"Fehler: Nicht genügend Plätze (Nur noch {selected_presentation.free_seats} frei).")
            else:
                print("Fehler: Ungültige Nummer.")
        except ValueError:
            print("Fehler: Bitte geben Sie nur Zahlen ein.")

    def cancel_catch(self):
        print("\n--- Reservierung stornieren ---")
        if not self.presentations:
            print("Fehler: Keine Vorstellungen vorhanden.")
            return

        for i, presentation in enumerate(self.presentations, 1):
            print(f"[{i}] {presentation}")

        try:
            choice = int(input("Wählen Sie eine Vorstellung (Nummer): ")) - 1
            if 0 <= choice < len(self.presentations):
                selected_presentation = self.presentations[choice]
                amount = int(input("Wie viele Plätze sollen storniert werden? "))

                if selected_presentation.cancel_reservation(amount):
                    print(f"Erfolg: {amount} Plätze wieder freigegeben.")
                    print(f"Aktuell frei: {selected_presentation.free_seats}/{selected_presentation.capacity}")
                else:
                    print("Fehler: Stornierung ungültig (Kapazität überschritten).")
            else:
                print("Fehler: Ungültige Nummer.")
        except ValueError:
            print("Fehler: Bitte geben Sie nur Zahlen ein.")