import { HttpClient,} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private REST_API_SERVER = "http://localhost:8000/";
  constructor(private httpClient:HttpClient) { }
  getTypeRequest(url: string) {
    return this.httpClient.get(this.REST_API_SERVER+url).pipe(map((res: any) => {
      return res;
    }));
  }

  postTypeRequest(url: string, payload: any) {
    return this.httpClient.post(this.REST_API_SERVER+url, payload).pipe(map((res: any) => {
      return res;
    }));
  }

  putTypeRequest(url: string, payload: any) {
    return this.httpClient.put(this.REST_API_SERVER+url, payload).pipe(map((res: any) => {
      return res;
    }))
  }



}
