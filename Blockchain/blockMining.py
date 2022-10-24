#THIS PYTHON SCRIPT DEMONSTRATES THE WORKING OF BLOCK MINING ALGORITHM IN BLOCKCHAIN TECHNOLOGY
from hashlib import sha256
import time

def menu():
    print("1. DEFAULT MODE")
    print("2. CUSTOM MODE")
    print("3. QUIT PROGRAM")

    try:
        SELECTION=int(input("Choose a mode: "))
        if SELECTION==1:
            TRANSACTIONS="akshay->nikita -> 20 BTC nikita-> ashutosh -> 5 BTC vrunda -> akshay -> 10 BTC"
            DIFFICULTY=4
            MAX_NONCE = 1000 ** 1000
            BLOCK_NUMBER = 5
            PREVIOUS_HASH = 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
            NEW_HASH = mine(BLOCK_NUMBER, TRANSACTIONS, PREVIOUS_HASH, DIFFICULTY, MAX_NONCE)
            print("The hash of the current block is: ",NEW_HASH)

        elif SELECTION==2:
            #take user inputs for custom mode 
            print("Transaction details are strings in plain english like 'Akshay sends John 98BTC, John sends karina 43BTC' etc")
            TRANSACTIONS= input("Enter transactions: ")
            print("Difficulty is the amount of prefix zeros required for the block to be accepted ")
            print("Due to computational limitations, low value of difficulty is reccomended for successful mining")
            print("Reccomended range for difficulty is 0 to 6")
            DIFFICULTY=int(input("Enter difficulty(prefix zeros): "))
            print("Max nounce number of values of nonce what will be tested")
            print("Select a sufficiently high value of max nounce for successfull mining. For example 999999999999999999999999999")
            MAX_NONCE = int(input("Enter max nounce: "))
            print("Block number is the number of the block that you want to mine")
            BLOCK_NUMBER = int(input("Enter block number: "))
            print("Previous hash is the hash of the block that has been mined in the blockchain just before the block you want to mine ")
            print("Preferably enter a 64 character long hexadecimal value here for accurate representation of bitcoin mining ")
            print("If not possible,enter any value")
            PREVIOUS_HASH = input("Enter previous hash: ")
            NEW_HASH = mine(BLOCK_NUMBER, TRANSACTIONS, PREVIOUS_HASH, DIFFICULTY, MAX_NONCE)
            print("The hash of the current block is: ",NEW_HASH)
    
        elif SELECTION==3:
            pass   
        else:
            print("INVALID CHOICE. ENTER 1-3")
            menu()
                    
    except ValueError:
        print("INVALID CHOICE. ENTER 1-3")
        menu()
 

def SHA256(TEXT):
    return sha256(TEXT.encode("ascii")).hexdigest()

def mine(BLOCK_NUMBER, TRANSACTIONS, PREVIOUS_HASH, DIFFICULTY,MAX_NONCE):
    mineSTART=time.time()
    print("MINING HAS STARTED")
    for NONCE in range(MAX_NONCE):
        TEXT=str(BLOCK_NUMBER)+ TRANSACTIONS + PREVIOUS_HASH + str(NONCE)
        NEW_HASH=SHA256(TEXT)
        if NEW_HASH.startswith('0'* DIFFICULTY):
            print(f"SUCCESSFULLY MINED CRYPTOCURRENCY WITH NONCE VALUE: {NONCE}")
            TOTAL_TIME=(time.time()-mineSTART)
            print(f"MINING COMPLETE! MINING TOOK: {TOTAL_TIME} SECONDS")
            return NEW_HASH
    raise BaseException(f"COULD NOT FIND CORRECT HASH AFTER TRYING {MAX_NONCE} TIMES")

if __name__=='__main__':
    menu()
