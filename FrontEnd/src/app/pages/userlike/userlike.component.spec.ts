import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { UserLikeComponent } from './userlike.component';
import { UserService } from '../../services/user.service';
import { of } from 'rxjs';
import { UserMovie } from '../../models/user-movie';
import { Movie } from '../../models/movie';

describe('UserLikeComponent', () => {
  let component: UserLikeComponent;
  let fixture: ComponentFixture<UserLikeComponent>;
  let userService: UserService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UserLikeComponent ],
      imports: [ HttpClientTestingModule ],
      providers: [ UserService ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UserLikeComponent);
    component = fixture.componentInstance;
    userService = TestBed.inject(UserService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should fetch user movies on init', () => {
    const userMovies: UserMovie[] = [
      {
        movie: {
          id: 1,
          name: 'Movie 1',
          overview: 'Overview of Movie 1',
          genres: ['Action', 'Thriller'],
          poster_path: '/movie1.jpg',
          release_date: 1640858400,
          note_average: 7.5
        },
        watch: true,
        liked: true
      },
      {
        movie: {
          id: 2,
          name: 'Movie 2',
          overview: 'Overview of Movie 2',
          genres: ['Drama', 'Romance'],
          poster_path: '/movie2.jpg',
          release_date: 1640944800,
          note_average: 8.0
        },
        watch: false,
        liked: true
      }
    ];
  
    spyOn(userService, 'getUserMovies').and.returnValue();
    spyOnProperty(userService, 'userMoviesSubject', 'get').and.returnValue(of(userMovies));
    fixture.detectChanges();
  
    expect(component.userMovies).toEqual(userMovies);
  });
  
});
 