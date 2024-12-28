import pool from "@/app/assets/db/pool";
import { IFollowRequest } from "@/app/assets/interfaces/endpoints";

export async function POST(req: Request) {
const data : IFollowRequest = await req.json();

  try {
    // Use parameterized queries to avoid SQL injection
    const result = await pool.query(
      `INSERT INTO follower (follower_id, followed_id) VALUES ($1, $2)`,
      [data.followerId, data.followedId]
    );

    // Return success response
    return new Response(
      JSON.stringify({ message: "Follower added successfully." }),
      {
        status: 201,
      }
    );
  } catch (err) {
    console.error("Error inserting follower:", err);

    // Return error response
    return new Response(
      JSON.stringify({ message: "Failed to add follower." }),
      { status: 500 }
    );
  }
}

export async function DELETE(req: Request) {
  const data : IFollowRequest = await req.json();
   try {
     // Use parameterized queries to avoid SQL injection
     const result = await pool.query(
       `DELETE FROM follower WHERE follower_id = $1 AND followed_id = $2`,
       [data.followerId, data.followedId]
     );

     // Check if any rows were affected (i.e., the relationship existed)
     if (result.rowCount === 0) {
       return new Response(
         JSON.stringify({ message: "Follower relationship not found." }),
         { status: 404 }
       );
     }

     // Return success response
     return new Response(
       JSON.stringify({ message: "Follower removed successfully." }),
       {
         status: 200,
       }
     );
   } catch (err) {
     console.error("Error deleting follower:", err);

     // Return error response
     return new Response(
       JSON.stringify({ message: "Failed to remove follower." }),
       { status: 500 }
     );
   }


}
