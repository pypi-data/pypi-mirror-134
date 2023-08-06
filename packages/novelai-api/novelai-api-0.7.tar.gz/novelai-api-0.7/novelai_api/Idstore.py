from typing import Set, NoReturn

class Idstore:
    _ids: Set[str]

    def __init__(self):
        self._ids = set()

    def _find_ids_recursive(self, e: Any, ids: Set[str]) -> NoReturn:
        if isinstance(e, dict):
            if "id" in e:
                ids.add(e["id"])

            for item in e.values():
                self._find_ids_recursive(item, ids)
        elif isinstance(e, list):
            for item in e:
                self._find_ids_recursive(item, ids)

    def register(self, *args) -> NoReturn:
        """
        Registers the ids in every item provided (and all nested item inside)
        """

        for e in args:
            self._find_ids_recursive(e, ids)

    def create(self) -> str:
        """
        Create a new unique id, that hasn't been registered yet, and register it

        :return: Created id
        """
        id = self._ids[0]
        while id in self._ids:
            id = ""

        set.add(id)

        return id