"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
        RouteGroup([
        Get("/", "VacaGoController@index").name("index"),
        Get("/@id", "VacaGoController@show").name("show"),
        Post("/", "VacaGoController@create").name("create"),
        Put("/@id", "VacaGoController@update").name("update"),
        Delete("/@id", "VacaGoController@destroy").name("destroy")
    ],prefix="/vacago",name= "VacaGo")
]
