# sepyrot
A little python script that encodes and decodes a text by replacing spaces with random numbers, applies rot13 to the letters and replace the second of doubled letters with a "+".

## Usages :

```
# Encode
$ ./sepyrot.py encode "Hello I am a message"
Ury+b2V4nz8n9zrf+ntr

# Decode
$ ./sepyrot.py decode "Ury+b2V4nz8n9zrf+ntr"
Hello I am a message
```

## Issues :
- Special characters make the script crash with Python < 3. With Python 3 they are just not rot13 encoded and stay clear in the encoded message
- Cannot encode/decode messages that include numbers, it'll replace them with spaces in decoded message
