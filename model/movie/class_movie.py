
class Movie:
    def __init__(self, title, duration, fsk):
        self.title = title
        self.duration = duration
        self.fsk = fsk

    def __str__(self):
        return f'{self.title} {self.duration} {self.fsk}'