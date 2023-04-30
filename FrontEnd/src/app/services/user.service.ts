import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../models/user';
import { Movie } from '../models/movie';
import { Group } from '../models/group';
import { Genre } from '../models/genre';
import { UserMovie } from '../models/user-movie';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private httpCLient: HttpClient) {
    this.getUser();
   }
  URL = 'http://localhost:8002/user/';
  user: User = <User>{}
  user_movies: Array<UserMovie> = []
  user_groups: Array<Group> = []
  user_genres: Array<Genre> = []

  userMoviesSubject: BehaviorSubject<UserMovie[]> = new BehaviorSubject<UserMovie[]>([]);
  public userMovies: Observable<UserMovie[]> = this.userMoviesSubject.asObservable();

//Create a user in the backend
createUser(user: User) {
  this.httpCLient.post<User>(this.URL+'create', user)
    .subscribe(
      (response) => {
        console.log('User created successfully', response);
      },
      (error) => {
        console.log('Error creating user', error);
      }
    );
}
  
  
  // Get a user by id from the backend
  getUser() {
    this.httpCLient.get<User>(this.URL + this.user.id).subscribe((res: User) => {
      this.user = res
    }
    )
  }
  // Update a user by id from the backend
  updateUser(userUpdated: User) {
    this.httpCLient.put<User>(this.URL+"/update/" + this.user.id, userUpdated).subscribe((res: User) => {
      this.user = userUpdated
    }
    )
  }
  // Delete a user by id from the backendh
  deleteUser() {
    this.httpCLient.delete<User>(this.URL +"/delete/"+ this.user.id).subscribe((res: User) => {
      this.user = <User>{}
      console.log(res)
    }
    )
  }
  getUserMovies() {
    this.httpCLient.get<UserMovie[]>(this.URL + this.user.id + '/Movies').subscribe((res: UserMovie[]) => {
      this.userMoviesSubject.next(res);
    });
  }
  
  // Add a movie to the user from the backend
  addUserMovie(newMovie: UserMovie) {
    let payload={"movie_id":newMovie.movie.id,"watched":newMovie.watch,"liked":newMovie.liked}
    this.httpCLient.post<UserMovie>(this.URL + this.user.id + '/Movies/add', payload).subscribe((res: UserMovie) => {
      this.user_movies.push(res)
    }
    )
  }
  // Update a movie to the user from the backend
  updateUserMovie(newMovie: UserMovie) {
    let payload={"movie_id":newMovie.movie.id,"watched":newMovie.watch,"liked":newMovie.liked}
    this.httpCLient.put<UserMovie>(this.URL + this.user.id + '/Movies/update/' + newMovie.movie.id, payload).subscribe((res: UserMovie) => {
      this.user_movies.filter((m) => m.movie.id != newMovie.movie.id)
      this.user_movies.push(res)
    }
    )
  }
  // Delete a movie from the user from the backend
  deleteUserMovie(movie: UserMovie) {
    this.httpCLient.delete<Movie>(this.URL + this.user.id + '/Movies/delete' + movie.movie.id).subscribe((res: Movie) => {
      this.user_movies.filter((m) => m.movie.id != movie.movie.id)
    }
    )

  }
  /*
  //Get user Groups
  getUserGroups() {
    this.httpCLient.get<Group>(this.URL + this.user.id.toString+ '/Groups').subscribe((res: Group) => {
      this.user_groups.push(res)
    }
    )
  }
  // Add a group to the user from the backend
  addUserGroup(group: Group) {
    this.httpCLient.post<Group>(this.URL + this.user.id.toString+ '/Groups/add', group.id).subscribe((res: Group) => {
      this.user_groups.push(group)
    }
    )
  }
  //Update a group to the user from the backend
  updateUserGroup(group: Group, newGroup: Group) {

    this.httpCLient.put<Group>(this.URL + this.user.id.toString + '/Groups/update' + group.id.toString, newGroup.id).subscribe((res: Group) => {
      this.user_groups.filter((g) => g.id != group.id)
      this.user_groups.push(newGroup)
    }
    )
  }
  // Delete a group from the user from the backend
  deleteUserGroup(group: Group) {
    this.httpCLient.delete<Group>(this.URL + this.user.id.toString + '/Groups/delete' + group.id).subscribe((res: Group) => {
      this.user_groups.filter((g) => g.id != group.id)
    }
    )

  }
  */
  getUserGroups(): Observable<Group[]> {
    return this.httpCLient.get<Group[]>(this.URL + this.user.id.toString() + '/Groups');
}
 
  addUserGroup(group: Group): Observable<Group> {
    return this.httpCLient.post<Group>(this.URL + this.user.id.toString()+ '/Groups/add', group.id);
}

updateUserGroup(group: Group, newGroup: Group): Observable<Group> {
    return this.httpCLient.put<Group>(this.URL + this.user.id.toString() + '/Groups/update' + group.id.toString(), newGroup.id);
}

deleteUserGroup(group: Group): Observable<Group> {
    return this.httpCLient.delete<Group>(this.URL + this.user.id.toString() + '/Groups/delete' + group.id);
}

//Get genres of the user
  getUserGenres() {
    this.httpCLient.get<Genre>(this.URL + this.user.id + '/Genres').subscribe((res: Genre) => {
      this.user_genres.push(res)
    }
    )
  }
  // Add a genre to the user from the backend
  addUserGenre(genre: Genre) {
    this.httpCLient.post<Genre>(this.URL + this.user.id + '/Genres/add' , genre.id).subscribe((res: Genre) => {
      this.user_genres.push(genre)
    }
    )
  }
  
  //Update a genre to the user from the backend
  updateUserGenre(genre: Genre, newGenre: Genre) {

      this.httpCLient.put<Genre>(this.URL + this.user.id+ '/Genres/update' + genre.id, newGenre.id).subscribe((res: Genre) => {
        this.user_genres.filter((g) => g.id != genre.id)
        this.user_genres.push(newGenre)
      }
      )
    }
  // Delete a genre from the user from the backend
  deleteUserGenre(genre: Genre) {
    this.httpCLient.delete<Genre>(this.URL + this.user.id + '/Genres/delete' + genre.id).subscribe((res: Genre) => {
      this.user_genres.filter((g) => g.id != genre.id)
    }
    )
  }



}


