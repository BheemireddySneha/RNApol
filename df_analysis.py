import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import plotly.express as px

# Read the CSV file into a dataframe
df = pd.read_csv('combined_rev.csv')

# Remove ' kJ/mol' from the numerical columns and convert to float
numerical_columns = ['Hydrogen Bond Energy', 'Electrostatic Energy', 'van der Waals Energy',
                     'Total Stabilizing Energy']
for column in numerical_columns:
    df[column] = df[column].str.replace(' kJ/mol', '').astype(float)
odd_color = 'cyan'
even_color = 'gold'

# Plot bar graphs for each column
for column in df.columns[1:-1]:  # Exclude 'Unnamed' and 'Filename' columns
    fig = px.bar(df, x='Filename', y=column,
                 title=f'Comparison of {column}', template='plotly_dark')
    
    # Set color based on odd/even values
    colors = ['odd' if value % 2 == 1 else 'even' for value in df[column]]
    fig.update_traces(marker_color=colors)
    
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    fig.update_traces(marker_line_width=2)  # Increase the thickness of the bar
    fig.show()



