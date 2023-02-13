from dao.director_dao import DirectorDao


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_all(self):
        all_directors = self.dao.get_all()
        return all_directors

    def get_by_id(self, did):
        return self.dao.get_one(did)