from typing import List, Dict, Any, Tuple

from common.types import DjangoModelType


def model_update(
    *,
    instance: DjangoModelType,
    fields: List[str],
    data: Dict[str, Any],
) -> Tuple[DjangoModelType, bool]:
    has_updated = False

    for field in fields:
        if field not in data:
            continue

        if getattr(instance, field) != data[field]:
            has_updated = True
            setattr(instance, field, data[field])

    if has_updated:
        instance.full_clean()
        instance.save(update_fields=fields)

    return instance, has_updated


def is_string_blank(s: str) -> bool:
    return not (s and s.strip())
