# sepyrot
A little python script that encodes and decodes a text by replacing spaces with random numbers, applies rot13 to the letters and replace the second of doubled letters with a "+".

## Usages :

### Works with simple text...

```
# Encode a short message
$ ./sepyrot.py --encode "Hello I am a message"
Ury+b2V4nz8n9zrf+ntr

# Decode a short message
$ ./sepyrot.py --decode "Ury+b2V4nz8n9zrf+ntr"
Hello I am a message
```

### ...And with files as well

```
# Encode a text file (which works with multiple lines indeed)
$ ./sepyrot.py --encode "$(cat textfile.txt)" > encoded_textfile.txt

# Decode an encoded text file
$ ./sepyrot.py --decode "$(cat encoded_textfile.txt)" > decoded_textfile.txt
```

### Tips

- You can also use `-e` and `-d` instead of `--encode` and `--decode`

## Issues :
- Special characters make the script crash with Python < 3. With Python 3 they are just not rot13 encoded and stay clear in the encoded message
- Cannot encode/decode messages that include numbers, it'll replace them with spaces in decoded message
