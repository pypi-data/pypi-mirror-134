from typing import Optional, List

from camel_model.camel_model import CamelModel

from domain.shared.text_line import TextLine


class Fault(CamelModel):
    fault_kind: List[TextLine] = []
    flash_pattern_image: Optional[str]
    flashs_number_by_time: Optional[str]
    parts_to_review: Optional[List[TextLine]]
