# MicroFilm
MicroFilm is a project developed for a school course on MicroService architecture. The project follows a MonoRepo architecture and consists of multiple backend services including:

- Auth: A service responsible for user login and JWT token generation.
- Data: A service that creates the DB table, Movie Table, and calls the TMDB API to insert movies into the database.
- User: A service that creates and manages users.
- Group: A service that creates and manages user groups.
- UserSuggestion: A service that will suggest movies to users (TO DO).
The frontend of the project is developed using Angular. Each service is containerized using Docker.

# How to run 
## Local:
In the root of the project excecute `docker-compose build` to build the docker and then run it with `docker-compose up -d`
## Online 
The project will be hosted in this link : for a period of : 
# Groupe:
- Yassir AIT TMILLA
- Cillian   ROSAY
- Yassine   Alami
