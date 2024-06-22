from typing import Any

from iok.state import State


class Txt(State, suffix="txt"):
    def __init__(self, data: str, **kwargs: Any):
        if not isinstance(data, str):  # type: ignore
            raise TypeError(f"Expected str, got {type(data).__name__}")
        super().__init__(data=data.encode("utf-8"), **kwargs)

    def load(self) -> str:
        return self.data.getvalue().decode("utf-8")
