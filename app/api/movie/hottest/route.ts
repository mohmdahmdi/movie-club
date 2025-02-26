import { NextResponse } from "next/server";
import pool from "@/app/assets/db/pool";

export async function GET() {
  const query = `SELECT DISTINCT * FROM movie WHERE title != 'unknown' ORDER BY rating DESC LIMIT 8`;
  try {
    const { rows } = await pool.query(query);
    return NextResponse.json(rows, { status: 200 });
  } catch (e) {
    console.log("Error in getting data from pool:\n" + e);
    return NextResponse.json("internal server error.", { status: 500 });
  }
}
