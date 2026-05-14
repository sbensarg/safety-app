const express  = require('express');
const bcrypt   = require('bcryptjs');
const jwt      = require('jsonwebtoken');
const speakeasy = require('speakeasy');
const qrcode   = require('qrcode');
const { pool } = require('./db');

const router = express.Router();
const JWT_SECRET = process.env.JWT_SECRET || 'safety-first-secret-change-in-prod';

// ── POST /api/auth/register ──
// No domain restriction, no email verification — just create account + setup 2FA
router.post('/register', async (req, res) => {
  const { name, email, employee_id, password } = req.body;

  if (!name || !email || !password)
    return res.status(400).json({ error: 'Champs obligatoires manquants.' });

  if (password.length < 8)
    return res.status(400).json({ error: 'Le mot de passe doit comporter au moins 8 caractères.' });

  try {
    const existing = await pool.query('SELECT id FROM users WHERE email=$1', [email.toLowerCase()]);
    if (existing.rows.length > 0)
      return res.status(409).json({ error: 'Un compte avec cet email existe déjà.' });

    const hashed = await bcrypt.hash(password, 12);

    // Generate 2FA secret immediately on registration
    const secret = speakeasy.generateSecret({
      name: `Safety First (${email})`,
      issuer: 'TK Home Solutions',
      length: 20,
    });

    await pool.query(
      `INSERT INTO users (name, email, employee_id, password, two_fa_secret, two_fa_enabled)
       VALUES ($1, $2, $3, $4, $5, FALSE)`,
      [name, email.toLowerCase(), employee_id || null, hashed, secret.base32]
    );

    // Return QR code so user can scan it in their authenticator app
    const qrDataURL = await qrcode.toDataURL(secret.otpauth_url);

    res.json({
      ok: true,
      message: 'Compte créé. Scannez le QR code avec votre application 2FA.',
      qr_code: qrDataURL,
      secret_key: secret.base32, // shown as fallback if QR doesn't scan
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Erreur serveur.' });
  }
});

// ── POST /api/auth/verify-2fa-setup ──
// After scanning QR, user confirms with first OTP to enable 2FA
router.post('/verify-2fa-setup', async (req, res) => {
  const { email, otp } = req.body;
  if (!email || !otp)
    return res.status(400).json({ error: 'Email et code OTP requis.' });

  try {
    const result = await pool.query('SELECT * FROM users WHERE email=$1', [email.toLowerCase()]);
    if (result.rows.length === 0)
      return res.status(404).json({ error: 'Utilisateur non trouvé.' });

    const user = result.rows[0];

    const verified = speakeasy.totp.verify({
      secret:   user.two_fa_secret,
      encoding: 'base32',
      token:    otp.replace(/\s/g, ''),
      window:   2,
    });

    if (!verified)
      return res.status(400).json({ error: 'Code incorrect. Vérifiez votre application et réessayez.' });

    await pool.query('UPDATE users SET two_fa_enabled=TRUE WHERE id=$1', [user.id]);

    res.json({ ok: true, message: '2FA activé avec succès. Vous pouvez maintenant vous connecter.' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Erreur serveur.' });
  }
});

// ── POST /api/auth/login ──
// Step 1: verify email + password → return needs_2fa
router.post('/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password)
    return res.status(400).json({ error: 'Email et mot de passe requis.' });

  try {
    const result = await pool.query('SELECT * FROM users WHERE email=$1', [email.toLowerCase()]);
    if (result.rows.length === 0)
      return res.status(401).json({ error: 'Email ou mot de passe incorrect.' });

    const user = result.rows[0];
    const match = await bcrypt.compare(password, user.password);
    if (!match)
      return res.status(401).json({ error: 'Email ou mot de passe incorrect.' });

    if (!user.two_fa_enabled)
      return res.status(403).json({ error: '2FA non configuré. Veuillez terminer la configuration de votre compte.', needs_2fa_setup: true });

    // Credentials OK — ask for OTP next
    res.json({ ok: true, needs_2fa: true, email: user.email });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Erreur serveur.' });
  }
});

// ── POST /api/auth/login-2fa ──
// Step 2: verify OTP → return full JWT
router.post('/login-2fa', async (req, res) => {
  const { email, otp } = req.body;

  if (!email || !otp)
    return res.status(400).json({ error: 'Email et code OTP requis.' });

  try {
    const result = await pool.query('SELECT * FROM users WHERE email=$1', [email.toLowerCase()]);
    if (result.rows.length === 0)
      return res.status(401).json({ error: 'Utilisateur non trouvé.' });

    const user = result.rows[0];

    const verified = speakeasy.totp.verify({
      secret:   user.two_fa_secret,
      encoding: 'base32',
      token:    otp.replace(/\s/g, ''),
      window:   2, // allow ±2 time steps (60 sec tolerance)
    });

    if (!verified)
      return res.status(401).json({ error: 'Code incorrect ou expiré. Réessayez.' });

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

module.exports = router;
