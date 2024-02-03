from models.route import Route
from models.package import Package

class ApplicationData:
    
    def __init__(self):
        self._delivery_routes: list[Route] = []
        self._delivery_packages: list[Package] = []
        pass