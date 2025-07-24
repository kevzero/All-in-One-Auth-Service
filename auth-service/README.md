# All-in-One Auth Service

## 📌 Overview
This project provides a **complete authentication solution** that can be integrated into any application. It includes JWT authentication, refresh tokens, OAuth2 login (Google, GitHub), an Admin Panel UI, and Dockerized deployment for easy setup.

### ✅ Key Features
- **FastAPI Backend**
  - JWT Authentication (Access + Refresh Tokens)
  - OAuth2 (Google, GitHub)
  - Secure password hashing (bcrypt)
- **Frontend (React)**
  - Login and Register pages
  - Admin Panel for user management
- **Database**: PostgreSQL
- **Deployment**: Docker Compose for full stack
- **.env configuration**: Ready for API keys and secrets

---

## ⚙️ Requirements
- **Docker & Docker Compose**
- **Python 3.10+** (for the generator script)
- **Node.js 18+** (if you run the frontend without Docker)
- **OAuth credentials** for Google and GitHub

---

## 🚀 Quick Start

### 1️⃣ Generate the Project
```bash
python generate_auth_service.py
```
This will create the `auth-service/` directory with all required files.

### 2️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```env
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
DATABASE_URL=postgresql://postgres:postgres@db:5432/auth_db
JWT_SECRET=your_jwt_secret
```

### 3️⃣ Start with Docker
```bash
cd auth-service
docker-compose up --build
```

- **Backend** → http://localhost:8000
- **Frontend** → http://localhost:3000

---

## 🛠 API Endpoints
- `POST /auth/login` → Login with username/password, returns JWT tokens
- `GET /auth/oauth/google` → Start Google OAuth flow
- `GET /auth/oauth/github` → Start GitHub OAuth flow
- `GET /admin/users` → Fetch users (Admin only)

---

## 🖥 Frontend Features
- **Login Page** → Authenticate via username/password or social login (Google/GitHub)
- **Register Page** → Placeholder for user registration
- **Admin Panel** → View users (expandable for user management)

---

## 📦 Project Structure
```
auth-service/
├── backend/      # FastAPI backend
├── frontend/     # React frontend
├── docker-compose.yml
├── .env.example
├── README.md
└── LICENSE
```

---

## 🔮 Future Improvements
- Full registration flow
- Role-based access control in Admin Panel
- Integration with local authentication providers
- Advanced logging and audit trails

---

## 📜 License
MIT
