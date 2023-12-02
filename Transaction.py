import uuid
import time
import copy


class Transaction():

    def __init__(self, senderPublicKey, receiverPublicKey, amount, type):
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = type
        self.id = (uuid.uuid1()).hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__

    # assign a signature to the transaction
    def sign(self, signature):
        self.signature = signature

    # return a copy of the json representation of the transaction with the signature set to an empty string
    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    # checks if two transactions are equal based on their unique identifier
    def equals(self, transaction):
        if self.id == transaction.id:
            return True
        else:
            return False
