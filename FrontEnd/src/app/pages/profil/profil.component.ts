import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-profil',
  templateUrl: './profil.component.html',
  styleUrls: ['./profil.component.css']
})
export class ProfilComponent implements OnInit {

    constructor(
      private _auth: AuthService,
    ) { }

    ngOnInit(): void {
      this.test_jwt()
    }
    test_jwt(){
      this._auth.checkToken().subscribe((res: any) => {
        console.log(res)
      })
    }

}
