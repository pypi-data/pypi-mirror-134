
from pylem import MorphanHolder, MorphLanguage

holder = MorphanHolder(MorphLanguage.Russian)
answer = holder.synthesize("мама", "N fem,sg,gen")
print(answer)
