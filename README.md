# Description
Cryptotools is a simple program for centralize functions as encoding, hashing, and encryption.

# Usage
```
$ cryptotools -h

optional arguments:
  -h, --help                        show this help message and exit
  -i INPUT, --input INPUT           Text for Encode/Hash/Encrypt
  -f FILE, --file FILE              File for Encode/Hash/Encrypt
  -p, --pwd                         Text without echo for Encode/Hash/Encrypt
  -o OUTPUT, --output OUTPUT        File output
                        

Encoding:
  -b16, --base16                    Encode with base 16
  -b32, --base32                    Encode with base 32
  -b64, --base64                    Encode with base 64
  -hex, --hex                       Encode hex

Hashing:
  -sha1, --sha1                     Use sha1 hash algorithmn
  -sha256, --sha256                 Use sha256 hash algorithmn
  -sha512, --sha512                 Use sha512 hash algorithmn
  -md5, --md5                       Use md5 hash algorithmn
  -custom, --custom                 Test hashing

Encryption:
  -rot13, --rot13                   Encryption ROT13
  -caesar TYPE, --caesar TYPE       Encryption Caesar (Select letter or ascii)
  -vigenere TYPE, --vigenere TYPE   Encryption Vigenere (Select letter or ascii)
  -xor, --xor                       Encryption xor
  -rc4, --rc4                       Encryption RC4

Encryption - Sub args:
  -k KEY, --key KEY                 Key for encryption
  -shift NUMBER, --shift NUMBER     Number for shift
  -repeat NUMBER, --repeat NUMBER   Number for repetition shift
                        

Other:
  -t, --test                        Run unit testing
  -c, --clip                        Copy to clipboard
  -up, --upper                      View the result with uppercase
  -v, --view                        View result
  -vv, --verbose                    Mode verbose
  -d, --debug                       Mode debug
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
