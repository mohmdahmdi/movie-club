import pool from "@/app/assets/db/pool";
import { ITagPostRequest } from "@/app/assets/interfaces/endpoints";

export async function POST(req: Request) {
  try {
    const data : ITagPostRequest = await req.json();

    await pool.query(
      `INSERT INTO tag(name) VALUES ($1)`,
      [data.name]
    );

    return new Response(
      JSON.stringify({ message: "Tag added successfully." }),
      { status: 201 }
    );
  } catch (err) {
    console.log("Error inserting tag:", err);

    // Return error response
    return new Response(JSON.stringify({ message: "Failed to add tag." }), {
      status: 500,
    });
  }
}
