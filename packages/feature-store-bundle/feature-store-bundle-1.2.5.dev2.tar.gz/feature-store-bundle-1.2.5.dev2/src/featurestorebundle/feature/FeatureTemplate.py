from typing import Optional
from dataclasses import dataclass


@dataclass(repr=True, frozen=True)
class FeatureTemplate:
    name_template: str
    description_template: str
    category: Optional[str] = None
