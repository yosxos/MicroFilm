import { Component, OnInit } from '@angular/core';
import { UserMovie } from '../../models/user-movie';
import { MovieService } from '../../services/movie.service';
import { UserService } from '../../services/user.service';
import { Movie } from '../../models/movie';
import { Genre } from '../../models/genre';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-movie-card',
  templateUrl: './moviecard.component.html',
  styleUrls: ['./moviecard.component.css']
})
export class MovieCardComponent implements OnInit {
  movies$ = this.movieService.movies$;
  genres: Genre[] = [];
  showDetailsFlag = false;

  constructor(
    private userService: UserService,
    private movieService: MovieService,
    private httpCLient: HttpClient
  ) { }

  ngOnInit(): void {}

  like(movie: Movie): void {
  
    this.userService.addUserMovie({ movie, liked: true, watch: true });
  }

  dislike(movie: Movie): void {
    const userMovie: UserMovie = { movie, liked: false, watch: true };
    this.userService.deleteUserMovie(userMovie);
  }

  markAsUnwatched(movie: Movie): void {
    this.userService.updateUserMovie({ movie, liked: false, watch: false });
  }
  
  showDetails(movie: Movie): void {
    this.showDetailsFlag = true;
    this.movieService.getGenres().subscribe((genres: Genre[]) => {
      this.genres = genres.filter((genre) => movie.genres.includes(genre.id.toString()));
    });
    console.log("Fetching details of movie with id " + movie.id);
    const foundMovie = this.movieService.movies.find(m => m.id === movie.id);
    if (foundMovie) {
      console.log("Movie details: ");
      console.log("Overview: " + foundMovie.overview);
      console.log("Release Date: " + foundMovie.release_date);
      console.log("Note Average: " + foundMovie.note_average);
      console.log("Genres: " + foundMovie.genres.join(", "));
    } else {
      console.log("Movie with id " + movie.id + " not found!");
    }
  }
  

  


  hideDetails(): void {
    this.showDetailsFlag = false;
  }
  
}

