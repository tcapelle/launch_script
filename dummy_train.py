from dataclasses import dataclass
import simple_parsing

@dataclass
class Args(simple_parsing.Serializable):
    arg1: str
    arg2: str = "arg2"
    arg3: str = "arg3"


args = simple_parsing.parse(Args)
print(f"We are inside dummy_train.py with args: {args}")