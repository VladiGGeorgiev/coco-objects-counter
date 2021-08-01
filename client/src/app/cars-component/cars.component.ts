import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'cars-component',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css']
})
export class CarsComponent implements OnInit {
  loading: boolean = false;
  numberOfCars: number = 0;
  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  uploadFile(event: any) {
    this.loading = true;
    let file = event.target.files[0];
    let formData = new FormData();
    formData.append('file', file, file.name);

    this.apiService.uploadFile(formData).subscribe(data => {
      this.numberOfCars = data;
      this.loading = false;
    })
  }
}
