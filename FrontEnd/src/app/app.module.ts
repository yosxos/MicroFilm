import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HTTP_INTERCEPTORS, HttpClient, HttpClientModule, HttpHeaders } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './pages/login/login.component';
import { ProfilComponent } from './pages/profil/profil.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AuthInterceptor } from './securite/auth.interceptor';
import { MovieCardComponent } from './pages/moviecard/moviecard.component';
import { UserLikeComponent } from './pages/userlike/userlike.component';
import { RouterModule } from '@angular/router';
import { GroupComponent } from './pages/group/group.component'; // Import RouterModule


@NgModule({
  declarations:
  [
    AppComponent,
    LoginComponent,
    ProfilComponent,
    MovieCardComponent,
    UserLikeComponent,
    GroupComponent
],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule,
    BrowserModule
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }