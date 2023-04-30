import { Component, OnInit } from '@angular/core';
import { UserMovie } from '../../models/user-movie';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-user-like',
  templateUrl: './userlike.component.html',
  styleUrls: ['./userlike.component.css']
})
export class UserLikeComponent implements OnInit {
  userMovies: UserMovie[] = [];

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.userService.getUserMovies();
    this.userService.userMoviesSubject.subscribe((userMovies: UserMovie[]) => {
      this.userMovies = userMovies;
    });
  }

}
