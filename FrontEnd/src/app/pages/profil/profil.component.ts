import { Component, OnInit } from '@angular/core';
import { User } from '../../models/user';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-profil',
  templateUrl: './profil.component.html',
  styleUrls: ['./profil.component.css']
})
export class ProfilComponent implements OnInit {
  
  message: string = '';

  constructor(private userService: UserService) { }
  user: User = this.userService.user;
  ngOnInit(): void {

  }

  updateUser(): void {
    this.userService.updateUser(this.user);
    this.message = 'Vos informations ont été mises à jour avec succès.';
  }

  deleteUser(): void {
    this.userService.deleteUser();
    this.message = 'Votre compte a été supprimé avec succès.';
  }
}