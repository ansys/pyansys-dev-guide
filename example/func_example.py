from typing import Union


def test_function(
    param1: int = 1, param2: str = "test", param3: Union[int, float] = 1
) -> bool:
    """Function description.

    Parameters
    ----------
    param1 :
        Description of the integer parameter.
    param2 :
        Very long parameter
        description text. Lorem ipsum dolor sit amet, consectetur adipiscing
        elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
        in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
        sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
        mollit anim id est laborum.
    param3 :
        Parameter that can be either int or float using Union (typing).
    """
    return True
