class Repository():

    def __init__(self, id: int, name: str, stars: int) -> None:
        self._id = id
        self._name = name
        self._stars = stars

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def stars(self) -> int:
        return self._stars

    def __str__(self) -> str:
        return f'id: {self._id} name: {self._name} stars: {self._stars}'
