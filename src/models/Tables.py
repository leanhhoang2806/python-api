from sqlalchemy import \
    Column, String, Table, \
    TIMESTAMP, text, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Tables:
    def __init__(self) -> None:
        self.Items = Table(
            "items",
            metadata,
            Column("id", UUID(as_uuid=True), primary_key=True),
            Column(
                "created_at",
                TIMESTAMP(timezone=True),
                server_default=text("current_timestamp")),
            Column(
                "updated_at",
                TIMESTAMP(timezone=True),
                server_default=text("current_timestamp")),
            Column("name", String, nullable=False),
        )


tables = Tables()


class Items(Base):
    __table__ = tables.Items
