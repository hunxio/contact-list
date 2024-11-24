from typing import Optional


class Contact:

    def __init__(self,
                 name: str,
                 last_name: str,
                 number: str,
                 email: Optional[str] = None) -> None:
        self.name = name
        self.last_name = last_name
        self.number = number
        self.email = email
