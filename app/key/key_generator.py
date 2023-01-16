# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       IPToken.key.key_generator.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import string
import secrets
from typing import Union
# |--------------------------------------------------------------------------------------------------------------------|

class KEY(object):
    def __init__(self, lowercase: bool = False,
                       uppercase: bool = False,
                       digits: bool = True,
                       punctuation: bool = False,
                       user_mode: Union[str, bool] = False) -> None:
        """
            Generates a random key with the given specifications.

            The inialitization instance of the class will load into memory the data that will be used in the key.
        Args:
            lowercase (bool, optional): lowercase in key. Defaults to False.
            uppercase (bool, optional): uppercase in key. Defaults to False.
            digits (bool, optional): digits in key. Defaults to True.
            punctuation (bool, optional): punctuation in key. Defaults to False.
            user_mode (Union[str, boll], optional): adds the characters of the given string. Defaults to False.
        """
        
        # | Config dictionary |----------------------------------------------------------------------------------------|
        self.config: dict[str, bool] = {
            "lowercase": lowercase,
            "uppercase": uppercase,
            "digits": digits,
            "punctuation": punctuation
        }
        # |------------------------------------------------------------------------------------------------------------|

        # | Assemble ascii dictionary |--------------------------------------------------------------------------------|
        self.ascii_data: dict[str] = {
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "punctuation": string.punctuation
        }
        # |------------------------------------------------------------------------------------------------------------|

        # | user_mode instance |---------------------------------------------------------------------------------------|
        if isinstance(user_mode, str):
            self.ascii_data["user_mode"]: str = user_mode
            self.config["user_mode"]: bool = True
        else:
            self.config["user_mode"]: bool = False
        # |------------------------------------------------------------------------------------------------------------|

    def generate(self, key_len: int) -> str:
        """
        Generate the secure key.
        Args:
            key_len (int): key size.
        Returns:
            str: Secure key.
        """
        alphabet: str = ''
        string_mode_list: list[str] = [str_mode for str_mode in self.config.keys()]
        try:
            # | Generate secure key |----------------------------------------------------------------------------------|
            for mode in string_mode_list:
                if self.config[mode] == True:
                    alphabet: str = alphabet + self.ascii_data[mode]
            return ''.join(secrets.choice(alphabet) for i in range(key_len))
            # |--------------------------------------------------------------------------------------------------------|
        except IndexError as exc:
            raise RuntimeError("At least one of the parameters of the KEY class must be True") from exc