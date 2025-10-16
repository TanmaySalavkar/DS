import pandas as pd

def main():
    # Load CSV
    df = pd.read_csv("data/Books_Dataset.csv")

    # Example processing: count books per category
    if "Category" in df.columns:
        category_counts = df["Category"].value_counts()
        print("Book counts by category:\n")
        print(category_counts)
    else:
        print("Category column not found in dataset!")

    # Example: list first 5 books
    if "Title" in df.columns:
        print("\nFirst 5 books in the dataset:\n")
        print(df["Title"].head())
    else:
        print("Title column not found in dataset!")

if __name__ == "__main__":
    main()
