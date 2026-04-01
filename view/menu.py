from model.cinema_manager.class_cinema_manager import Cinema_Manager


class Menu:
    def __init__(self):
        self.manager = Cinema_Manager()
    @staticmethod
    def menu_user_input():
        return """
    **************************
    * GOTHAM NOIR ************      
    **************************
    1. Neuen Film erfassen
    2. Neue Vorstellung erfassen
    3. Plätze reservieren
    4. Reservierung stornieren
    5. Vorstellungsstatus anzeigen
    6. Alle Filme anzeigen
    Q. Beenden
    """

    def show_menu(self):
        while True:
            print(self.menu_user_input())
            user_option = input("Wählen Sie eine Option (1-5 oder Q): ").upper()

            if user_option == "1":
                self.manager.movie_catch()

            elif user_option == "2":
                print("Funktion 'Neue Vorstellung' wird aufgerufen...")
                self.manager.presentation_catch()

            elif user_option == "3":
                print("Funktion 'Reservieren' wird aufgerufen...")
                self.manager.reservation_catch()

            elif user_option == "4":
                print("Funktion 'Stornieren' wird aufgerufen...")
                self.manager.cancel_catch()

            elif user_option == "5":
                self.manager.show_presentations_status()

            elif user_option == "6":
                self.manager.show_movies()

            elif user_option == "Q" or "q":
                print("Programm beendet. Auf Wiedersehen im Gotham Noir!")
                break
            else:
                print("Ungültige Eingabe! Bitte wählen Sie 1-5 oder Q.")