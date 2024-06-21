export interface Review {
  review: string;
  value: number;
}

export interface Game {
  title: string;
  reviews: { [key: string]: Review };
}
