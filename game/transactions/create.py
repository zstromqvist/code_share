import pandas as pd
import random
from datetime import datetime, timedelta

from models.transaction import transaction
from models.activation import new_activation
from activations.create import generate_random_timestamp



def create_transactions(activations_file, transactions_file):
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



def simulate_transactions(activations_file, transactions_file, date):
    """
    Simulate transactions between users or guilds.

    Parameters:
    activations_file (str): The name of the CSV file containing activation data.
    transactions_file (str): The name of the CSV file to write transaction data to.
    date (str): The date to simulate transactions for in the format YYYY-MM-DD.

    Returns:
    None.
    """
    # Load activation data
    activations = pd.read_csv(activations_file)

    # Filter activations by date
    activations = activations[activations['activation_date'] <= date]

    # Create an empty list to store transactions
    transactions = []

    # Loop until we have enough transactions
    while len(transactions) < 1000:
        # Choose two random rows from the activations data
        row1, row2 = activations.sample(n=2)

        # Create activation objects for the two rows
        activation1 = new_activation(
            activation_date=row1['activation_date'],
            id=row1['id'],
            state=row1['state'],
            county=row1['county'],
            type=row1['type']
        )
        activation2 = new_activation(
            activation_date=row2['activation_date'],
            id=row2['id'],
            state=row2['state'],
            county=row2['county'],
            type=row2['type']
        )

        # Check that the two activations are not of the same type
        if activation1.type == activation2.type:
            continue

        # Generate a random transaction date and golds amount
        transaction_date = f"{date} {generate_random_timestamp()}"
        golds = random.randint(1, 100)

        # Create a transaction object and add it to the transactions list
        transactions.append(
            transaction(
                payer_id=activation1.id,
                payer_state=activation1.state,
                payer_county=activation1.county,
                payer_type=activation1.type,
                receiver_id=activation2.id,
                receiver_state=activation2.state,
                receiver_county=activation2.county,
                receiver_type=activation2.type,
                transaction_date=transaction_date,
                golds=golds
            )
        )

    # Write transactions to CSV file
    df = pd.DataFrame([vars(t) for t in transactions])
    df.to_csv(transactions_file, index=False)
