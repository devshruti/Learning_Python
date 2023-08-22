import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  dishes: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.fetchDishes();
  }

  fetchDishes() {
    const apiUrl = 'https://www.themealdb.com/api/json/v1/1/search.php?s=';
    
    this.http.get(apiUrl).subscribe((data: any) => {
      // Process the data here and assign it to this.dishes
      this.dishes = data.meals;
    });
  }
}
