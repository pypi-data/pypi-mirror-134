from dataclasses import dataclass

TOKEN = str


@dataclass
class AuthData:
    """
        This class provides a container for user credential.

        As the scope of this project is not password security,
        no kind of protection is used to safety store passwords.
    """
    username: str
    password: str
