import pandas as pd
import numpy as np
import re

def load_file(path, header=[]):
    """
    This function will parse a standard HEKA .asc file into a pandas dataframe.

    Parameters
    ---------- 
    path : string 
        String input of path to a standard HEKA output .asc file.
    
    headers : list
        A list or iterable of string column headers. The list of headers must match the number of columns in the dataframe.
        
    Returns
    ---------
    dataframe
        The file reformatted into a dataframe with the given headers.
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

    if len(processedFile[0]) != len(header):
        raise Exception("Header length must match number of columns in dataframe")
        
    df = pd.DataFrame(data=processedFile, columns=header)
    df = df.apply(pd.to_numeric)
    df = df.dropna(axis=0)

    # Make new column with sweep identity
    df['sweep'] = np.repeat(np.arange(nSweeps) + 1, len(df)/nSweeps)
    
    return df