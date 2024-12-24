import nltk
import re
from pprint import pprint


patterns = {
    "Pattern a": "[a-z]+",
    "Pattern b": "[A-Z][a-z]+",
    "Pattern c": "c[aeiou]{1,2}t"
}

text = "a b Ahello ccat cot cut Celt Cat aHello World H"

print("Pattern a")
matches_a = re.findall(patterns["Pattern a"], text)
pprint(matches_a)
nltk.re_show(patterns["Pattern a"], text)


print("\nPattern b")
matches_b = re.findall(patterns["Pattern b"], text)
pprint(matches_b)
nltk.re_show(patterns["Pattern b"], text)


print("\nPattern c")

matches_c = re.findall(patterns["Pattern c"], text)
pprint(matches_c)
nltk.re_show(patterns["Pattern c"], text)

