from Crypto.PublicKey import RSA
from Transaction import Transaction
from Block import Block
from BlockchainUtils import BlockchainUtils
from Crypto.Signature import PKCS1_v1_5


class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    # import a key pair from a file
    def fromKey(self, file):
        key = ''
        with open(file, 'r') as keyfile:
            key = RSA.importKey(keyfile.read())
        self.keyPair = key

    # create a digital signature for a given data
    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

    # verify the validity of a digital signature for a given data using a public key
    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        signatureValid = signatureSchemeObject.verify(dataHash, signature)
        return signatureValid

    # export the public key in PEM format, decode it
    def publicKeyString(self):
        publicKeyString = self.keyPair.publickey().exportKey(
            'PEM').decode('utf-8')
        return publicKeyString
    
    # create a new transaction with the wallet as the sender
    def createTransaction(self, receiver, amount, type):
        transaction = Transaction(
            self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction

    # create a new block with the given transactions, last hash, and block count
    def createBlock(self, transactions, lastHash, blockCount):
        block = Block(transactions, lastHash,
                      self.publicKeyString(), blockCount)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
