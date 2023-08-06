import numpy as np
import pandas as pd

def sweep_summary(df, stim, col, ref, window, param="Max"):
    """
    This function will summarize sweep data of a specified column of the dataframe based on a provided window within a reference column.

    Arguments
    -------------------
    df: dataframe
        A pandas dataframe with columns ``col`` and ``ref``.
    stim: string
        A string indicating the name of the stimulus column.
    col: string
        A string indicating the name of the column to be summarized.
    ref: string
        A reference column over-which to find the window.
    window: list
        An iterable with the start and end coordinates of the region over-which the sweep is to be summarized.
    param: string
        A string of either ``"Mean", "Min", or "Max"`` indicating the desired summary statistic. The default value is "Min"
    
    Returns
    --------------------
    dataframe
        A dataframe summarizing the desired ``col`` across sweeps over a given ``window`` on a reference column, ``ref``.
    """

    subsetDf = df.query(f'{ref} >= @window[0] and {ref} < @window[1]')
    groups = subsetDf.groupby('sweep')

    if param == 'None':
        return
    elif param == 'Mean':
        iMean = groups[col].mean()
        summaryDict = {
            stim: np.abs(groups[stim].median()),
            'mean_i': iMean,
            'mean_norm_i': np.abs(iMean)/np.max(np.abs(iMean)),
            'stdev_i': groups[col].std()
        }

        summaryDf = pd.DataFrame(summaryDict)

 
    elif param == 'Max':
        iMax = groups[col].max()
        summaryDict = {
            stim: np.abs(groups[stim].median()),
            'max_i': iMax,
            'max_norm_i': iMax/np.max(iMax)
        }

        summaryDf = pd.DataFrame(summaryDict)
        
    else:
        iMin = groups[col].min()
        summaryDict = {
            stim: np.abs(groups[stim].median()),
            'min_i': iMin,
            'min_norm_i': iMin/np.min(iMin),
        }

        summaryDf = pd.DataFrame(summaryDict)
        
    return summaryDf