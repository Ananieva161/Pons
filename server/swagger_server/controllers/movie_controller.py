import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util


def add_movie(body):  # noqa: E501
    """Добавить новый фильм

     # noqa: E501

    :param body: Новый фильм
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_movie_by_id(movie_id):  # noqa: E501
    """Удалить фильм по ID

     # noqa: E501

    :param movie_id: ID фильма
    :type movie_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_movie_by_id(movie_id):  # noqa: E501
    """Получить информацию о фильме по ID

     # noqa: E501

    :param movie_id: ID фильма
    :type movie_id: int

    :rtype: Movie
    """
    return 'do some magic!'


def get_movies_list():  # noqa: E501
    """Получить список всех фильмов

     # noqa: E501


    :rtype: List[Movie]
    """
    return 'do some magic!'


def update_movie_by_id(body, movie_id):  # noqa: E501
    """Обновить информацию о фильме по ID

     # noqa: E501

    :param body: Обновленная информация о фильме
    :type body: dict | bytes
    :param movie_id: ID фильма
    :type movie_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
