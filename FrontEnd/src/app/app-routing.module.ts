import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { ProfilComponent } from './pages/profil/profil.component';
import { AuthguardGuard } from './securite/authguard.guard';
import { SignupComponent } from './pages/signup/signup.component';
import { MovieCardComponent } from './pages/moviecard/moviecard.component';
import { UserLikeComponent } from './pages/userlike/userlike.component';
import { GroupComponent } from './pages/group/group.component';

const routes: Routes = [
{ path: '', redirectTo: 'login', pathMatch: 'full' },
{ path:'login', component: LoginComponent},
{ path:'signup', component: SignupComponent},
{ path: 'profil', component: ProfilComponent },
{ path: 'moviecard', component: MovieCardComponent },
{ path: 'userlike', component: UserLikeComponent },
{ path: 'group', component: GroupComponent },
/*{ path:'profil',component:ProfilComponent,canActivate:[AuthguardGuard] }*/
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
