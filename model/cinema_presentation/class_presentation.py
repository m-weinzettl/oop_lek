import datetime

class Presentation:
    def __init__(self, movie, date, time, capacity):
        self.movie = movie
        self.date = date
        self.time = time
        self.capacity = capacity
        self.free_seats = capacity

    def reserve_seats(self, amount):
        if amount <= self.free_seats:
            self.free_seats -= amount
            reservation_date = datetime.date.today()
            return True, reservation_date
        return False, None

    def cancel_reservation(self, amount):
        if self.free_seats + amount <= self.capacity:
            self.free_seats += amount
            return True
        return False

    def __str__(self):
        return (f"Film: {self.movie.title} | Datum: {self.date} | "
                f"Uhrzeit: {self.time} | Freie Plätze: {self.free_seats}/{self.capacity}")