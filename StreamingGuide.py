# Author: Ayush Rajbhandari
# Date: 7-4-2026
# Description: defines classes for managing movies, streaming services,
#               and a streaming guide to look up where movies are available.

class Movie:
    """
    Represents a movie with a title, genre, director, and release year.
    All data members are private.
    """
    def __init__(self, title, genre, director, year):
        """Initializes a Movie object with title, genre, director, and year."""
        self.__title = title
        self.__genre = genre
        self.__director = director
        self.__year = year

    def get_title(self):
        """Returns the title of the movie."""
        return self.__title

    def get_genre(self):
        """Returns the genre of the movie."""
        return self.__genre

    def get_director(self):
        """Returns the director of the movie."""
        return self.__director

    def get_year(self):
        """Returns the release year of the movie."""
        return self.__year


class StreamingService:

    """Represents a streaming service with a name and a catalog of Movie objects."""

    def __init__(self, name):
        """Initializes a StreamingService with a name and an empty catalog."""
        self.__name = name
        self.__catalog = {}

    def get_name(self):
        """Returns the name of the streaming service."""
        return self.__name

    def get_catalog(self):
        """Returns the catalog dictionary of the streaming service."""
        return self.__catalog

    def add_movie(self, movie):
        """Adds a Movie object to the catalog using the movie's title as the key."""
        self.__catalog[movie.get_title()] = movie

    def delete_movie(self, movie_title):
        """Removes a movie from the catalog if it exists."""
        if movie_title in self.__catalog:
            del self.__catalog[movie_title]


class StreamingGuide:
    """
    Represents a guide that tracks multiple StreamingService objects.
    It has methods to search for movie availability across services.
    """
    def __init__(self):
        """Initializes a StreamingGuide with an empty list of services."""
        self.__services = []

    def add_streaming_service(self, service):
        """Adds a StreamingService object to the guide."""
        self.__services += [service]

    def delete_streaming_service(self, service_name):
        """Removes a StreamingService from the guide by its name."""
        for service in self.__services:
            if service.get_name() == service_name:
                self.__services -= [service]
                break  # Assuming unique service names, we can stop searching

    def who_streams_this_movie(self, movie_title):
        """
        Searches all streaming services in the guide for a specific movie title.
        Returns a dictionary with the movie's title, year, and a list of
        services streaming it. Returns None if no service streams the movie.
        """
        available_services = []
        movie_year = None

        for service in self.__services:
            catalog = service.get_catalog()
            if movie_title in catalog:
                available_services += [service.get_name()]
                # If the year hasnt been grabbed, get it from the Movie object
                if movie_year is None:
                    movie_year = catalog[movie_title].get_year()

        if not available_services:
            return None

        return {
            'title': movie_title,
            'year': movie_year,
            'services': available_services
        }
