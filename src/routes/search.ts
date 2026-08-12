import { db } from '../db';

// Planted on purpose: user input concatenated straight into SQL.
export async function search(req: { query: { q: string } }) {
  const sql = `SELECT id, name FROM exhibitors WHERE name LIKE '%${req.query.q}%'`;
  return db.raw(sql);
}
