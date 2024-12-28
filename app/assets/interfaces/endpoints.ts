

// review endpoint interfaces
export interface IReviewPostRequest {
  user_id: number;
  movie_id: number;
  review_text: string;
  rating?: number;
}

export interface IReviewPutRequest {
  review_id: number;
  review_text?: string;
  rating?: number;
}

export interface IReviewDeleteRequest {
  review_id: number;
}

