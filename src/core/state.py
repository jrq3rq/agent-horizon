from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import date

class HorizonState(BaseModel):
    """Core state for Agent Horizon - the single source of truth"""
    current_week: int = 0
    total_weeks: int = 36
    completed_weeks: List[int] = Field(default_factory=list)
    mastery: Dict[str, float] = Field(default_factory=dict)
    start_date: Optional[date] = None
    projected_end_date: Optional[date] = None
    status: str = "active"

    # Builder Program specifics
    child_age: int = 10
    difficulty_tier: str = "Builder"
    neurodivergent_adaptations: bool = True