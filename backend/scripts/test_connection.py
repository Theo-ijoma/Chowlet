from pathlib import Path
import sys
from sqlalchemy import text  # type: ignore[import]

# Ensure project root (two levels up: backend) is on sys.path so `import app` works
# sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.db.session import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.scalar())