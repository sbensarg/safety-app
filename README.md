# Safety First — TK Home Solutions

Full-stack workplace safety platform. **100% free deployment** using Render + Neon + Resend.

---

## Free Stack (no credit card needed)

| Service | Purpose | Free limit |
|---------|---------|------------|
| [Render.com](https://render.com) | Backend (Node/Express) + serves frontend | 750h/month |
| [Neon.tech](https://neon.tech) | PostgreSQL database | 0.5 GB forever |
| [Resend.com](https://resend.com) | Email verification | 3,000 emails/month |

Render free tier sleeps after 15min of inactivity (first request ~30s). Fine for internal tools.

---

## Deploy in 10 minutes

### Step 1 — Free PostgreSQL on Neon

1. Go to neon.tech → Sign up free
2. New Project → name it safety-first → Create
3. Copy the Connection string from the dashboard

It looks like:
postgresql://username:password@ep-something.us-east-1.aws.neon.tech/neondb?sslmode=require

Save this — it is your DATABASE_URL.

---

### Step 2 — Free email on Resend

1. Go to resend.com → Sign up free
2. API Keys → Create API Key → copy it

SMTP settings:
  SMTP_HOST = smtp.resend.com
  SMTP_PORT = 587
  SMTP_USER = resend
  SMTP_PASS = re_xxxx   (your Resend API key)

Alternative — Gmail App Password:
  Google Account → Security → 2-Step Verification → App Passwords → Generate
  SMTP_HOST = smtp.gmail.com
  SMTP_USER = your@gmail.com
  SMTP_PASS = (16-char app password)

---

### Step 3 — Push to GitHub

  cd safety-first
  git init
  git add .
  git commit -m "Initial commit"
  git remote add origin https://github.com/YOUR_USERNAME/safety-first.git
  git push -u origin main

---

### Step 4 — Deploy on Render (free)

1. render.com → Sign up free (use GitHub login)
2. New + → Web Service → connect your GitHub repo
3. Fill in:
   - Environment: Node
   - Build Command: npm install
   - Start Command: node src/server.js
   - Plan: Free

4. Add these Environment Variables:

  NODE_ENV          = production
  DATABASE_URL      = (paste your Neon connection string)
  JWT_SECRET        = (random 40+ char string — see below)
  ADMIN_SECRET      = (another random 40+ char string)
  ADMIN_USER        = admin
  ADMIN_PASS        = (choose your admin password)
  SMTP_HOST         = smtp.resend.com
  SMTP_PORT         = 587
  SMTP_USER         = resend
  SMTP_PASS         = (your Resend API key)
  APP_URL           = (leave blank for now)

5. Click Create Web Service → wait ~3 min for first deploy
6. Copy your URL: https://safety-first-xxxx.onrender.com
7. Go back to Environment → add:
   APP_URL = https://safety-first-xxxx.onrender.com

Done! Your app is live.

---

## Generate random secrets

Run in your terminal:
  node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"

Run it twice — once for JWT_SECRET, once for ADMIN_SECRET.

---

## Admin Login

Go to your app → Log In as employee → tap Admin in dashboard header:
  Username: value of ADMIN_USER (default: admin)
  Password: value of ADMIN_PASS (what you set)

---

## API Reference

  POST   /api/auth/register              — Create employee account
  POST   /api/auth/login                 — Login, returns JWT
  GET    /api/auth/verify/:token         — Verify email from link
  POST   /api/auth/resend-verification   — Resend verification email
  POST   /api/admin/login                — Admin login, returns admin JWT
  GET    /api/dashboard                  — Get dashboard data (user JWT)
  PUT    /api/dashboard                  — Update dashboard data (admin JWT)
  GET    /api/users                      — List all users (admin JWT)
  POST   /api/reports                    — Submit incident report (user JWT)
  GET    /api/reports                    — View all reports (admin JWT)
  GET    /health                         — Health check

---

## Local Development

  npm install
  cp .env.example .env
  # Edit .env with your Neon DATABASE_URL and SMTP credentials
  npm run dev
  # Open http://localhost:3000

---

## Email domain restriction

Only @tkelevator.com addresses can register.
To change it, edit src/authRoutes.js:
  const ALLOWED_DOMAIN = '@tkelevator.com';
