const express = require('express');
const jwt     = require('jsonwebtoken');
const { pool } = require('./db');

const router = express.Router();
const JWT_SECRET   = process.env.JWT_SECRET   || 'safety-first-secret-change-in-prod';
const ADMIN_USER   = process.env.ADMIN_USER   || 'admin';
const ADMIN_PASS   = process.env.ADMIN_PASS   || 'safety2024';
const ADMIN_SECRET = process.env.ADMIN_SECRET || 'admin-secret-change-in-prod';

function requireUser(req, res, next) {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith('Bearer ')) return res.status(401).json({ error: 'Non authentifié.' });
  try { req.user = jwt.verify(auth.slice(7), JWT_SECRET); next(); }
  catch { res.status(401).json({ error: 'Token invalide ou expiré.' }); }
}

function requireAdmin(req, res, next) {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith('Bearer ')) return res.status(401).json({ error: 'Non autorisé.' });
  try {
    const payload = jwt.verify(auth.slice(7), ADMIN_SECRET);
    if (payload.role !== 'admin') throw new Error();
    next();
  } catch { res.status(403).json({ error: 'Accès admin requis.' }); }
}

// ── POST /api/admin/login ──
router.post('/admin/login', (req, res) => {
  const { username, password } = req.body;
  if (username === ADMIN_USER && password === ADMIN_PASS) {
    const token = jwt.sign({ role: 'admin' }, ADMIN_SECRET, { expiresIn: '12h' });
    return res.json({ ok: true, token });
  }
  res.status(401).json({ error: 'Identifiants admin incorrects.' });
});

// ── GET /api/dashboard ──
router.get('/dashboard', requireUser, async (req, res) => {
  try {
    const result = await pool.query(
      `SELECT days, unsafe, sif, quiz,
              moment_title_fr, moment_title_en,
              moment_text_fr, moment_text_en,
              moment_btn_fr, moment_btn_en,
              camp1_name_fr, camp1_name_en, camp1_url,
              camp2_name_fr, camp2_name_en, camp2_url,
              updated_at
       FROM dashboard_data ORDER BY id DESC LIMIT 1`
    );
    res.json(result.rows[0] || {});
  } catch (err) { console.error(err); res.status(500).json({ error: 'Erreur serveur.' }); }
});

// ── PUT /api/dashboard ── (admin)
router.put('/dashboard', requireAdmin, async (req, res) => {
  const {
    days, unsafe, sif, quiz,
    moment_title_fr, moment_title_en,
    moment_text_fr, moment_text_en,
    moment_btn_fr, moment_btn_en,
    camp1_name_fr, camp1_name_en, camp1_url,
    camp2_name_fr, camp2_name_en, camp2_url,
  } = req.body;
  try {
    const existing = await pool.query('SELECT id FROM dashboard_data LIMIT 1');
    const vals = [
      days, unsafe, sif, quiz,
      moment_title_fr, moment_title_en,
      moment_text_fr, moment_text_en,
      moment_btn_fr, moment_btn_en,
      camp1_name_fr, camp1_name_en, camp1_url || '',
      camp2_name_fr, camp2_name_en, camp2_url || '',
    ];
    if (existing.rows.length === 0) {
      await pool.query(
        `INSERT INTO dashboard_data
         (days,unsafe,sif,quiz,moment_title_fr,moment_title_en,moment_text_fr,moment_text_en,
          moment_btn_fr,moment_btn_en,camp1_name_fr,camp1_name_en,camp1_url,
          camp2_name_fr,camp2_name_en,camp2_url)
         VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16)`, vals
      );
    } else {
      await pool.query(
        `UPDATE dashboard_data SET
         days=$1,unsafe=$2,sif=$3,quiz=$4,
         moment_title_fr=$5,moment_title_en=$6,
         moment_text_fr=$7,moment_text_en=$8,
         moment_btn_fr=$9,moment_btn_en=$10,
         camp1_name_fr=$11,camp1_name_en=$12,camp1_url=$13,
         camp2_name_fr=$14,camp2_name_en=$15,camp2_url=$16,
         updated_at=NOW() WHERE id=$17`,
        [...vals, existing.rows[0].id]
      );
    }
    res.json({ ok: true, updated_at: new Date().toISOString() });
  } catch (err) { console.error(err); res.status(500).json({ error: 'Erreur serveur.' }); }
});

// ── GET /api/users ── (admin)
router.get('/users', requireAdmin, async (req, res) => {
  try {
    const result = await pool.query(
      'SELECT id, name, email, employee_id, verified, created_at FROM users ORDER BY created_at DESC'
    );
    res.json(result.rows);
  } catch (err) { res.status(500).json({ error: 'Erreur serveur.' }); }
});

// ── POST /api/reports ── (user — submit incident report)
router.post('/reports', requireUser, async (req, res) => {
  const { report_type, location, incident_date, description, actions_taken, photo_url } = req.body;
  if (!report_type || !description) return res.status(400).json({ error: 'Type et description requis.' });
  try {
    await pool.query(
      `INSERT INTO incident_reports
       (reporter_id, reporter_email, report_type, location, incident_date, description, actions_taken, photo_url)
       VALUES ($1,$2,$3,$4,$5,$6,$7,$8)`,
      [req.user.id, req.user.email, report_type, location || '', incident_date || '', description, actions_taken || '', photo_url || '']
    );
    res.json({ ok: true, message: 'Rapport soumis avec succès.' });
  } catch (err) { console.error(err); res.status(500).json({ error: 'Erreur serveur.' }); }
});

// ── GET /api/reports ── (admin — view all reports)
router.get('/reports', requireAdmin, async (req, res) => {
  try {
    const result = await pool.query(
      `SELECT r.*, u.name as reporter_name FROM incident_reports r
       LEFT JOIN users u ON u.id = r.reporter_id
       ORDER BY r.created_at DESC`
    );
    res.json(result.rows);
  } catch (err) { res.status(500).json({ error: 'Erreur serveur.' }); }
});

module.exports = { router, requireUser, requireAdmin };

