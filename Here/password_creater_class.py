from random import choices
from string import ascii_letters, punctuation


class Password:
    """
    this class make a random password in low , mid and high level
    ( low -> 8 , mid -> 12, high -> 16 )
    --> type strength: str, optional
    --> type length: int, optional
    """
    Characters = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }
    
    Default_length = {
        "low": 8,
        "mid": 12,
        "high": 16
    }
    
    def show_inputs(inp):
        """
        this method show the inputs that used for the password
        such as number , letter and etc ...
        format : dict
        """
        return inp.Characters
    
    def __init__(self , strength="mid", length = None):
        """
        Constructor method
        """
        self.st = strength
        self.le = length
        self._creater()
        
    def _creater(self):
        """generate the password with data """
        char = self.Characters["letters"].copy()
        length = self.le or self.Default_length.get(self.st)

        if self.st == "high":
            char += self.Characters["numbers"] + self.Characters["punctuation"]
        else:
            char += self.Characters["numbers"]

        self.password = "".join(list(map(str, choices(char, k=length))))


if __name__ == "__main__" :
    p_low = Password(strength="low")
    print("low password:------> " + p_low.password)

    p_mid = Password(strength="mid", length=20)
    print("Mid password:------> " + p_mid.password)

    p_high = Password(strength="high", length=40)
    print("High password:------> " + p_high.password)

    p_default = Password()
    print("Default password: " + p_default.password)
