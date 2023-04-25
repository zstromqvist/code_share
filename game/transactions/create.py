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

import pandas as pd
import random
from datetime import datetime, timedelta

def simulate_transactions(activations_file, transactions_file):
    # Read activations CSV file into a Pandas DataFrame
    activations_df = pd.read_csv(activations_file)

    # Create an empty list to store transactions
    transactions = []

    # Loop until there are at least two activated users or guilds with different IDs
    while True:
        # Select two random rows from the activations DataFrame
        payer_row = activations_df.sample(n=1)
        receiver_row = activations_df.sample(n=1)

        # Check that payer and receiver IDs are different
        if payer_row['id'].values[0] != receiver_row['id'].values[0]:
            # Extract payer and receiver attributes from the DataFrame rows
            payer_id = payer_row['id'].values[0]
            payer_state = payer_row['state'].values[0]
            payer_type = payer_row['type'].values[0]
            receiver_id = receiver_row['id'].values[0]
            receiver_state = receiver_row['state'].values[0]
            receiver_type = receiver_row['type'].values[0]

            # Generate random transaction date within the last week
            transaction_date = datetime.now() - timedelta(days=random.randint(0, 7))

            # Generate random amount of golds
            golds = random.randint(1, 100)

            # Create new transaction object
            transaction_obj = transaction(payer_id, payer_state, payer_type, receiver_id, receiver_state, receiver_type, transaction_date, golds)

            # Add transaction to the list
            transactions.append(transaction_obj)

            # Create a Pandas DataFrame from the transactions list
            transactions_df = pd.DataFrame([vars(t) for t in transactions])

            # Write DataFrame to CSV file
            transactions_df.to_csv(transactions_file, index=False)
            break


