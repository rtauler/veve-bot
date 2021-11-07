from PIL import Image
import imagehash, time


hash0 = imagehash.average_hash(Image.open('img/1.png'))
hash1 = imagehash.average_hash(Image.open('img/2.png'))
cutoff = 5  # maximum bits that could be different between the hashes.

start = time.time()
if hash0 - hash1 < cutoff:
    print('similar')
else:
    print('not similar')
end = time.time()

print(end - start)
