class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'


    DEBUG = True
class ProdConfig:

    pass

class DevConfig:

    DEBUG = True