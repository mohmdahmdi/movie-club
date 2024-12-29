import pool from "@/app/assets/db/pool";
import {
  ILikeDeleteRequest,
  ILikePostRequest,
} from "@/app/assets/interfaces/endpoints";

export async function POST(req: Request) {
  try {
    const data: ILikePostRequest = await req.json();

    await pool.query(
      `INSERT INTO like (user_id, movie_id, review_id, list_id, created_at) VALUES ($1, $2, $3, $4, $5)`,
      [
        data.user_id,
        data.movie_id || "NULL",
        data.review_id || "NULL",
        data.list_id || "NULL",
        data.created_at || "CURRENT_TIMESTAMP",
      ]
    );

    return new Response(
      JSON.stringify({ message: "Like added successfully." }),
      {
        status: 201,
      }
    );
  } catch (err) {
    console.error("Error adding like:", err);
    return new Response(JSON.stringify({ message: "Failed to add like." }), {
      status: 500,
    });
  }
}

export async function DELETE(req: Response) {
  try {
    const data: ILikeDeleteRequest = await req.json();

    await pool.query(`DELETE FROM like WHERE like_id = $1`, [data.like_id]);

    return new Response(
      JSON.stringify({ message: "Like deleted successfully." }),
      {
        status: 200,
      }
    );
    
  } catch (err) {
    console.error("Error deleting like:", err);
    return new Response(JSON.stringify({ message: "Failed to delete like." }), {
      status: 500,
    });
  }
}
