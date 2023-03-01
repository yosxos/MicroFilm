import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { ProfilComponent } from './pages/profil/profil.component';
import { AuthguardGuard } from './securite/authguard.guard';

const routes: Routes = [
{ path: '', redirectTo: 'login', pathMatch: 'full' },
{ path:'login', component: LoginComponent},
{ path:'profil',component:ProfilComponent,canActivate:[AuthguardGuard] }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
