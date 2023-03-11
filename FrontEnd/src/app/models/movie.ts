export interface Movie {
  id: number;
  name: string;
  overview: string;
  genres: Array<string>;
  poster_path: string;
  runtime: number;
  note_average: number;
}
