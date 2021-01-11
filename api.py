from movies import *

# ruta para obtener todas las peliculas
@app.route('/movies', methods=['GET'])
def get_movies():
    ''' funcion para obtener todas las peliculas '''
    return jsonify({'Movies': Movie.get_all_movies()})

# ruta para obtener una pelicula por el id
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

# ruta para añadir una pelicula
@app.route('/movies', methods=['POST'])
def add_movie():
    ''' funcion para añadir una nueva pelicula a nuestra db '''
    request_data = request.get_json(force=True) # obtener los datos desde el cliente
    print(request_data)
    Movie.add_movie(request_data['title'],
                        request_data['year'],
                        request_data['genre'])
    response = Response("Movie added", 201, mimetype='application/json') # response body, code status, content type
    return response

# ruta para actualizar una pelicula
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    ''' funcion para editar una pelicula en nuestra db'''
    request_data = request.get_json(force=True)
    Movie.update_movie(id, request_data['title'],
                            request_data['year'],
                            request_data['genre'])
    response = Response("Movie updated", status=200, mimetype='application/son')
    return response

# ruta para eliminar una pelicula con su id
@app.route('/movies/<int:id>', methods=['Delete'])
def remove_movie(id):
    ''' funcion para eliminar una pelicula de nuestra db '''
    Movie.delete_movie(id)
    response = Response('Movie deleted', status=200, mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run(port=1234, debug=True)

