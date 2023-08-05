## Transcription Factor binding predictions with Attention and Transformers

A repository with exploration into using transformers to predict DNA ↔ transcription factor binding. If you are a researcher interested in this problem, please join the <a href="https://discord.gg/s7WyNU24aM">discord server</a> for discussions.

## Install

Run the following at the project root to download dependencies

```bash
$ python setup.py install --user
```

## Usage

```python
import torch
from tf_bind_transformer import AdapterModel

# instantiate enformer or load pretrained

from enformer_pytorch import Enformer
enformer = Enformer(
    dim = 1536,
    depth = 2,
    target_length = 256
)

# instantiate model wrapper that takes in enformer

model = AdapterModel(
    enformer = enformer,
    aa_embed_dim = 512,
    contextual_embed_dim = 256
).cuda()

# mock data

seq = torch.randint(0, 4, (1, 196_608 // 2)).cuda() # for ACGT

aa_embed = torch.randn(1, 1024, 512).cuda()
aa_mask = torch.ones(1, 1024).bool().cuda()

contextual_embed = torch.randn(1, 256).cuda() # contextual embeddings, including cell type, species, experimental parameter embeddings

target = torch.randn(1, 256).cuda()

# train

loss = model(
    seq,
    aa_embed = aa_embed,
    aa_mask = aa_mask,
    contextual_embed = contextual_embed,
    target = target
)

loss.backward()

# after a lot of training

corr_coef = model(
    seq,
    aa_embed = aa_embed,
    aa_mask = aa_mask,
    contextual_embed = contextual_embed,
    target = target,
    return_corr_coef = True
)
```

## Using ESM for fetching of transcription factor protein embeddings

```python
import torch
from enformer_pytorch import Enformer
from tf_bind_transformer import AdapterModel

enformer = Enformer(
    dim = 1536,
    depth = 2,
    target_length = 256
)

model = AdapterModel(
    enformer = enformer,
    use_esm_embeds = True,                            # set this to True
    contextual_embed_dim = 256
).cuda()

# mock data

seq = torch.randint(0, 4, (1, 196_608 // 2)).cuda()
tf_aa = torch.randint(0, 21, (1, 4)).cuda()           # transcription factor amino acid sequence, from 0 to 20

contextual_embed = torch.randn(1, 256).cuda()
target = torch.randn(1, 256).cuda()

# train

loss = model(
    seq,
    aa = tf_aa,
    contextual_embed = contextual_embed,
    target = target
)

loss.backward()
```

## Context passed in as free text

One can also pass the context (cell type, experimental parameters) directly as free text, which will be encoded by a text transformer trained on pubmed abstracts.

```python
import torch
from tf_bind_transformer import AdapterModel

# instantiate enformer or load pretrained

from enformer_pytorch import Enformer
enformer = Enformer(
    dim = 1536,
    depth = 2,
    target_length = 256
)

# instantiate model wrapper that takes in enformer

model = AdapterModel(
    enformer = enformer,
    use_esm_embeds = True,
    use_free_text_context = True,        # this must be set to True
    free_text_embed_method = 'mean_pool' # allow for mean pooling of embeddings, instead of using CLS token
).cuda()

# mock data

seq = torch.randint(0, 4, (2, 196_608 // 2)).cuda() # for ACGT
target = torch.randn(2, 256).cuda()

tf_aa = [
    'KVFGRCELAA',                  # single protein
    ('AMKRHGLDNY', 'YNDLGHRKMA')   # complex, representations will be concatted together
]

contextual_texts = [
    'cell type: GM12878 | dual cross-linked',
    'cell type: H1-hESC'
]

# train

loss = model(
    seq,
    target = target,
    aa = tf_aa,
    contextual_free_text = contextual_texts,
)

loss.backward()
```

## Data

Transcription factor dataset

```python
from tf_bind_transformer.data import FactorProteinDataset

ds = FactorProteinDataset(
    folder = 'path/to/tfactor/fastas'
)

# single factor

ds['ETV1'] # <seq>

# multi-complexes

ds['PAX3-FOXO1'] # (<seq1>, <seq2>)

```

## Caching

During training, protein sequences and contextual strings are cached to `~/.cache.tf.bind.transformer` directory. If you would like to make sure the caching is working, you just need to run your training script with `VERBOSE=1`

ex.

```bash
$ VERBOSE=1 python train.py
```

You can also force a cache clearance

```bash
$ CLEAR_CACHE=1 python train.py
```

## Todo

- [x] ESM and AF2 embedding fetching integrations
- [x] HF transformers integration for conditioning on free text
- [x] allow for fine-tuning layernorms of Enformer easily
- [x] add caching for external embeddings
- [x] figure out a way for external models (ESM, transformers) to be omitted from state dictionary on saving (use singletons)
- [x] take care of caching genetic sequences when enformer is frozen
- [x] offer a fully transformer variant with cross-attention with shared attention matrix and FiLM conditioning with contextual embed
- [x] also offer using pooled genetic / protein sequence concatted with context -> project -> squeeze excitation type conditioning
- [x] use checkpointing when fine-tuning enformer
- [ ] normalization of interactions between genetic and amino acid sequence
- [ ] hyperparameters for different types of normalization on fine grained interactions feature map
- [ ] support for custom transformers other than enformer

## Appreciation

This work is generously sponsored by <a href="https://github.com/jeffhsu3">Jeff Hsu</a> to be done completely open sourced.

## Citations

```bibtex
@article {Avsec2021.04.07.438649,
    author  = {Avsec, {\v Z}iga and Agarwal, Vikram and Visentin, Daniel and Ledsam, Joseph R. and Grabska-Barwinska, Agnieszka and Taylor, Kyle R. and Assael, Yannis and Jumper, John and Kohli, Pushmeet and Kelley, David R.},
    title   = {Effective gene expression prediction from sequence by integrating long-range interactions},
    elocation-id = {2021.04.07.438649},
    year    = {2021},
    doi     = {10.1101/2021.04.07.438649},
    publisher = {Cold Spring Harbor Laboratory},
    URL     = {https://www.biorxiv.org/content/early/2021/04/08/2021.04.07.438649},
    eprint  = {https://www.biorxiv.org/content/early/2021/04/08/2021.04.07.438649.full.pdf},
    journal = {bioRxiv}
}
```

```bibtex
@misc{yao2021filip,
    title   = {FILIP: Fine-grained Interactive Language-Image Pre-Training},
    author  = {Lewei Yao and Runhui Huang and Lu Hou and Guansong Lu and Minzhe Niu and Hang Xu and Xiaodan Liang and Zhenguo Li and Xin Jiang and Chunjing Xu},
    year    = {2021},
    eprint  = {2111.07783},
    archivePrefix = {arXiv},
    primaryClass = {cs.CV}
}
```

```bibtex
@misc{tay2020hypergrid,
    title   = {HyperGrid: Efficient Multi-Task Transformers with Grid-wise Decomposable Hyper Projections},
    author  = {Yi Tay and Zhe Zhao and Dara Bahri and Donald Metzler and Da-Cheng Juan},
    year    = {2020},
    eprint  = {2007.05891},
    archivePrefix = {arXiv},
    primaryClass = {cs.CL}
}
```

```bibtex
@misc{lowe2021logavgexp,
    title   = {LogAvgExp Provides a Principled and Performant Global Pooling Operator},
    author  = {Scott C. Lowe and Thomas Trappenberg and Sageev Oore},
    year    = {2021},
    eprint  = {2111.01742},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG}
}
```
