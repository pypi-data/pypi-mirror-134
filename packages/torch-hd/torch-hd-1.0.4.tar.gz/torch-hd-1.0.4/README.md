# Torch-HD lives here

Torch-HD is a library that provides optimized implementations of
various Hyperdimensional Computing functions using both GPUs and CPUs.
The package also provides HD based ML functions for classification tasks.

[Get started now](#getting-started). [View it on GitHub](https://github.com/rishikanthc/torch-hd)

---

## Getting started

### Installation 

Installation is straightforward. Simply use pip to install the pacakge.
```bash
pip3 install torch-hd
```
Requires python 3.6+ and PyTorch 1.8.2 or later.

To compile it locally clone this repo and run
```bash
python setup.py install
```

### Quick start: Encode and decode a vector using ID-Level encoding

```python
from torch_hd import hdlayers as hd

codec = hd.IDLevelCodec(dim_in = 5, D = 10000, qbins = 8, max_val = 8, min_val = 0)
testdata = torch.tensor([0, 4, 1, 3, 0]).type(torch.float)
out = codec(testdata)

print(out)
print(testdata)
```

Output
```
tensor([[0., 4., 1., 3., 0.]])
tensor([[0., 4., 1., 3., 0.]])
```

#### Checkout the Examples section for a classification example

### Functionalities available

Currently Torch-HD supports 3 different encoding methodologies namely
- Random Projection Encoding
- ID-Level Encoding
- Selective Kanerva Coding
- Pact quantization


Apart from encoding functionalities, the library also provides a HD classifier which
can be used for training and inference on classification tasks

### Coming soon
- [] Implement fractional-binding
- [] Utility functions for training and validation
- Different VSA architectures
	- [] Multiply-Add-Permute (MAP) - real, binary and integer vector spaces
	- [] Holographic Reduced Representations (HRR)
	- [] HRR in Frequency domain (FHRR)
- Functional implementations of
	- [] binding
	- [] unbinding
	- [] bundling

### Contributing

Contributions to help improve the implementation are welcome. Please create a pull request on the repo or report issues.
