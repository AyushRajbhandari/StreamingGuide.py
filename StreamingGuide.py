# Author: Ayush Rajbhandari
# GitHub username: AyushRajbhandari
# Date: 6-5-26
# Description: Defines classes for managing movies, streaming services,
#               and a streaming guide to look up where movies are available.

class Movie:
    """
    Represents a movie with a title, genre, director, and release year.
    All data members are private.
    """
    def __init__(self, title, genre, director, year):
        """Initializes a Movie object with title, genre, director, and year."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Returns the title of the movie."""
        return self._title

    def get_genre(self):
        """Returns the genre of the movie."""
        return self._genre

    def get_director(self):
        """Returns the director of the movie."""
        return self._director

    def get_year(self):
        """Returns the release year of the movie."""
        return self._year


class StreamingService:

    """Represents a streaming service with a name and a catalog of Movie objects."""

    def __init__(self, name):
        """Initializes a StreamingService with a name and an empty catalog."""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Returns the name of the streaming service."""
        return self._name

    def get_catalog(self):
        """Returns the catalog dictionary of the streaming service."""
        return self._catalog

    def add_movie(self, movie):
        """Adds a Movie object to the catalog using the movie's title as the key."""
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, movie_title):
        """Removes a movie from the catalog if it exists."""
        if movie_title in self._catalog:
            del self._catalog[movie_title]


class StreamingGuide:
    """
    A guide that tracks multiple StreamingService objects.
    Contains methods to search for movie availability across services.
    """
    def __init__(self):
        """Initializes a StreamingGuide with an empty list of services."""
        self._services = []

    def add_streaming_service(self, service):
        """Adds a StreamingService object to the guide using the += operator."""
        self._services += [service]

    def delete_streaming_service(self, service_name):
        """
        Removes a StreamingService from the guide by its name
        using a list comprehension instead of .remove().
        """
        # This keeps every service whose name does NOT match the one we want to delete
        self._services = [s for s in self._services if s.get_name() != service_name]

    def who_streams_this_movie(self, movie_title):
        """
        Searches all streaming services in the guide for a specific movie title.
        Returns the movie's title, year, and a list of services streaming it. Returns None if no service streams the movie.
        """
        available_services = []
        movie_year = None

        for service in self._services:
            catalog = service.get_catalog()
            if movie_title in catalog:
                available_services += [service.get_name()] # Also using += here!
                if movie_year is None:
                    movie_year = catalog[movie_title].get_year()

        if not available_services:
            return None

        return {
            'title': movie_title,
            'year': movie_year,
            'services': available_services
        }
