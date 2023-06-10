from datetime import date


class Observation:
    def __init__(self, celestial_object=None, observation_date=None, notes=None, images=None):
        self._celestial_object = celestial_object
        self._observation_date = observation_date
        self._notes = notes
        self._images = images if images is not None else []

    @staticmethod
    def _is_valid_celestial_object(celestial_object: str) -> bool:
        if not len(celestial_object) > 1:
            return False

        if not celestial_object[0].isupper():
            return False

        return True

    @property
    def celestial_object(self):
        return self._celestial_object

    @celestial_object.setter
    def celestial_object(self, value: str):
        if not self._is_valid_celestial_object(value):
            raise ValueError("Celestial Object name must starts with an Uppercase letter and has to be more than 1 "
                             "character")

        self._celestial_object = value

    @property
    def observation_date(self):
        return self._observation_date

    @observation_date.setter
    def observation_date(self, value: date ):
        pass

    @property
    def notes(self):
        return self._notes

    @property
    def images(self):
        return self._images
