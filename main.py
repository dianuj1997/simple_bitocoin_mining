from hashlib import sha256
import time

def sha256er(stringy):
    return sha256(stringy.encode("ascii")).hexdigest()

def mine(block_num,previous_hash,trans_num,prefix_zeros,nonce_max):
    prefix_str='0'*prefix_zeros
    for nonce in range(nonce_max):
        text=str(block_num)+trans_num+previous_hash +str(nonce)
        new_hash=sha256er(text)
        if new_hash.startswith(prefix_str):
            print("K!! Found it"); 
            return new_hash
        
    raise BaseException("Couldnot found shit after running {nonce_max} times")
    
    
if __name__=='__main__':
    transactions='''
    Monkey->Poop->20,
    Poopzilla->Pooparella->45
    '''
    
    difficulty=4
    nonce_max=100000000
    starty=time.time()
    new_hash=mine(5,'00',transactions,difficulty,nonce_max)
    endu=time.time()
    toty=str(endu-starty)
    print("It took this much time: {toty} secs")
    
    print("Resultant:  "+new_hash)