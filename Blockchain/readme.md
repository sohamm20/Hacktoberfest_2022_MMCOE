# block_mining
BLOCKCHAIN: A blockchain is a chain of blocks.
Each block is related by a special value called Hash. A hash is the digital signature of any data. The concept of blockchain is often related to cryptocurrencies 
like bitcoin and etherum; but in itself the concept of blockchain has various other applications.
Blockchain technology can be used to create a permanent, public, transparent ledger system for compiling data on sales, tracking digital use 
and payments to content creators, such as wireless users or musicians. 

Other applications of blockchain include:
  Secure sharing of medical data
  NFT marketplaces
  Music royalties tracking
  Cross-border payments
  Real-time IoT operating systems
  Personal identity security
  Anti-money laundering tracking system
  Supply chain and logistics monitoring
  Voting mechanism
  Advertising insights
  Original content creation
  Cryptocurrency exchange
  Real estate processing platform
   
In our example, we will be focusing on bitcoin mining.

WORKING OF BLOCKCHAIN:
  Blockchain is a decentralized system that makes it possible to transfer value without trusting a central authority or the other members.
  Blockchain works when each member trusts whichever ledger that has the most computational work put into it.
  The job of bitcoin miners is to add new blocks to the blockchain. Without miners, no new blocks can be added and hence no new transactions 
  will be logged.
  Thus, in theory, attackers owning 51% of the mining resources can keep generating fradulent blocks before everyone else and brodcasting 
  them for everyone to believe.
  

Each block contains:
  1. Block Number:It is the basic indexing of blocks. These are mostly taken in ascending order as base 10 integers like (1,2,3,4...etc).
  The first block of a blockchain is usually called the Genesis Block. It is the basis on which additional blocks are added to form a chain of blocks.
  The example taken here is the Bitcoin blockchain of the genesis block:
  Number of transactions: 1
  Transaction fee: $0.00
  Block height: 0
  Timestamp: 03/02/2009, 18:15
  Nonce: 208393
  Block difficulty: 1
  2. Previous Hash(The hash of the block preceding the current block in the blockchain)
  3. Transaction Details
  4. Nonce: Nonce or “number used only once” is the number that all miners around the globe are hoping to discover in order to validate a block 
  and receive its mining bonus.Changing the nonce causes a change in the hash. Nonce only applies to blockchains that have a Proof of Work algorithm
  as consensus algorithm.
  
Block difficulty: It is a number that regulates how long it can take for a miner to add a new block to the blockchain.
The difficulty is always fixed at a defined time interval, adjusted once every 2 weeks so that a block can be built at a fixed time interval. 
So there is a fixed time interval between constructing 2 blocks, which is approximately 10 minutes (in Bitcoin), set by the difficulty of the network.
In technical terms, difficulty is a value that is used to demonstrate, how hard is it to find a hash that will be lower than the target 
characterized by the system.

In bitcoin framework, the difficulty is adjusted by setting the number of prefix zeros required in the new hash.



SHA256() is a cryptographic hashing function. It is irreversible which means that given the output of this function, there is no other way to find its input
other than just guessing aka TRIAL AND ERROR. This function is used in all of modern security due to this fact. It also showcases the Butterfly Effect which 
means that any small change in the input of this function causes a radical change in the output.

This fuction takes a string of any arbitary length but always outputs a hash of 256 bits. When this 256 bit binary number is converted into hexadecimal,
we get 64 character long hash.

In bitcoin, the input for which we get a hexadecimal hash starting with some number of zeros (this number of prefix zeros is decided by bitcoin depending
on the difficulty to mine each block) is our nonce value. Once we find a hash starting with our specified number of prefix zeros, we say that the block has
been successfully mined and can be added to the blockchain.

note: 1. We convert the entire block that we are going to mine into a string and give it as an input to our cryptoghraphic hashing function SHA256().
      2. We also add our mining reward to the transaction details of the block before converting it into a string and mining it.
      3. If our block is successfully added to the blockchain, then the transactions will be executed and we will get our reward.
