#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 13:38:06 2026

@author: valentinaparada
"""

import pandas as pd
import os

# 1. Check if the folder is correct
_thisDir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(_thisDir, 'image_table.csv')

print(f"--- Checking Directory ---")
print(f"Looking for CSV at: {csv_path}")

if not os.path.exists(csv_path):
    print("❌ ERROR: File not found! Is 'image_table.csv' in the same folder as this script?")
else:
    print("✅ SUCCESS: File found!")
    
    # 2. Check the Column Names
    df = pd.read_csv(csv_path)
    actual_columns = df.columns.tolist()
    
    print(f"\n--- Checking Columns ---")
    print(f"Columns in your CSV: {actual_columns}")
    
    # These are the 3 names your experiment code REQUIRES:
    required = ['product_id', 'version', 'image_path']
    
    for col in required:
        if col in actual_columns:
            print(f"✅ Column '{col}': MATCHED")
        else:
            print(f"❌ Column '{col}': NOT FOUND (Check for capital letters or spaces!)")

    # 3. Check for data
    print(f"\n--- Checking Data ---")
    print(f"Total rows of stimuli: {len(df)}")