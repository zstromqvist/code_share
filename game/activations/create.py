import pandas as pd
import random
from datetime import datetime, timedelta
from models.activation import new_activation


def generate_random_timestamp():
    """
    Returns a random timestamp during the day on the format hh:mm:ss
    """
    hour = str(random.randint(0, 23)).zfill(2)
    minute = str(random.randint(0, 59)).zfill(2)
    second = str(random.randint(0, 59)).zfill(2)
    return f"{hour}:{minute}:{second}"


def create_activations(n, write_to_csv=False, file_name=None):
    activations = []
    for i in range(n):
        # Generate random activation date within the last year
        activation_date = datetime.now() - timedelta(days=random.randint(0, 365))
        # Generate random activation ID
        id = ''.join(random.choices('0123456789', k=6))
        # Generate random state and county
        state = random.choice(['CA', 'TX', 'FL', 'NY', 'IL'])
        county = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
        # Create new_activation object
        activation = new_activation(activation_date, id, state, county)
        # Add activation to the list
        activations.append(activation)

    # Create a Pandas DataFrame from the activations list
    activations_df = pd.DataFrame([vars(a) for a in activations])
    
    # Write DataFrame to CSV if specified
    if write_to_csv and file_name:
        activations_df.to_csv(file_name, index=False)
    
    return activations_df



