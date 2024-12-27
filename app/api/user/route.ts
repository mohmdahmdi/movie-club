import pool from "@/app/assets/db/pool";

export async function GET(req: Request) {
  const admin = await req.json();
  console.log(pool, admin);
}
