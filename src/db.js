const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: false } : false,
});

async function initDB() {
  const client = await pool.connect();
  try {
    await client.query(`
      CREATE TABLE IF NOT EXISTS users (
        id              SERIAL PRIMARY KEY,
        name            VARCHAR(200) NOT NULL,
        email           VARCHAR(200) UNIQUE NOT NULL,
        employee_id     VARCHAR(50),
        password        VARCHAR(200) NOT NULL,
        two_fa_secret   VARCHAR(200),
        two_fa_enabled  BOOLEAN DEFAULT FALSE,
        created_at      TIMESTAMP DEFAULT NOW()
      );

      CREATE TABLE IF NOT EXISTS dashboard_data (
        id               SERIAL PRIMARY KEY,
        days             INTEGER DEFAULT 0,
        unsafe           INTEGER DEFAULT 0,
        sif              INTEGER DEFAULT 0,
        quiz             INTEGER DEFAULT 0,
        moment_title_fr  TEXT DEFAULT 'Moment Securite',
        moment_title_en  TEXT DEFAULT 'Safety Moment',
        moment_text_fr   TEXT DEFAULT 'Le message de securite de la semaine apparaitra ici.',
        moment_text_en   TEXT DEFAULT 'Safety message or awareness content will appear here.',
        moment_btn_fr    TEXT DEFAULT 'Lire plus',
        moment_btn_en    TEXT DEFAULT 'Read More',
        camp1_name_fr    TEXT DEFAULT 'Campagne 1',
        camp1_name_en    TEXT DEFAULT 'Campaign 1',
        camp1_url        TEXT DEFAULT '',
        camp2_name_fr    TEXT DEFAULT 'Campagne 2',
        camp2_name_en    TEXT DEFAULT 'Campaign 2',
        camp2_url        TEXT DEFAULT '',
        updated_at       TIMESTAMP DEFAULT NOW(),
        updated_by       VARCHAR(200) DEFAULT 'admin'
      );

      INSERT INTO dashboard_data (days, unsafe, sif, quiz)
      SELECT 1037, 127, 1, 15
      WHERE NOT EXISTS (SELECT 1 FROM dashboard_data);

      CREATE TABLE IF NOT EXISTS incident_reports (
        id              SERIAL PRIMARY KEY,
        reporter_id     INTEGER REFERENCES users(id),
        reporter_email  VARCHAR(200),
        report_type     VARCHAR(100),
        location        VARCHAR(300),
        incident_date   VARCHAR(100),
        description     TEXT,
        actions_taken   TEXT,
        photo_url       TEXT,
        created_at      TIMESTAMP DEFAULT NOW()
      );
    `);

    await client.query(`ALTER TABLE users ADD COLUMN IF NOT EXISTS two_fa_secret  VARCHAR(200);`).catch(()=>{});
    await client.query(`ALTER TABLE users ADD COLUMN IF NOT EXISTS two_fa_enabled BOOLEAN DEFAULT FALSE;`).catch(()=>{});
    await client.query(`ALTER TABLE users DROP COLUMN IF EXISTS verified;`).catch(()=>{});
    await client.query(`ALTER TABLE users DROP COLUMN IF EXISTS verify_token;`).catch(()=>{});

    console.log('Database initialized');
  } finally {
    client.release();
  }
}

module.exports = { pool, initDB };
