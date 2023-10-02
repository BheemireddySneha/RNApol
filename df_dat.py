import pandas as pd

def extract_data_from_dat_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        line = line.strip()
        if line:
            key, value = line.split(':')
            key = key.strip()
            value = value.strip()
            data[key] = value

    return data

# File paths
file1_path = '/home/sneha/work/RnaP/ppcheck/PA_5UH5_f_r_noNA_202304071308_8b00e06a077848c9/A-B_results.dat'
file2_path = '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/A-B_results.dat'

# Extract data from the first file
data1 = extract_data_from_dat_file(file1_path)

# Extract data from the second file
data2 = extract_data_from_dat_file(file2_path)

# Create a dataframe with the extracted data
df = pd.DataFrame({'File 1': data1, 'File 2': data2})

# Print the dataframe
print(df)

