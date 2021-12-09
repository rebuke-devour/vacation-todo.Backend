"""VacaGoTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.VacaGo import VacaGo

class VacaGoTableSeeder(Seeder):
    def run(self):
        VacaGo.create({"city":"Los Angeles", "activity": "Mount Wilson Observatory","details":"See LA from 6000 feet" })
        VacaGo.create({"city":"Bali", "activity": "Bali Volcano with Jungle Swing Experience", "details": "Get a great photo at one of the island's most photographed destinations."})
        VacaGo.create({"city": "Tokyo", "activity": "Go-kart tour in Shinjuku metro area", "details": "Go-karting in heart of TOKYO metropolitan area is experience that gives you an adrenaline rush like never before." })
       
