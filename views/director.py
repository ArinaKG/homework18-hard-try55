from flask_restx import Resourse, Namespace
from implemented import director_service, director_schema, directors_schema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorView(Resourse):

    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resourse):

    def get(self, did):
        director = director_service.get_by_id(did)
        return director_schema.dump(director), 200