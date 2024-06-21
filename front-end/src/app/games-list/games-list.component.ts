// games-list.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../api.service';
import { Game, Review } from '../interfaces/games';

@Component({
  selector: 'app-games-list',
  standalone: true,
  imports: [CommonModule, FormsModule], // Importa FormsModule aquí
  templateUrl: './games-list.component.html',
  styleUrls: ['./games-list.component.css']
})
export class GamesListComponent implements OnInit {
  gameTitles: string[] = [];
  displayedTitles: string[] = [];
  selectedGame: Game | null = null;  
  gameReviews: Review[] = [];
  newReviewText: string = '';

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadGameTitles();
  }

  loadGameTitles(): void {
    this.apiService.getGameTitles().subscribe((titles: string[]) => {
      this.iterateTitles(titles);
    });
  }

  iterateTitles(titles: string[]): void {
    if (titles.length > 0) {
      const currentTitle = titles[0];
      this.displayedTitles.push(currentTitle);
      setTimeout(() => this.iterateTitles(titles.slice(1)), 500); // Pasa la parte restante de la lista
    }
  }

  loadGameReviews(gameTitle: string): void {
    this.apiService.getGameReviews(gameTitle).subscribe((reviews: Review[]) => {
      this.selectedGame = { title: gameTitle, reviews : {}};
      this.gameReviews = reviews;
    });
  }

  submitReview(): void {
    if (this.selectedGame) {
      this.apiService.addReview(this.selectedGame.title, this.newReviewText).subscribe(response => {
        console.log('Review added:', response);
        this.newReviewText = '';
        this.loadGameReviews(this.selectedGame!.title); // Reload reviews after adding new one
      }, error => {
        console.error('Error adding review:', error);
      });
    }
  }
}
