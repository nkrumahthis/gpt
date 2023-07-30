f = open("./kjv.txt", "r")
text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)

# create a mapping from characters to integers
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }

encode = lambda s: [stoi[c] for c in s] # encode: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decode: take a list of integers, output a string

print(encode("hello world"))
print(decode(encode("hello world")))
