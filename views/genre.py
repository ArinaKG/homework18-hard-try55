from flask_restx import Resourse, Namespace
from implemented import genre_service, genre_schema, genres_schema

genre_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resourse):

    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genres_ns.route('<int:gid>')
class GenreView(Resourse):

    def get(self, gid):
        genre = genre_service.get_by_id(gid)
        return genre_service.dump(genre), 200