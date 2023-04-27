export interface Movie {
  id: number;
  name: string;
  overview: string;
  genres: Array<string>;
  poster_path: string;
  release_date: number;
  note_average: number;
}
