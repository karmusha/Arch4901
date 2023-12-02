from adapters.user_command import UserCommand
from adapters.movie_reviews_repo import MovieReviewsRepo
from adapters.console_printer import ConsolePrinter
from application.movie_user import MovieUser
from domain.movie_search_request import MovieSearchRequest

if __name__ == '__main__':
    fetchMovieReviews = MovieReviewsRepo()
    printMovieReviews = ConsolePrinter()

    userCommand = UserCommand(fetchMovieReviews, printMovieReviews)

    movieUser = MovieUser(userCommand)

    starWarsRequest = MovieSearchRequest('Star Wars')
    starTrekRequest = MovieSearchRequest('Star Trek')

print('Displaying reviews for movie ' + starWarsRequest.getMovieName())
movieUser.processInput(starWarsRequest)

print('Displaying reviews for movie ' + starTrekRequest.getMovieName())
movieUser.processInput(starTrekRequest)
