import pandas as pd
import numpy as np
import re

def load_file(path, colnames=[]):
    """
    This function will parse a standard HEKA .asc file into a pandas dataframe.

    Arguments: 
    path - a stringIO input of a standard HEKA output .asc file.

    Returns:
    df - The file reformatted into a dataframe.
    """

    lineIndices = []            
    
    # Splits string at \n and removes trailing spaces  
    with open(path, "r") as f:                        
        rawFile = f.read().strip().split("\n")         

    count=0          
    # Finds rows that contain header information to exclude from df                                     
    for line in rawFile:                                  
        if re.search(r"[a-z]+", line) == None:           
            lineIndices.append(count)                     
        count += 1                                    
    
    # Formats headerless file for later df
    processedFile = [rawFile[i].strip().replace(" ", "").split(",") for i in lineIndices]     

    # Use the difference in file with and without headers to find nSweeps
    nSweeps = int((len(rawFile)-len(processedFile)-1)/2)   

    if len(colnames) == 0: 
        if len(processedFile[0]) == 5:
            colnames = ['index','ti','i','tp','p']
        else:
            colnames = ['index','ti','i','tp','p','tv','v']

    df = pd.DataFrame(columns=colnames, data=processedFile)
    df = df.apply(pd.to_numeric)
    df = df.dropna(axis=0)

    # Make new column with sweep identity
    df['sweep'] = np.repeat(np.arange(nSweeps) + 1, len(df)/nSweeps)
    
    # Change units to something easier to work with
    df['p'] = df['p'] / 0.02
    df['ti'] *= 1000
    df['i'] *= 1e12
    df['tp'] *= 1000

    return df