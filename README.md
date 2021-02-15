# Description
Cryptotools is a simple program for centralize functions as encoding, hashing, and encryption.

# Usage
```
$ cryptotools -h

optional arguments:
  -h, --help       show this help message and exit
  --text TEXT      Text for Encode/Hash/Encrypt
  --file FILE      File for Encode/Hash/Encrypt
  --output OUTPUT  File output

Encoding:
  --b16            Encode with base 16
  --b32            Encode with base 32
  --b64            Encode with base 64

Hashing:
  --sha1           Use sha1 hash algorithmn
  --sha256         Use sha256 hash algorithmn
  --sha512         Use sha512 hash algorithmn
  --md5            Use md5 hash algorithmn
  --test           Test hashing

Encryption:
  --rot13          Encryption Caesar
  --xor            Encryption xor
  --key KEY        Key for encryption

Other:
  --clip           Copy to clipboard
  --upper          View the result with uppercase
  --view           View result
  --verbose        Mode verbose
  --debug          Mode debug
```

# Examples
## Text
```bash
$ cryptotools --text "Hello friend" --sha256 --view
ad7c4d7f20d11015260cd4609df255c99ebef944f59110167f2ff62a2c750072
```
## File
```bash
$ echo "Hello, I'm Zami3l." > file.txt
$ cryptotools.py --file file.txt --b64 --output file_checksum.txt
$ cat file_checksum.txt
SGVsbG8sIEknbSBaYW1pM2wuCg==
```

# Author
Zami3l

# License
Check LICENSE.
