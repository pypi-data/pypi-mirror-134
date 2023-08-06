import sys

import py_ravif


if __name__ == "__main__":
    img_bytes = py_ravif.convert_to_avif_from_path(sys.argv[1], quality=60)
    with open(f"{sys.argv[1]}.avif", "wb") as f:
        f.write(img_bytes)
