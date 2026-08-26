# Caesar Cipher & Brute Force Cracker

A command-line tool for encrypting/decrypting text with a Caesar cipher,
plus two brute-force methods for cracking ciphertext without knowing the key.

## Features

- Encrypt/decrypt via an interactive CLI (`caesar_cipher.py`)
- Brute force by word-matching against an English dictionary (`brute_force_v1`)
- Brute force by exact match against a known plaintext (`brute_force_v2`)

## Setup

pip3 install nltk
(Mac only: if you hit an SSL certificate error on first run, execute
"Install Certificates.command" found in your Python app folder)

## Usage

python3 caesar_cipher.py # interactive encrypt/decrypt
python3 brute_force.py # runs a demo cracking example

## What I learned

- How to brute-force a small keyspace instead of relying purely on
  cleverness
- The character set here places uppercase and lowercase letters in two
  adjacent 26-character blocks, so any correct key `k` also produces a
  valid-looking result at key `k + 26` (case-swapped) — the word-matching
  cracker can't always tell these apart automatically.

## Known limitations

- Word-matching brute force assumes the plaintext has normal spacing;
  it won't detect readable text with no spaces (e.g. "hellohowareyou")
- Exact-match brute force (v2) only works if you already know the plaintext
