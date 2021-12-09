""" A VacaGoController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.VacaGo import VacaGo



class VacaGoController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", VacaGoController)
        """
        id = self.request.params("id")
        return VacaGo.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", VacaGoController)
        """
        return VacaGo.all()

    def create(self):
        city = self.request.input("city")
        activity = self.request.input("activity")
        details = self.request.input("details")
        vacaGo= VacaGo.create({ "city": city, "activity": activity, "details": details })
        return vacaGo


    def update(self):
        city = self.request.input("city")
        activity = self.request.input("activity")
        details = self.request.input("details")
        id = self.request.param("id")
        VacaGo.where("id", id).update({"city": city, "activity": activity, "details": details})
        return VacaGo.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        vacaGo = VacaGo.where("id", id).get()
        VacaGo.where("id", id).delete()
        return vacaGo