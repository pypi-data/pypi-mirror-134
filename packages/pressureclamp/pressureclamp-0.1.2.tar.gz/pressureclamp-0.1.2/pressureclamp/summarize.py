import numpy as np
import pandas as pd

def sweep_summary(df, window, param):
    """
    This function will summarize sweep data based on a selected summary statistic.

    Arguments: 
    df - a pandas dataframe with columns p, ti, tp, sweep, and i.
    window - an iterable with the start and end coordinates of the baseline window.
    param - a summary statistic by which to summarize the data ('Max', 'Min' or 'Mean' currently accepted).
    
    Returns:
    df - a dataframe of summary data by sweep.
    """

    subsetDf = df.query('ti >= @window[0] and ti < @window[1]')
    groups = subsetDf.groupby('sweep')

    i_thalf = np.zeros(len(groups))
    for i, grp in df.groupby('sweep'):
        i_thalf[i-1] = grp['i'][grp['ti'] == 250.0]   ########  Change this number if you want to change where you measure your current #######

    if param == 'None':
        return
    elif param == 'Mean':
        iMean = groups['i'].mean()
        summaryDict = {
            'pressure': np.abs(groups['p'].median()),
            'mean_i': iMean,
            'mean_norm_i': np.abs(iMean)/np.max(np.abs(iMean)),
            'stdev_i': groups['i'].std()
        }

        summaryDf = pd.DataFrame(summaryDict)

    elif param == 'Min':
        iMin = groups['i'].min()
        summaryDict = {
            'pressure': np.abs(groups['p'].median()),
            'min_i': iMin,
            'min_norm_i': iMin/np.min(iMin),
            'i_thalf': i_thalf,
            'inactivation': i_thalf/iMin
        }

        summaryDf = pd.DataFrame(summaryDict)
    else:
        iMax = groups['i'].max()
        summaryDict = {
            'pressure': np.abs(groups['p'].median()),
            'max_i': iMax,
            'max_norm_i': iMax/np.max(iMax)
        }

        summaryDf = pd.DataFrame(summaryDict)
    return summaryDf