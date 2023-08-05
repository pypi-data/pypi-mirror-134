import numpy as np
import pandas as pd

# todo: add time param (default 0.1sec)
def resample_df(df_orig, rule='100ms'):
    df = df_orig.copy()
    df['td'] = pd.to_timedelta(df['time'], 'ms')
    df.set_index(df['td'])
    df = df.resample(rule, on='td').mean().bfill()
    #df = df.drop(columns=['time'])
    return df


def read_scan_csv(csv_file_path):
    'special method handling the string representation of the values in list'
    
    df_scan_string = pd.read_csv(csv_file_path)
    df_scan_np = pd.DataFrame(columns=['time', 'ranges', 'angles'])
    
    for index, row in df_scan_string.iterrows():
        ranges_string = row['ranges']
        angles_string = row['angles']
        
        ranges_list = ranges_string.strip('][').split(', ')
        angles_list = angles_string.strip('][').split(', ')
        
        np_ranges = np.asarray(ranges_list).astype('float64')
        np_angles = np.asarray(angles_list).astype('float64')
        
        df_scan_np = df_scan_np.append({'time': row['time'], 'ranges': np_ranges, 'angles': np_angles}, ignore_index=True)
    
    return df_scan_np
