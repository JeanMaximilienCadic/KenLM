# KenLM compiled version (fork from https://github.com/kpu/kenlm)

Language model inference code by Kenneth Heafield (kenlm at kheafield.com)

I do development in master on https://github.com/kpu/kenlm/.  Normally, it works, but I do not guarantee it will compile, give correct answers, or generate non-broken binary files.  For a more stable release, get https://kheafield.com/code/kenlm.tar.gz .

The website https://kheafield.com/code/kenlm/ has more documentation.  If you're a decoder developer, please download the latest version from there instead of copying from another decoder.

### Installation

```bash
conda install -c ninedw kenlm 
``

### Basic Usage
```python
from kenlm.kenlm import Model
from kenlm import bin

bin('lmplz') # TODO

model = Model('lm/test.arpa')
print(model.score('this is a sentence .', bos = True, eos = True))
```


