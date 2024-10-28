import pandas as pd

def load_data(file_path):
    """Loads CSV data and generates a prompt for the LLM."""
    df = pd.read_csv(file_path)
    if df.columns[0] == 'Unnamed: 0':
        df = df.set_index(df.columns[0])  # Set the unnamed column as the index
        df.reset_index(drop=True, inplace=True)

    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.max_colwidth', None)
    # Basic analysis of data
    basic_summary = df.describe(include='all').T
    data_types = df.dtypes
    missing_values = df.isnull().sum()
    unique_values = df.nunique()
    mode_values = df.mode().iloc[0]
    detailed_summary = pd.DataFrame({
        'Data Type': data_types,
        'Missing Values': missing_values,
        'Unique Values': unique_values,
        'Most Frequent Value': mode_values,
    })
    
    # Adding basic summary to detailed summary
    detailed_summary = detailed_summary.join(basic_summary)
    columns = df.columns.to_list()
    data_head=df.head()
    
    prompt = (
    f"df.describe: {detailed_summary} \n"
    f"df.columns: {columns}\n"
    f"df.head:{data_head}\n"
    )
    
    return df, prompt
