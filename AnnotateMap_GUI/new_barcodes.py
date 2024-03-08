import pandas as pd
from scipy.spatial import KDTree
import tkinter as tk
from tkinter import filedialog

# Create a function to handle file selection
def select_csv_file():
    file_path = filedialog.askopenfilename(title="Select CSV File with pixels/barcodes", filetypes=[("CSV files", "*.csv")])
    if file_path:
        return file_path
    else:
        return None

# Prompt the user to select the contours CSV file
contours_file_path = select_csv_file()

# Prompt the user to select the tissue positions CSV file
tissue_positions_file_path = select_csv_file()

# Check if the user canceled the file selection
if not contours_file_path or not tissue_positions_file_path:
    print("File selection canceled. Exiting.")
    exit()

# Load the CSV files
contours_df = pd.read_csv(contours_file_path)
tissue_positions_df = pd.read_csv(tissue_positions_file_path)

# Filter out entries where 'in_tissue' is not 1
tissue_positions_df = tissue_positions_df[tissue_positions_df['in_tissue'] == 1]

# Create a KDTree for efficient nearest neighbor search
tree = KDTree(tissue_positions_df[['pxl_col_in_fullres', 'pxl_row_in_fullres']])

# Find the nearest neighbor for each point in contours_df
closest_points_indices = tree.query(contours_df[['x', 'y']])[1]

# Extract the corresponding barcodes
closest_barcodes = tissue_positions_df.iloc[closest_points_indices]['barcode']

# Remove duplicate barcodes
unique_barcodes = closest_barcodes.drop_duplicates()

# Save the unique barcodes to a new CSV file
unique_barcodes.to_csv('barcodes.csv', index=False)

print("Unique barcodes have been saved to barcodes.csv")
