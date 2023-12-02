class Model:
    def __init__(self, movieApp):
        self.movieApp = movieApp

    def run(self, userCommand):
        self.movieApp.accept(userCommand)
