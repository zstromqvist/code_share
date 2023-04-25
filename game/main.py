from activations.create import create_activations
from transactions.create import simulate_transactions


# Define file paths
activations_file = 'activations.csv'
transactions_file = 'transactions.csv'

# Create activation data
create_activations(n=1000, filename=activations_file)

# Simulate transactions
simulate_transactions(activations_file=activations_file, transactions_file=transactions_file)


