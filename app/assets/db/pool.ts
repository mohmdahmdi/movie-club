import { Pool } from "pg";

const pool = new Pool({
  host: process.env.PGHOST,
  port: 5432, // fix this in the future
  user: process.env.PGUSER,
  password: process.env.PGPASSWORD,
  database: process.env.PGDATABASE,
});

export default pool;
