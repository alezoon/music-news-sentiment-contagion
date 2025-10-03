import pandas as pd

#--------------------------------------------
# Reformatting data for display in Streamlit
#--------------------------------------------

def reformatData(data):
    df = pd.DataFrame(data)
    df['score'] = (df['score'] * 100).round(1)
    df.columns = ['Emotions', 'Probability (%)']
    df = df.sort_values('Probability (%)', ascending=False)
    return df
