from settings import *
import json

# Inicializacion de la db
db = SQLAlchemy(app)

# Clase movie que se herada de db.Model de sqlalchemy
class Movie(db.Model):
    __tablename__ = 'movies' # creacion de la tabla 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    # volver nuestra clase movie a json
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'genre': self.genre
        }

    # funcion para añadir una movie a la db
    def add_movie(_title, _year, _genre):
        ''' se pasan los parametros _title, _year, _genre para ser añadidos a la db'''
        # creando una instancia movie en la db
        new_movie = Movie(title=_title, year=_year, genre=_genre)
        db.session.add(new_movie) # añade la movie en la db
        db.session.commit() # persistencia commit

    def get_all_movies():
        '''obtener todas las movies de nuestra db'''
        return [Movie.json(movie) for movie in Movie.query.all()] # obtenenos con una iteracion una lista de las movies

    def get_movie(id):
        '''obtener una pelicula desde la db con su id'''
        return [Movie.json(Movie.query.filter_by(id=id).first())] # query con la id
         # Movie.json() convierte nuestra salida en json
        # el metodo filter_by filtra el query por el id
        # el id es unico obtendremos un solo dato
        # el metodo .first() retorna el primer valor obtenido

    def update_movie(_id, _title, _year, _genre):
        ''' actualiza los detalles de una pelicula usando id, title, year y genre como params'''
        movie_to_update = Movie.query.filter_by(id=_id).first()
        movie_to_update.title = _title
        movie_to_update.year = _year
        movie_to_update.genre = _genre
        db.session.commit()

    def delete_movie(_id):
        ''' elimina una pelicula pasando como parametro el id'''
        Movie.query.filter_by(id=_id).delete()
        db.session.commit()
    