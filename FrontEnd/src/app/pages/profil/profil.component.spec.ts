import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ProfilComponent } from './profil.component';
import { UserService } from '../../services/user.service';
import { User } from '../../models/user';

describe('ProfilComponent', () => {
  let component: ProfilComponent;
  let fixture: ComponentFixture<ProfilComponent>;
  let userService: UserService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfilComponent ],
      imports: [ HttpClientTestingModule ],
      providers: [ UserService ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfilComponent);
    component = fixture.componentInstance;
    userService = TestBed.inject(UserService);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should update user', () => {
    const spy = spyOn(userService, 'updateUser').and.callThrough();
    component.user = { id: 1, name: 'John Doe', email: 'johndoe@gmail.com', password: 'password' };
    component.updateUser();
    expect(spy).toHaveBeenCalled();
    expect(component.message).toEqual('Vos informations ont été mises à jour avec succès.');
  });

  it('should delete user', () => {
    const spy = spyOn(userService, 'deleteUser').and.callThrough();
    component.deleteUser();
    expect(spy).toHaveBeenCalled();
    expect(component.message).toEqual('Votre compte a été supprimé avec succès.');
  });
});
