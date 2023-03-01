import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-profil',
  templateUrl: './profil.component.html',
  styleUrls: ['./profil.component.css']
})
export class ProfilComponent implements OnInit {

    constructor(
      private _api : ApiService,
      private _auth: AuthService,
    ) { }

    ngOnInit(): void {
      this.test_jwt()
    }
    test_jwt(){
      this._api.getTypeRequest('test-jwt').subscribe((res: any) => {
        console.log(res)

      }, err => {
        console.log(err)
      });
    }

}
