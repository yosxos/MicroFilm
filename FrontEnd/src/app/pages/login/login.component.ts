import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form!: FormGroup
  constructor(
    private _auth: AuthService,
    private router: Router,
    public fb: FormBuilder,
    private Uservice:UserService,

  ) { }
  ngOnInit(): void {
    this.form = this.fb.group({
      email: ['', Validators.required],
      password:['', Validators.required]
    });
  }


  login(){
    let b = this.form.value
    this._auth.login(b).subscribe((res: any) => {
      console.log(res)
      this._auth.setDataInLocalStorage('token', res.token)
      this.Uservice.user=res
      console.log("user",this.Uservice.user)
      this.router.navigate(['/profil'])
    }
    )

  }
  goToSignUp() {
    this.router.navigate(['/signup']);
  }

}
