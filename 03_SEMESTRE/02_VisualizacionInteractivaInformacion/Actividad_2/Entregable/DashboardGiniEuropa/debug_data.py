import sys
import os
import pandas as pd

# Add the project root to the path so we can import app
sys.path.append(os.getcwd())

from app.services.data_loader import DataLoader

def test_loader():
    print("Testing DataLoader...")
    loader = DataLoader()
    print(f"File path: {loader.file_path}")
    
    if not os.path.exists(loader.file_path):
        print("❌ File does not exist!")
        return

    df = loader.load_data()
    print(f"Dataframe shape: {df.shape}")
    
    if df.empty:
        print("❌ Dataframe is empty.")
    else:
        print("✅ Dataframe loaded.")
        print(df.head())
        print("Unique countries:", df['Country Name'].unique())
        
        # Check specific countries
        target = ['España', 'Alemania', 'Francia']
        for t in target:
            if t in df['Country Name'].values:
                print(f"✅ Found {t}")
            else:
                print(f"❌ Missing {t}")

if __name__ == '__main__':
    test_loader()
