from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service, movie_schema, movies_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id":  genre,
            "year": year,
        }
        all_movies = movie_service.filters(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


    def post(self):
        data = request.json
        new_movie = movie_service.add_movie(data)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_service.update(data)

        return 'updated', 204

    def delete(self, mid):
        movie_service.del_movie(mid)
        return 'deleted', 204