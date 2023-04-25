from activations import create_activations
from transactions import create_transactions

# Define file paths
activations_file = 'activations.csv'
transactions_file = 'transactions.csv'

# Create activation data
create_activations(n=1000, filename=activations_file)

# Simulate transactions
create_transactions(activations_file=activations_file, transactions_file=transactions_file)


