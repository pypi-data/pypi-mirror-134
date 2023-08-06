# py_ravif

Python bindings for [`ravif`](https://github.com/kornelski/cavif-rs/tree/main/ravif) using [pyO3/maturin](https://github.com/pyO3/maturin).

## Install

```
pip install py-ravif
```

## Usage

```python
import py_ravif

# convert png or jpeg file
# give path to file
avif_bytes = py_ravif.convert_to_avif_from_path(some_path, quality=60)
# or give bytes of image
avif_bytes = py_ravif.convert_to_avif_from_bytes(img_bytes, quality=60)

```