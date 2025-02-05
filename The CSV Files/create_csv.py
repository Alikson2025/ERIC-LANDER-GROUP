import csv

data = [
    ["Email", "Area_of_Interest"],
    ["patiencemnena5996@gmail.com", "Genomics"],
    ["ibrahimnuhupaki8@gmail.com", "System Biology"],
    ["Ahmad Adamu Muhammad", "Metagenomics"],
    ["Saleh Muazu Muhammad", "Data Visualization"],
    ["maryammuhammadnawat@gmail.com", "Bioinformatics Tools Development"],
    ["mhizzphydo@gmail.com", "Machine Learning in Bioinformatics"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file 'data.csv' created successfully")
