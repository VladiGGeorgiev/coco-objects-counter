import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly ApiUrl = 'http://localhost:8000/';

  constructor(private http: HttpClient) { }

  uploadFile(file: any): Observable<any> {
    return this.http.post(this.ApiUrl + 'upload/', file);
  }
}
