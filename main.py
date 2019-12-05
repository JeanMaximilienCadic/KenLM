from kenlm.kenlm import Model
from kenlm import bin

bin('lmplz') # TODO

model = Model('lm/test.arpa')
print(model.score('this is a sentence .', bos = True, eos = True))
