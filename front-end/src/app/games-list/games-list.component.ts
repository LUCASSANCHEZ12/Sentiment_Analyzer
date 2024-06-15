import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Review {
  id: number;
  author: string;
  date: string;
  rating: string;
  content: string;
}

interface Game {
  title: string;
  description: string;
  reviews: Review[];
}

@Component({
  selector: 'app-games-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './games-list.component.html',
  styleUrls: ['./games-list.component.css']
})
export class GamesListComponent {
  selectedGame: Game | null = null;

  games: Game[] = [
    {
      title: 'Game Title',
      description: 'This is a brief description of the game, showcasing its key features and highlights.',
      reviews: [
        {
          id: 1,
          author: 'John Doe',
          date: '2 days ago',
          rating: 'Positive',
          content: 'This game is amazing! I\'ve been playing it for hours and can\'t get enough. The graphics are stunning, the gameplay is smooth, and the story is engaging. Highly recommended!',
        },
        {
          id: 2,
          author: 'Jane Smith',
          date: '1 week ago',
          rating: 'Negative',
          content: 'I was really disappointed with this game. The controls felt clunky, the story was lackluster, and the graphics were not up to par. I wouldn\'t recommend this to anyone.',
        },
      ],
    },
    {
      title: 'Another Game',
      description: 'This is a brief description of the game, showcasing its key features and highlights.',
      reviews: [
        {
          id: 1,
          author: 'John Doe',
          date: '3 days ago',
          rating: 'Positive',
          content: 'This game is really fun! The gameplay is addictive and the graphics are great. I\'ve been playing it non-stop.',
        },
        {
          id: 2,
          author: 'Jane Smith',
          date: '1 week ago',
          rating: 'Negative',
          content: 'I was disappointed with this game. The story was not very engaging and the controls felt unresponsive. I wouldn\'t recommend it.',
        },
      ],
    },
  ];

  constructor() {}

  selectGame(game: Game): void {
    this.selectedGame = game;
  }
}
