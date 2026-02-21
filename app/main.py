from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_wear = 0

    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except NotWearingMaskError:
            masks_to_wear += 1
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
    if masks_to_wear:
        return f"Friends should buy {masks_to_wear} masks"

    return f"Friends can go to {cafe.name}"
