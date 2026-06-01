from fastapi import APIRouter, Depends, Header, HTTPException, status  # type: ignore[import]
from sqlalchemy.orm import Session  # type: ignore[import]
from sqlalchemy.exc import IntegrityError  # type: ignore[import]

from app.api.deps import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, AuthResponse, UserResponse
from app.services.auth import auth_service
from app.db.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])


def build_user_response(user: User) -> UserResponse:
    return UserResponse.model_validate(user)


def extract_bearer_token(authorization: str | None) -> str:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header"
        )

    return token


@router.post("/register", response_model=AuthResponse)
async def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    """Register a new user"""
    auth_result = auth_service.register(
        email=request.email,
        password=request.password,
        full_name=request.full_name,
        school_id=request.school_id,
        phone=request.phone,
        role=request.role
    )

    if not auth_result["success"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=auth_result.get("error", "Registration failed")
        )

    try:
        user = auth_service.save_user_to_db(
            session=db,
            supabase_id=auth_result["user_id"],
            email=auth_result["email"],
            full_name=request.full_name,
            school_id=request.school_id,
            phone=request.phone,
            role=request.role
        )

        return AuthResponse(
            access_token=auth_result.get("access_token", ""),
            user=build_user_response(user)
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists for this school"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/login", response_model=AuthResponse)
async def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    """Login user"""
    auth_result = auth_service.login(
        email=request.email,
        password=request.password
    )

    if not auth_result["success"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return AuthResponse(
        access_token=auth_result["access_token"],
        user=build_user_response(user)
    )


@router.get("/me", response_model=UserResponse)
async def get_current_user(
    db: Session = Depends(get_db),
    authorization: str | None = Header(default=None)
):
    """Get current authenticated user from a Supabase bearer token."""
    token = extract_bearer_token(authorization)
    auth_result = auth_service.get_supabase_user(token)

    if not auth_result["success"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user = db.query(User).filter(
        User.supabase_id == auth_result["user_id"],
        User.is_active.is_(True),
    ).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return build_user_response(user)
