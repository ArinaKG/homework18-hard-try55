from .model.director import Director

class DirectorDao:

    def ___init___(self, session):
        self.session = session

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors

    def get_one(self, did):
        director = self.session.query(Director).get(did)
        return director