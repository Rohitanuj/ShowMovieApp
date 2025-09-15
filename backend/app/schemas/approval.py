from pydantic_settings import BaseSettings
from typing import Optional

class ApprovalIn(BaseModel):
    remarks: Optional[str] = None
