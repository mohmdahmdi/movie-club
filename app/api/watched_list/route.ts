import pool from "@/app/assets/db/pool";
import {
  IWatchedDeleteRequest,
  IWatchedPostRequest,
} from "@/app/assets/interfaces/endpoints";

export async function GET(req: Request) {
  try {
    // Get user_id from query parameters
    const url = new URL(req.url);
    const userId = url.searchParams.get("user_id");

    if (!userId) {
      return new Response(
        JSON.stringify({ error: "Missing user_id query parameter" }),
        { status: 400 }
      );
    }

    // Validate that userId is a valid number
    const user_id = parseInt(userId, 10);
    if (isNaN(user_id)) {
      return new Response(JSON.stringify({ error: "Invalid user_id" }), {
        status: 400,
      });
    }

    // Use parameterized query to prevent SQL injection
    const result = await pool.query(
      `SELECT * FROM watched WHERE user_id = ${user_id}`
    );

    // Return the list of watched movies for the user
    return new Response(JSON.stringify(result.rows), {
      status: 200,
    });
  } catch (err) {
    console.error("Error fetching watched movies:", err);
    return new Response(
      JSON.stringify({ error: "Failed to fetch watched movies." }),
      { status: 500 }
    );
  }
}

export async function POST(req: Request) {
  try {
    const data: IWatchedPostRequest = await req.json();

    // Use parameterized queries to avoid SQL injection
    await pool.query(
      `INSERT INTO watched (user_id, movie_id, watched_at) VALUES ($1, $2, $3)`,
      [data.user_id, data.movie_id, data.watched_at || "DEFAULT"]
    );

    // If insertion was successful, return success message
    return new Response(
      JSON.stringify({
        message: "Movie added to watched list successfully.",
      }),
      { status: 200 }
    );
  } catch (err) {
    // If error occurred during insertion, return error message
    console.error("Error adding watched movie:", err);
    return new Response(
      JSON.stringify({ error: "Failed to add movie to watched list." }),
      { status: 500 }
    );
  }
}

export async function DELETE(req: Request) {
  try {
    const data: IWatchedDeleteRequest = await req.json();

    // Use parameterized queries to avoid SQL injection
    const result = await pool.query(
      `DELETE FROM watched WHERE user_id = ${data.user_id} AND movie_id = ${data.movie_id}`
    );

    // Check if any rows were affected (i.e., the record existed)
    if (result.rowCount === 0) {
      return new Response(
        JSON.stringify({ error: "No such watched record found." }),
        { status: 404 }
      );
    }

    // If record was found, return success message
    return new Response(
      JSON.stringify({
        message: "Movie removed from watched list successfully.",
      }),
      { status: 200 }
    );
  } catch (err) {
    // If error occurred during deletion, return error message
    console.error("Error deleting watched movie:", err);
    return new Response(
      JSON.stringify({ error: "Failed to remove movie from watched list." }),
      { status: 500 }
    );
  }
}
