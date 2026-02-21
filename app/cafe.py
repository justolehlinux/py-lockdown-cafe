from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError

import datetime


def check_exception_date(expiration_date: datetime.date) -> bool:

    current_date = datetime.date.today()

    return expiration_date < current_date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if visitor.get("vaccine") is None:
            raise NotVaccinatedError(
                "You must be vaccinated to enter the cafe.")

        if check_exception_date(visitor["vaccine"]["expiration_date"]):
            raise OutdatedVaccineError("Your vaccine is outdated.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(
                "You must wear a mask to enter the cafe.")

        return f"Welcome to {self.name}"
