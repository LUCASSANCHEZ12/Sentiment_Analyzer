import { Routes } from '@angular/router';
import { provideRouter } from '@angular/router';
import { GamesListComponent } from './games-list/games-list.component';

export const routes: Routes = [
  { path: '', component: GamesListComponent },
  { path: '**', redirectTo: '' }
];

export const appRouterProviders = [
  provideRouter(routes)
];
