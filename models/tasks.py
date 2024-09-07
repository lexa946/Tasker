from sqlalchemy.orm import Mapped, mapped_column

from backed.db import Base


class TaskOrm(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[str | None] = mapped_column(default=None)


    def to_dict(self):
        return self.__dict__
        # {
        #     for attr in
        # }