const express = require('express');
const bcrypt  = require('bcryptjs');
const jwt     = require('jsonwebtoken');
const { v4: uuidv4 } = require('uuid');
const nodemailer = require('nodemailer');
const { pool } = require('./db');

const router = express.Router();

const ALLOWED_DOMAIN = '@tkelevator.com';
const JWT_SECRET     = process.env.JWT_SECRET || 'safety-first-secret-change-in-prod';
const APP_URL        = process.env.APP_URL || 'http://localhost:3000';

// ── Email transporter (configure with your SMTP) ──
function getMailer() {
  return nodemailer.createTransport({
    host:   process.env.SMTP_HOST   || 'smtp.gmail.com',
    port:   parseInt(process.env.SMTP_PORT || '587'),
    secure: false,
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS,
    },
  });
}

// ── POST /api/auth/register ──
router.post('/register', async (req, res) => {
  const { name, email, employee_id, password } = req.body;

  if (!name || !email || !password) {
    return res.status(400).json({ error: 'Champs obligatoires manquants.' });
  }

  if (!email.toLowerCase().endsWith(ALLOWED_DOMAIN)) {
    return res.status(400).json({ error: `Seules les adresses ${ALLOWED_DOMAIN} sont autorisées.` });
  }

  if (password.length < 8) {
    return res.status(400).json({ error: 'Le mot de passe doit comporter au moins 8 caractères.' });
  }

  try {
    const existing = await pool.query('SELECT id FROM users WHERE email=$1', [email.toLowerCase()]);
    if (existing.rows.length > 0) {
      return res.status(409).json({ error: 'Un compte avec cet email existe déjà.' });
    }

    const hashed      = await bcrypt.hash(password, 12);
    const verifyToken = uuidv4();

    await pool.query(
      `INSERT INTO users (name, email, employee_id, password, verify_token)
       VALUES ($1, $2, $3, $4, $5)`,
      [name, email.toLowerCase(), employee_id || null, hashed, verifyToken]
    );

    // Send verification email
    const verifyURL = `${APP_URL}/api/auth/verify/${verifyToken}`;
    try {
      const mailer = getMailer();
      await mailer.sendMail({
        from:    `"Safety First - TK Home Solutions" <${process.env.SMTP_USER}>`,
        to:      email,
        subject: 'Vérifiez votre adresse email — Safety First',
        html: `
          <div style="font-family:sans-serif;max-width:500px;margin:0 auto;padding:24px;">
            <h2 style="color:#6b21a8;">Safety First — TK Home Solutions</h2>
            <p>Bonjour <strong>${name}</strong>,</p>
            <p>Merci de vous être inscrit. Cliquez sur le bouton ci-dessous pour activer votre compte :</p>
            <a href="${verifyURL}"
               style="display:inline-block;margin:20px 0;padding:14px 28px;background:linear-gradient(135deg,#6b21a8,#ea580c);color:white;border-radius:8px;text-decoration:none;font-weight:700;">
              Vérifier mon email
            </a>
            <p style="color:#888;font-size:13px;">Ce lien expire dans 24h. Si vous n'avez pas créé de compte, ignorez cet email.</p>
          </div>
        `,
      });
    } catch (mailErr) {
      console.error('Email send error:', mailErr.message);
      // Continue — account created, email failed silently
    }

    res.json({ ok: true, message: 'Compte créé. Vérifiez votre email.' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Erreur serveur.' });
  }
});

// ── GET /api/auth/verify/:token ──
router.get('/verify/:token', async (req, res) => {
  const { token } = req.params;
  try {
    const result = await pool.query(
      `UPDATE users SET verified=TRUE, verify_token=NULL
       WHERE verify_token=$1 RETURNING email`,
      [token]
    );
    if (result.rows.length === 0) {
      return res.status(400).send(`
        <html><body style="font-family:sans-serif;text-align:center;padding:60px;">
          <h2 style="color:#ef4444;">Lien invalide ou expiré.</h2>
          <a href="/">Retour à l'accueil</a>
        </body></html>
      `);
    }
    res.send(`
      <html><body style="font-family:sans-serif;text-align:center;padding:60px;background:#f0ecf8;">
        <h2 style="color:#6b21a8;">✅ Email vérifié avec succès !</h2>
        <p>Votre compte est maintenant actif.</p>
        <a href="/" style="display:inline-block;margin-top:20px;padding:12px 28px;background:linear-gradient(135deg,#6b21a8,#ea580c);color:white;border-radius:8px;text-decoration:none;font-weight:700;">
          Se connecter
        </a>
      </body></html>
    `);
  } catch (err) {
    console.error(err);
    res.status(500).send('Erreur serveur.');
  }
});

// ── POST /api/auth/login ──
router.post('/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email et mot de passe requis.' });
  }

  if (!email.toLowerCase().endsWith(ALLOWED_DOMAIN)) {
    return res.status(400).json({ error: `Seules les adresses ${ALLOWED_DOMAIN} sont autorisées.` });
  }

  try {
    const result = await pool.query('SELECT * FROM users WHERE email=$1', [email.toLowerCase()]);
    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'Email ou mot de passe incorrect.' });
    }

    const user = result.rows[0];

    if (!user.verified) {
      return res.status(403).json({ error: 'Veuillez vérifier votre email avant de vous connecter.' });
    }

    const match = await bcrypt.compare(password, user.password);
    if (!match) {
      return res.status(401).json({ error: 'Email ou mot de passe incorrect.' });
    }

    const token = jwt.sign(
      { id: user.id, email: user.email, name: user.name },
      JWT_SECRET,
      { expiresIn: '8h' }
    );

    res.json({
      ok: true,
      token,
      user: { id: user.id, name: user.name, email: user.email }
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Erreur serveur.' });
  }
});

// ── POST /api/auth/resend-verification ──
router.post('/resend-verification', async (req, res) => {
  const { email } = req.body;
  try {
    const result = await pool.query('SELECT * FROM users WHERE email=$1', [email.toLowerCase()]);
    if (result.rows.length === 0) return res.status(404).json({ error: 'Email non trouvé.' });

    const user = result.rows[0];
    if (user.verified) return res.status(400).json({ error: 'Compte déjà vérifié.' });

    const verifyToken = uuidv4();
    await pool.query('UPDATE users SET verify_token=$1 WHERE id=$2', [verifyToken, user.id]);

    const verifyURL = `${APP_URL}/api/auth/verify/${verifyToken}`;
    const mailer = getMailer();
    await mailer.sendMail({
      from:    `"Safety First" <${process.env.SMTP_USER}>`,
      to:      email,
      subject: 'Nouveau lien de vérification — Safety First',
      html: `<p>Bonjour ${user.name},</p><p><a href="${verifyURL}">Vérifier mon email</a></p>`,
    });

    res.json({ ok: true });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Erreur serveur.' });
  }
});

module.exports = router;
