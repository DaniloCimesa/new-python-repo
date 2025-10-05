import camelot
import os

folder_path = r"C:\Users\Danilo\OneDrive\Desktop\pdfs"
search_names = ['GLAUSER', 'DARLEUX']

for filename in os.listdir(folder_path):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        print(f"\nProcessing: {filename}")
        tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')
        for idx in [1, 2, 6, 7]:
            if tables.n > idx:
                df = tables[idx].df
                filtered_data = df[
                    df.apply(
                        lambda row: any(row.astype(str).str.contains(name, case=False).any() for name in search_names),
                        axis=1
                    )
                ]
                if not filtered_data.empty:
                    print(f"\nMatches in table {idx}:")
                    print(filtered_data)
            else:
                print(f"Table {idx} not found in this PDF.")


"""
import camelot

pdf_path = r"C:\Users\Danilo\OneDrive\Desktop\t2"

# Extract all tables from all pages
tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')

print(f"Total tables found: {tables.n}")

# Show all data in table 1
print("All data in table 1:")
print(tables[2].df)
"""