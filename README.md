# KenLM compiled version 
This is a fork from https://github.com/kpu/kenlm. Please consult this page for more informations
Language model inference code by Kenneth Heafield (kenlm at kheafield.com)

### Installation

```bash
conda install -c ninedw kenlm 
```

### Basic Usage
```python
from kenlm.kenlm import Model
from kenlm import bin

bin('lmplz') # TODO

model = Model('lm/test.arpa')
print(model.score('this is a sentence .', bos = True, eos = True))
```


