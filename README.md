## To Sequential

`to_sequential` is a simple utility function to generate sequential data from a Pandas DataFrame, making it suitable for
preparing data for sequential models.

### Usage

Here's a basic example of how to use the generate_sequences function:

```python
import pandas as pd
from to_sequential import generate_sequences

df = pd.read_csv('Example.csv')

# Generate sequences
sequences, targets = generate_sequences(df, window_size=10, column_names=['feature1', 'feature2'])

print("Sequences:\n", sequences)
print("Targets:\n", targets)
```

### Function Documentation
`generate_sequences`
Generate sequential data for sequential model.

#### Parameters
* df (pd.DataFrame): The input data frame.
* window_size (int): The size of the window for the sequences.
* column_names (List[str]): List of column names to use for generating sequences.

#### Returns
* np.ndarray: Array of sequences of shape (number_of_sequences, window_size, number_of_columns).
* np.ndarray: Array of targets of shape (number_of_sequences, number_of_columns).

#### Raises
* ValueError: If any column in column_names is not found in the DataFrame.