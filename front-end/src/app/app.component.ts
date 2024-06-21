import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { GamesListComponent } from './games-list/games-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, GamesListComponent],
  template: '<app-games-list></app-games-list>',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Reviews';
}
