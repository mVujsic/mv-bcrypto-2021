import hashlib
import random
import time
import string

LIMIT_OF_NONCE = 100000000
hardness = 0;
blockNum = random.randrange(200)


def time_converter(sec):
#TODO
	min = sec // 60
	hours = min //60
	print("Proteklo vreme {0}:{1}:{2}".format(int(hours),int(min),int(sec)))

def random_char(y):
	return_string = ''
	random_chars = [random.choice(string.ascii_letters) for x in range(y)]
	for x in random_chars:
		return_string += x
	return return_string

def miner(block_number,transaction,prev_hash):
	start_time = time.time()
	for nonce in range(LIMIT_OF_NONCE):
		base_tex = str(block_number) + transaction + prev_hash + str(nonce)
		hash_try = hashlib.sha256(base_tex.encode()).hexdigest()
		#print(f'Nonce:{nonce} hash: {hash_try}')
		
		if hash_try.startswith('0' * hardness):
			elapsed_time = time.time() - start_time
			print(f'Pronadjen hash!\nNonce:{nonce}\nHash:{hash_try}\nVreme:{round(elapsed_time,2)} sec.')
			print('============================')
			#time_converter(elapsed_time)
			return hash_try

	print("Dostignut limit za Nonce!Izlaz!")
	return -1

transation_hash = random_char(10)
prev_transaction_hash = random_char(10)

while True:
	try:
		hardness = int(input("Unesi zeljenu tezinu[1-]:"))
		if hardness == 0 or hardness < 0:
			raise ValueError
		
		dump = miner(blockNum,transation_hash, prev_transaction_hash)
		prev_transaction_hash = transation_hash

		if dump == -1:
			break

		transation_hash = random_char(10)

	except ValueError:
		print("Pogresan unos!Pokusaj ponovo!")
	
	except KeyboardInterrupt:
		print("")
		break


print("Izlaz....")

exit(1)

