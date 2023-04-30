import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Movie } from '../models/movie';
import { Genre } from '../models/genre';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(private httpCLient: HttpClient) { }
  URL = 'http://localhost:8004/api/v1/movies';

  movies: Array<Movie> = []
  genres: Array<Genre> = []

  moviesSubject: BehaviorSubject<Movie[]> = new BehaviorSubject<Movie[]>([]);
  public movies$: Observable<Movie[]> = this.moviesSubject.asObservable();

  //Get all movies
  getMovies() {
    this.httpCLient.get<Movie[]>(this.URL + 'movies').subscribe((res: Movie[]) => {
      this.movies = res;
      this.moviesSubject.next(this.movies);
    })
  }

  //Get all genres
  getGenres(): Observable<Genre[]> {
    return this.httpCLient.get<Genre[]>(this.URL + 'genres')
      .pipe(map((res: Genre[]) => {
        this.genres = res;
        return res;
      }));
  }
}