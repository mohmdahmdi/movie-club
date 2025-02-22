import pool from "@/app/assets/db/pool";
import { ISliderPostRequest } from "@/app/assets/interfaces/endpoints";
import { NextResponse } from "next/server";

export async function GET() {
  const query = `SELECT slider.url, movie.* 
    FROM slider, movie 
    WHERE slider.movie_id = movie.movie_id 
    ORDER BY slider_id DESC LIMIT 8`;
  try {
    const { rows } = await pool.query(query);
    return NextResponse.json(rows, { status: 200 });
  } catch (e) {
    console.log("Error in getting data from pool:\n" + e);
    return NextResponse.json("internal server error.", { status: 500 });
  }
}

export async function POST(req: Request) {
  const data: ISliderPostRequest = await req.json();
  if (data.slider_id) {
    try {
      await pool.query(
        "UPDATE slider SET url = $1, movie_id = $2 WHERE slider_id = $3",
        [data.url, data.movie_id, data.slider_id]
      );
      return NextResponse.json("Slider updated successfully", { status: 200 });
    } catch (e) {
      console.log("Error in updating data from pool:\n" + e);
      return NextResponse.json("Pass the slider_id parameter if you want to update a row.", { status: 400 });
    }
  } else {
    try { 
      await pool.query(
        "INSERT INTO slider (url, movie_id) VALUES ($1, $2)",
        [data.url, data.movie_id]
      )
      return NextResponse.json("Slider inserted successfully", { status: 200 });
    } catch(e) {
      console.log("Error in inserting values in db:\n" + e);
      return NextResponse.json("internal server error", { status: 500 });
    }
  }
}
