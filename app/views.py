from flask import render_template,redirect,request,url_for

from app import app
from .request import get_movies,get_movie,search_movie

@app.route('/')
def index():

    popular=get_movies('popular')

    upcoming=get_movies('upcoming')
    
    title="flask app"

    search_movie=request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html',popular=popular,upcoming=upcoming,title=title)

@app.route('/movie/<int:id>')
def movie(id):
    movie=get_movie(id)
    title=f'{movie.title}'

    return render_template('movie.html',title=title,movie=movie)



@app.route('/search/<movie_name>')

def search(movie_name):
    movie_name_list=movie_name.strip().split(" ")
    movie_name_format="+".join(movie_name_list)

    searched_movies=search_movie(movie_name_format)
    title=f'search results for {movie_name}'
    return render_template('search.html', movies=searched_movies,title=title)