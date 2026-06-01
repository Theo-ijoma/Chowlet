from uuid import UUID

from pydantic import BaseModel, EmailStr, Field  # type: ignore[import]

from app.db.models.user import UserRole


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str = Field(min_length=2, max_length=255)
    phone: str | None = None
    school_id: UUID
    role: UserRole = UserRole.STUDENT


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: str
    phone: str | None
    role: UserRole
    school_id: UUID
    is_verified: bool

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    access_token: str
    user: UserResponse
