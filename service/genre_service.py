from dao.genre_dao import GenreDao


class GenreService:
    def __init__(self, dao:GenreDao):
        self.dao = dao

    def get_all(self):
        all_genres = self.dao.get_all()
        return all_genres

    def get_by_id(self, gid):
        genre = self.dao.get_one(gid)
        return genre