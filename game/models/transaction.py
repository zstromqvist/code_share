class transaction:
    def __init__(self, payer_id, payer_state, payer_type, receiver_id, receiver_state, receiver_type, transaction_date, golds):
        self.payer_id = payer_id
        self.payer_state = payer_state
        self.payer_type = payer_type
        self.receiver_id = receiver_id
        self.receiver_state = receiver_state
        self.receiver_type = receiver_type
        self.transaction_date = transaction_date
        self.golds = golds