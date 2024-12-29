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

// tag endpoint interfaces
export interface ITagPostRequest {
  name: string;
}

// follow endpoint interfaces
export interface IFollowRequest {
  followerId: number;
  followedId: number;
}

// watched endpoint interfaces
export interface IWatchedPostRequest {
  user_id: number;
  movie_id: number;
  watched_at?: Date;
}

export interface IWatchedDeleteRequest {
  user_id: number;
  movie_id: number;
}

// like endpoint interfaces
export interface ILikePostRequest {
  user_id: number;
  movie_id?: string;
  review_id?: string;
  list_id?:number;
  created_at?: Date;
}


export interface ILikeDeleteRequest {
  like_id: number;
}
