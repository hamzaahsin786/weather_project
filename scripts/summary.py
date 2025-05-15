import pandas as pd

def load_data(filepath):
    """Load the weather data from CSV"""
    try:
        df = pd.read_csv(r'C:\Users\test\Desktop\weather_project\data\hourly_weather_10_days.csv')
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean missing values in the data"""
    if df is None:
        return None
        
    for column in df.columns:
        # Handle numeric columns
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].mean())
        # Handle text columns
        elif pd.api.types.is_string_dtype(df[column]):
            df[column] = df[column].fillna('Unknown')
    
    print("Data cleaned!")
    return df

def compute_summary(df):
    """Calculate statistics for numeric columns"""
    if df is None:
        return None
        
    summary = {}
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    for col in numeric_cols:
        summary[col] = {
            'mean': df[col].mean(),
            'min': df[col].min(),
            'max': df[col].max()
        }
    
    print("Summary calculated!")
    return summary

def save_summary(summary, output_path):
    """Save results to a text file"""
    if not summary:
        return False
        
    try:
        with open(output_path, 'w') as f:
            for col, stats in summary.items():
                f.write(f"{col}:\n")
                f.write(f"  Average: {stats['mean']:.2f}\n")
                f.write(f"  Minimum: {stats['min']:.2f}\n")
                f.write(f"  Maximum: {stats['max']:.2f}\n\n")
        print(f"Results saved to {output_path}!")
        return True
    except Exception as e:
        print(f"Error saving results: {e}")
        return False