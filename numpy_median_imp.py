import numpy as np

# Create a sample 2D NumPy array
data_2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# Calculate the median along the flattened array
median_flat = np.median(data_2d)
print(f"Median of the flattened array: {median_flat}")

# Calculate the median along axis 0 (columns)
median_cols = np.median(data_2d, axis=0)
print(f"Median along columns: {median_cols}")

# Calculate the median along axis 1 (rows)
median_rows = np.median(data_2d, axis=1)
print(f"Median along rows: {median_rows}")

# Example with NaN values
data_2d_nan = np.array([[1, 2, np.nan],
                         [4, 5, 6],
                         [7, np.nan, 9]])

median_cols_nan = np.nanmedian(data_2d_nan, axis=0)
print(f"Median along columns (ignoring NaNs): {median_cols_nan}")

median_rows_nan = np.nanmedian(data_2d_nan, axis=1)
print(f"Median along rows (ignoring NaNs): {median_rows_nan}")