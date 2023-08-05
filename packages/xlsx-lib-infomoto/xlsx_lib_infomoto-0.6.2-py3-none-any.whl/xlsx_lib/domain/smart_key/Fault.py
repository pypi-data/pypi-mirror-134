from typing import Optional, List

from camel_model.camel_model import CamelModel


class Fault(CamelModel):
    fault_kind: List[str] = []
    flash_pattern_image: Optional[str]
    flashs_number_by_time: Optional[str]
    parts_to_review: Optional[List[str]]
