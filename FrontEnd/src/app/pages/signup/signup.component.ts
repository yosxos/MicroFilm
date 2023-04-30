import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {
  email = '';
  name='';
  password = '';
  confirmPassword = '';

  constructor(
    private router: Router,
    private userService: UserService
  ) { }

  isValidForm() {
    return this.email && this.password && this.confirmPassword && (this.password === this.confirmPassword);
  }

  signUp() {
    this.userService.createUser({
      id: 1,
      name: this.name,
      email: this.email,
      password: this.password
    });
    this.router.navigate(['/login']);
  }
}
