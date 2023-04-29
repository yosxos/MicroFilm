import requests
from databases import Database
from sqlalchemy import select, insert
from db import movies, genre
import os

DATABASE_URL = os.getenv('DATABASE_URL')

api_key = '1f0343b182ed839f73d76a47cb67adc4'

database = Database(DATABASE_URL)


# On récupère les genres de l'API TMDB
async def get_genres(api_key):
    response = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=fr-FR')
    genres_list = response.json()['genres']
    return genres_list

# On met ces genres dans notre table 'genres'
async def insert_genres(genres_table, genres_list):
    async with database:
        for genre in genres_list:
            query = genres_table.insert().values(id=genre['id'], name=genre['name'])
            await database.execute(query)

# On met les films dans la table 'movies'
async def insert_movies(movies_table, movies):
    async with database:
        for movie in movies:
            # On vérifie si la clé 'release_date' existe dans le dictionnaire pour savoir si le film est sortie
            release_date = movie.get('release_date', None)
            movie_query = movies_table.select().where(movies_table.c.id == movie['id'])
            result = await database.fetch_one(movie_query)
            alreadyExist = result is not None
            if release_date != None and alreadyExist==False:
                # On insère le film dans la table 'movies'
                try :
                    movie_query = movies_table.insert().values(id=movie['id'], name=movie['title'], overview=movie['overview'], note_average=movie['vote_average'], release_date=movie['release_date'], poster_path='https://image.tmdb.org/t/p/original' +movie['poster_path'], genres_id = movie['genre_ids'])
                except TypeError :
                    print(f"Erreur : Pas de poster_path pour le film avec l'ID {movie['id']}")
                    continue
            await database.execute(movie_query)

                    
            

async def main():
    await database.connect()
    genres_list = await get_genres(api_key)
    await insert_genres(genre, genres_list)
    for pagePopular in range(0, 340): # Récupération des 20 premières pages de films populaires
        response = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=fr-FR&page={pagePopular}')
        movies_list = response.json()['results']
        await insert_movies(movies, movies_list)
    for pageTopRated in range(0,340):
        response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=fr-FR&page={pageTopRated}')
        movies_list = response.json()['results']
        await insert_movies(movies, movies_list)
    await database.disconnect()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())