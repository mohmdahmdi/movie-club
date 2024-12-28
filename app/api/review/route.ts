import pool from "@/app/assets/db/pool";
import {
  IReviewDeleteRequest,
  IReviewPostRequest,
  IReviewPutRequest,
} from "@/app/assets/interfaces/endpoints";

export async function POST(req: Request) {
  try {
    const data: IReviewPostRequest = await req.json();

    await pool.query(
      `INSERT INTO review (user_id, movie_id, review_text, rating) VALUES ($1, $2, $3, $4)`,
      [
        data.user_id,
        data.movie_id,
        data.review_text,
        data.rating ? data.rating : null,
      ]
    );

    return new Response(
      JSON.stringify({ message: "Review added successfully." }),
      { status: 201 }
    );
  } catch (err) {
    console.error("Error adding review:", err);
    return new Response(JSON.stringify({ message: "Failed to add review." }), {
      status: 500,
    });
  }
}

export async function PUT(req: Request) {
  try {
    const data: IReviewPutRequest = await req.json();

    if (data.rating != null && data.review_text == null) {
      await pool.query(`UPDATE review SET rating = $1 WHERE id = $2`, [
        data.rating,
        data.review_id,
      ]);
    } else if (data.rating == null && data.review_text != null) {
      await pool.query(`UPDATE review SET review_text = $1 WHERE id = $2`, [
        data.review_text,
        data.review_id,
      ]);
    } else if (data.rating != null && data.review_text != null) {
      await pool.query(
        `UPDATE review SET rating = $1, review_text = $2 WHERE id = $3`,
        [data.rating, data.review_text, data.review_id]
      );
    } else {
      return new Response(
        JSON.stringify({ message: "No changes made to the review." }),
        { status: 200 }
      );
    }

    return new Response(
      JSON.stringify({ message: "Review updated successfully." }),
      { status: 200 }
    );
  } catch (err) {
    console.error("Error updating review:", err);
    return new Response(
      JSON.stringify({ message: "Failed to update review." }),
      { status: 500 }
    );
  }
}

export async function DELETE(req: Request) {
  try {
    const data: IReviewDeleteRequest = await req.json();
    await pool.query(`DELETE FROM review WHERE id = $1`, [data.review_id]);

    return new Response(
      JSON.stringify({ message: "Review deleted successfully." }),
      { status: 200 }
    );
  } catch (err) {
    console.error("Error deleting review:", err);
    return new Response(
      JSON.stringify({ message: "Failed to delete review." }),
      { status: 500 }
    );
  }
}
