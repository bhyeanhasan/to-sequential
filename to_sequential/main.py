from typing import List, Tuple
import numpy as np
import pandas as pd


def generate_sequences(df: pd.DataFrame, window_size: int, column_names: List[str]) -> Tuple[np.ndarray, np.ndarray]:
    """
    Parameters:
    df (pd.DataFrame): The input data frame.
    window_size (int): The size of the window for the sequences.
    column_names (list): List of column names to use for generating sequences.

    Returns:
    np.ndarray: Array of sequences of shape (number_of_sequences, window_size, number_of_columns).
    np.ndarray: Array of targets of shape (number_of_sequences, number_of_columns).
    """

    for column in column_names:
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame")

    data = df[column_names].values
    sequences = []
    targets = []

    for i in range(len(data) - window_size):
        sequences.append(data[i:i + window_size])
        targets.append(data[i + window_size])

    return np.array(sequences), np.array(targets)
