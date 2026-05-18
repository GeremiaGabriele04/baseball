from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, anno):
        return DAO.getTeamsOfYear(anno)