# vigenere breaker demo

## encrypt

to encrypt a text with the vigenere cipher, run the the script encrypt.py:

```
python3 encrypt.py -s <secret> -m <text_to_encrypt>
```

### example
```bash
python3 encrypt.py -s tumble -m "The house introduced in the introduction is Arthuer Dents house"
```

## decrypt

to decrypt a encrypted message, run the script decrypt.py:

```
python3 decrypt.py -s <secret> -m <encrypted_message>
```

### example
```bash
python3 decrypt.py -s tumble -m "MBQIZY LYUOEV HXGDPH BHFIPM GNDPOY VNUPYM LUDUSY XLPFYX LBAVDI"
```


