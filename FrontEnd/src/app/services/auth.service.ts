import { Injectable } from '@angular/core';
import { UserService } from './user.service';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
API_URL = 'http://localhost:8001/';
constructor(private httpClient:HttpClient) { }

// authentification
login(user: any) {
    return this.httpClient.post(this.API_URL+"login", user);
}
//check tocken
checkToken() {
    return this.httpClient.get(this.API_URL+'test_jwt');
}



setDataInLocalStorage(variableName: any, data: any) {
    localStorage.setItem(variableName, data);
}

getToken() {
    return localStorage.getItem('token');
}

clearStorage() {
    localStorage.clear();
}
}
