import pandas as pd
import os

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

# List of file paths
file_paths = [
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/A-B_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/A-C_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/A-D_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/A-E_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/A-F_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/B-C_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/B-D_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/B-E_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/B-F_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/C-D_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/C-E_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/C-F_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/D-E_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/D-F_results.dat',
    '/home/sneha/work/RnaP/ppcheck/PA_6C04_r_f_202304071308_dd5da0396642481e/E-F_results.dat'
]

# Extract data from each file and store in a list
data_list = []
for file_path in file_paths:
    data = extract_data_from_dat_file(file_path)
    data['Filename'] = os.path.basename(file_path)  # Add 'Filename' column with the filename
    data_list.append(data)

# Create a dataframe with the extracted data
df = pd.DataFrame(data_list)

df.to_csv('output_6c04.csv')

# Print the dataframe
print(df)

