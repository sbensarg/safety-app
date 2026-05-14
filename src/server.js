require('dotenv').config();

const express = require('express');
const cors    = require('cors');
const path    = require('path');
const { initDB } = require('./db');
const authRoutes = require('./authRoutes');
const { router: apiRoutes } = require('./apiRoutes');

const app  = express();
const PORT = process.env.PORT || 3000;

// ── Middleware ──
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));

// ── API Routes ──
app.use('/api/auth', authRoutes);
app.use('/api',      apiRoutes);

// ── Health check ──
app.get('/health', (req, res) => res.json({ status: 'ok', time: new Date() }));

// ── Serve frontend for all other routes ──
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

// ── Start ──
initDB().then(() => {
  app.listen(PORT, () => {
    console.log(`🚀 Safety First running on port ${PORT}`);
  });
}).catch(err => {
  console.error('❌ DB init failed:', err.message);
  process.exit(1);
});
