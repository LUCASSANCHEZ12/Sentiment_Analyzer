// api.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Game, Review } from './app/interfaces/games';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'http://127.0.0.1:8000/reviews';
  constructor(private http: HttpClient) {}

  getGameTitles(): Observable<string[]> {
    return this.http.get<{ [key: string]: any }>(this.baseUrl).pipe(
      map(data => Object.keys(data))
    );
  }

  getGameReviews(gameTitle: string): Observable<Review[]> {
    return this.http.get<Game>(`${this.baseUrl}/${gameTitle}`).pipe(
      map(game => Object.values(game.reviews)) // Convertir objeto de reseñas a un arreglo
    );
  }
  
  addReview(gameTitle: string, review: string): Observable<any> {
    const reviewData = { review: review };
    return this.http.post(`${this.baseUrl}/${gameTitle}/add`, reviewData);
  }
}
