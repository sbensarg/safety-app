# Safety First — TK Home Solutions

Full-stack workplace safety platform. Deploy-ready for Railway.

---

## Stack

- **Backend**: Node.js + Express
- **Database**: PostgreSQL (auto-provisioned by Railway)
- **Auth**: JWT + bcrypt + email verification
- **Frontend**: Vanilla HTML/CSS/JS (served by Express)

---

## Project Structure

```
safety-first/
├── public/
│   └── index.html          ← Full frontend (landing + login + dashboard + admin)
├── src/
│   server.js               ← Express entry point
│   db.js                   ← PostgreSQL pool + schema init
│   authRoutes.js           ← /api/auth/* (register, login, verify, resend)
│   apiRoutes.js            ← /api/dashboard, /api/users, /api/admin/login
├── .env.example            ← Copy to .env and fill in values
├── railway.toml            ← Railway deploy config
└── package.json
```

---

## Deploy on Railway (step by step)

### 1. Push to GitHub

```bash
cd safety-first
git init
git add .
git commit -m "Initial commit"
# Create a repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/safety-first.git
git push -u origin main
```

### 2. Create Railway project

1. Go to [railway.app](https://railway.app) → **New Project**
2. Click **Deploy from GitHub repo** → select your repo
3. Railway detects Node.js automatically

### 3. Add PostgreSQL

1. In your Railway project dashboard → **+ New** → **Database** → **PostgreSQL**
2. Railway automatically sets `DATABASE_URL` in your environment ✅

### 4. Set environment variables

In Railway → your service → **Variables** tab, add:

| Variable       | Value                          |
|----------------|-------------------------------|
| `NODE_ENV`     | `production`                   |
| `JWT_SECRET`   | (random 40+ char string)       |
| `ADMIN_SECRET` | (random 40+ char string)       |
| `ADMIN_USER`   | `admin`                        |
| `ADMIN_PASS`   | (your admin password)          |
| `SMTP_HOST`    | `smtp.gmail.com`               |
| `SMTP_PORT`    | `587`                          |
| `SMTP_USER`    | `your-email@gmail.com`         |
| `SMTP_PASS`    | (Gmail App Password)           |
| `APP_URL`      | `https://your-app.railway.app` |

> **Gmail App Password**: Google Account → Security → 2-Step Verification → App Passwords

### 5. Deploy

Railway deploys automatically on every push. First deploy takes ~2 min.

Your app is live at `https://your-app.railway.app` 🚀

---

## API Reference

| Method | Endpoint                      | Auth     | Description                    |
|--------|-------------------------------|----------|--------------------------------|
| POST   | `/api/auth/register`          | None     | Create employee account        |
| POST   | `/api/auth/login`             | None     | Login, returns JWT             |
| GET    | `/api/auth/verify/:token`     | None     | Verify email from link         |
| POST   | `/api/auth/resend-verification` | None   | Resend verification email      |
| POST   | `/api/admin/login`            | None     | Admin login, returns admin JWT |
| GET    | `/api/dashboard`              | User JWT | Get dashboard data             |
| PUT    | `/api/dashboard`              | Admin JWT| Update dashboard data          |
| GET    | `/api/users`                  | Admin JWT| List all registered users      |
| GET    | `/health`                     | None     | Health check                   |

---

## Default Admin Credentials

Set via environment variables:
- **Username**: value of `ADMIN_USER` (default: `admin`)
- **Password**: value of `ADMIN_PASS` (default: `safety2024`)

**Change these before going live.**

---

## Email Domain

Only `@tkelevator.com` addresses can register. To change this, edit line in `src/authRoutes.js`:
```js
const ALLOWED_DOMAIN = '@tkelevator.com';
```

---

## Local Development

```bash
npm install
cp .env.example .env
# Fill in .env with your local PostgreSQL connection and SMTP
npm run dev
```

Open `http://localhost:3000`
