from scripts.summary import load_data, clean_data, compute_summary, save_summary
import os

def main():
    # File paths
    input_file = r"C:\Users\test\Desktop\weather_project\data\hourly_weather_10_days.csv"
    output_file = "output/results.txt"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Step 1: Load data
    print("Loading data...")
    df = load_data(input_file)
    
    if df is None:
        return
    
    # Step 2: Clean data
    print("Cleaning data...")
    clean_df = clean_data(df)
    
    # Step 3: Calculate stats
    print("Calculating statistics...")
    summary = compute_summary(clean_df)
    
    if not summary:
        return
    
    # Step 4: Save results
    print("Saving results...")
    save_summary(summary, output_file)

if __name__ == "__main__":
    main()