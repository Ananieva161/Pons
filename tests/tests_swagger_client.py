import unittest
import swagger_client
from swagger_client.rest import ApiException
from unittest.mock import patch, Mock

class TestMovieApi(unittest.TestCase):

    def setUp(self):
        self.configuration = swagger_client.Configuration()
        self.configuration.host = 'http://127.0.0.1:8080/'
        self.api_client = swagger_client.ApiClient(configuration=self.configuration)
        self.api_instance = swagger_client.MovieApi(api_client=self.api_client)

    def test_add_movie(self):
        mock_movie = swagger_client.Movie()
        mock_movie.title = "Test Movie"
        mock_movie.description = "This is a test movie"
        mock_movie.director = "Test Director"

        with patch.object(self.api_instance, 'add_movie') as mock_add_movie:
            mock_add_movie.return_value = None
            self.api_instance.add_movie(mock_movie)
            mock_add_movie.assert_called_once_with(mock_movie)

    def test_add_movie_exception(self):
        mock_movie = swagger_client.Movie()
        mock_movie.title = "Test Movie"
        mock_movie.description = "This is a test movie"
        mock_movie.director = "Test Director"

        with patch.object(self.api_instance, 'add_movie') as mock_add_movie:
            mock_add_movie.side_effect = ApiException(status=500, reason="Internal Server Error")
            with self.assertRaises(ApiException):
                self.api_instance.add_movie(mock_movie)
            mock_add_movie.assert_called_once_with(mock_movie)

    def test_delete_movie_by_id(self):
        movie_id = 123

        with patch.object(self.api_instance, 'delete_movie_by_id') as mock_delete_movie:
            mock_delete_movie.return_value = None
            self.api_instance.delete_movie_by_id(movie_id)
            mock_delete_movie.assert_called_once_with(movie_id)

    def test_delete_movie_by_id_exception(self):
        movie_id = 123

        with patch.object(self.api_instance, 'delete_movie_by_id') as mock_delete_movie:
            mock_delete_movie.side_effect = ApiException(status=404, reason="Movie not found")
            with self.assertRaises(ApiException):
                self.api_instance.delete_movie_by_id(movie_id)
            mock_delete_movie.assert_called_once_with(movie_id)

if __name__ == '__main__':
    unittest.main()
