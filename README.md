# sepyrot
A little python script that encodes and decodes a text by replacing spaces with random numbers, applies rot13 to the letters and replace the second of doubled letters with a dot.

## Usages :

```
# Encode
$ ./sepyrot.py encode "Hello I am a text"
Ury.b3V8nz0n5grkg

# Decode
$ ./sepyrot.py decode "Ury.b3V8nz0n5grkg"
Hello I am a text
```

## Issues :
- Doesn't work with special characters. Doesn't crash when using Python3 but those letters stay in clear text and special characters become spaces when decoded
- Cannot encode/decode messages that include numbers, it'll replace them with spaces in decoded message
