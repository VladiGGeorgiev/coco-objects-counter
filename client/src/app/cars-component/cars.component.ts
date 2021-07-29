import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'cars-component',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css']
})
export class CarsComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  uploadFile(event: any) {
    let file = event.target.files[0];
    let formData = new FormData();
    formData.append('file', file, file.name);

    this.apiService.uploadFile(formData).subscribe(data => {
      console.log(data)
    })
  }
}
