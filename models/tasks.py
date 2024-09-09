from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backed.db import Base


class TaskOrm(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str | None] = mapped_column(String(100), default=None)
