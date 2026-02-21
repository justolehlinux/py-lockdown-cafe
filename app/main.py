from app.cafe import Cafe
from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError

import datetime


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
    if masks_to_wear > 0:
        return f"Friends should buy {masks_to_wear} masks"
    else:
        return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    cafe = Cafe("Cafe Python")

    visitor = {
        "name": "John Doe",
        "vaccine": {
            "expiration_date": datetime.date(2023, 1, 1)
        },
        "wearing_a_mask": True
    }

    try:
        print(cafe.visit_cafe(visitor))
    except NotVaccinatedError as e:
        print(e)
    except OutdatedVaccineError as e:
        print(e)
    except NotWearingMaskError as e:
        print(e)
