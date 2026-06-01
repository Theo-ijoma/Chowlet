from uuid import UUID

import httpx
from sqlalchemy.orm import Session  # type: ignore[import]

from app.core.config import settings
from app.db.models.user import User, UserRole


class AuthService:
    def __init__(self):
        self.auth_url = f"{settings.SUPABASE_URL.rstrip('/')}/auth/v1"
        self.headers = {
            "apikey": settings.SUPABASE_KEY,
            "Content-Type": "application/json",
        }

    def register(
        self,
        email: str,
        password: str,
        full_name: str,
        school_id: UUID,
        phone: str | None = None,
        role: UserRole = UserRole.STUDENT,
    ):
        """Register user with Supabase Auth."""
        try:
            response = httpx.post(
                f"{self.auth_url}/signup",
                headers=self.headers,
                json={"email": str(email), "password": password},
                timeout=20,
            )
            response.raise_for_status()
            payload = response.json()
            user = payload.get("user") or payload
            session = payload.get("session") or {}

            return {
                "success": True,
                "user_id": user["id"],
                "email": user["email"],
                "access_token": session.get("access_token"),
                "full_name": full_name,
                "school_id": school_id,
                "phone": phone,
                "role": role,
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }

    def login(self, email: str, password: str):
        """Login user with Supabase Auth."""
        try:
            response = httpx.post(
                f"{self.auth_url}/token?grant_type=password",
                headers=self.headers,
                json={"email": str(email), "password": password},
                timeout=20,
            )
            response.raise_for_status()
            payload = response.json()
            user = payload["user"]

            return {
                "success": True,
                "user_id": user["id"],
                "email": user["email"],
                "access_token": payload["access_token"],
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }

    def get_supabase_user(self, access_token: str):
        """Resolve a Supabase JWT into its auth user."""
        try:
            response = httpx.get(
                f"{self.auth_url}/user",
                headers={
                    **self.headers,
                    "Authorization": f"Bearer {access_token}",
                },
                timeout=20,
            )
            response.raise_for_status()
            user = response.json()

            return {
                "success": True,
                "user_id": user["id"],
                "email": user["email"],
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }

    def save_user_to_db(
        self,
        session: Session,
        supabase_id: str,
        email: str,
        full_name: str,
        school_id: UUID,
        phone: str | None,
        role: UserRole,
    ):
        """Save user to local database after Supabase registration."""
        try:
            user = User(
                supabase_id=supabase_id,
                email=email,
                full_name=full_name,
                school_id=school_id,
                phone=phone,
                role=role,
                is_verified=False,
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except Exception:
            session.rollback()
            raise


auth_service = AuthService()
