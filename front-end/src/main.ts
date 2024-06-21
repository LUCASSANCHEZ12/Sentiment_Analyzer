// main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { appRouterProviders } from './app/app.routes';
import { provideHttpClient, withFetch } from '@angular/common/http';

bootstrapApplication(AppComponent, {
  providers: [
    appRouterProviders,
    provideHttpClient(withFetch())  // Aquí se configura el HttpClient con fetch
  ]
}).catch(err => console.error(err));
