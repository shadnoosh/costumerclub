import pandas as pd

# Re-load the uploaded file after code execution state reset
file_path = "data/products.xlsx"
existing_products_df = pd.read_excel(file_path)

# Strip column names to avoid any issues
existing_products_df.columns = existing_products_df.columns.str.strip()

# Generate 10 more sample clothing products
additional_products = pd.DataFrame({
    "Product ID": [f"P{str(i).zfill(3)}" for i in range(6, 16)],
    "Product Name": [
        "Slim Fit Jeans", "Leather Jacket", "Wool Sweater", "Denim Skirt", "Formal Trousers",
        "Silk Scarf", "Cotton Blazer", "Linen Shirt", "Hoodie", "Tracksuit"
    ],
    "Category": [
        "Bottomwear", "Outerwear", "Winterwear", "Bottomwear", "Bottomwear",
        "Accessories", "Outerwear", "Topwear", "Casualwear", "Sportswear"
    ],
    "Price": [40, 85, 60, 35, 50, 20, 70, 45, 30, 55]
})

# Append to the original DataFrame
updated_products_df = pd.concat([existing_products_df, additional_products], ignore_index=True)

# Save the updated DataFrame back to Excel
updated_file_path = "data/updated_products.xlsx"
updated_products_df.to_excel(updated_file_path, index=False)

updated_file_path