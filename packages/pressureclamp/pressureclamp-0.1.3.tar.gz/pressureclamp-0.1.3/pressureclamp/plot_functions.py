import cufflinks as cf
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import iqr
from scipy.stats import norm

def sigmoid_fit(p, p50, k):
    """
    This function defines a sigmoid curve.

    Arguments
    ------------------- 
    p: series 
        The abscissa data.
    p50: float
        The inflection point of the sigmoid.
    k: float
        The slope at the inflection point of a sigmoid.
    
    Returns
    --------------------
    series
        The ordinate for a boltzmann sigmoid with the passed parameters.
    """
    return(1 / (1 + np.exp((p50 - p) / k)))
    
def single_gauss_fit(x, a1, m1, s1):
    """
    This function defines a single gaussian curve.

    Arguments
    ------------------- 
    x: series 
        The abscissa data.
    a1: float
        The amplitude of the gaussian.
    m1: float
        The midpoint of the gaussian.
    s1: float
        The standard deviation of the gaussian
    
    Returns
    --------------------
    series
        The ordinate for a gaussian curve described by the input parameters.
    """
    gauss = a1 * norm.pdf(x, loc = m1, scale = s1)

    return gauss

def double_gauss_fit(x, a1, a2, m1, m2, s1, s2):
    """
    This function defines a double gaussian curve.

    Arguments
    ------------------- 
    x: series 
        The abscissa data.
    a1: float
        The amplitude of the first gaussian.
    a2: float
        The amplitude of the second gaussian.
    m1: float
        The midpoint of the first gaussian.
    m2: float
        The midpoint of the second gaussian.
    s1: float
        The standard deviation of the first gaussian.
    s2: float
        The standard deviation of the second gaussian.
    
    Returns
    --------------------
    series
        The ordinate for a pair of gaussian curve described by the input parameters.
    """
    
    gauss = a1 * norm.pdf(x, loc = m1, scale = s1)
    gauss += a2 * norm.pdf(x, loc = m2, scale = s2)

    return gauss

def triple_gauss_fit(x, a1, a2, a3, m1, m2, m3, s1, s2, s3):
    """
    This function defines a double gaussian curve.

    Arguments
    ------------------- 
    x: series 
        The abscissa data.
    a1: float
        The amplitude of the first gaussian.
    a2: float
        The amplitude of the second gaussian.
    a3: float
        The amplitude of the third gaussian.
    m1: float
        The midpoint of the first gaussian.
    m2: float
        The midpoint of the second gaussian.
    m3: float
        The midpoint of the third gaussian.
    s1: float
        The standard deviation of the first gaussian.
    s2: float
        The standard deviation of the second gaussian.
    s3: float
        The standard deviation of the third gaussian.
    
    Returns
    --------------------
    series
        The ordinate for three gaussian curves described by the input parameters.
    """
    gauss = a1 * norm.pdf(x, loc = m1, scale = s1)
    gauss += a2 * norm.pdf(x, loc = m2, scale = s2)
    gauss += a3 * norm.pdf(x, loc = m3, scale = s3)

    return gauss

def ngauss_guesses(x, y, nGauss):
    """
    This function will generate initial guesses for a gaussian fit to single-channel data.

    Arguments
    ------------------- 
    x: list 
        A list of histogram bins.
    y: list
        A list of histogram weights.
    nGauss: int
        The number of gaussians estimated to represent the data.
    
    Returns
    --------------------
    test: list
        A list of parameter estimates for the gaussian fits.
    """
    initial_guesses = {"p":[1], "u": [x[np.argmax(y)]], "s": [0.5]}
    for i in list(range(0, nGauss - 1)):
        initial_guesses["p"].append(0.5 * initial_guesses["p"][i])
        initial_guesses["u"].append(-2.2 * (i+1) + initial_guesses["u"][i])
        initial_guesses["s"].append(2 * initial_guesses["s"][i])

    arr = [np.array(initial_guesses['p']), np.array(initial_guesses['u']), np.array(initial_guesses['s'])]

    return(arr)

def plot_sweeps(df, x, stim, col):
    """
    This function will plot a dataframe of sweeps using plotly with hidden axis.

    Arguments
    --------------
    df: dataframe
    
    x: string
        A string identifying the column defining the abscissa of the plot.
    
    stim: string
        A string identifying the column defining the stimulus amplitude.
        
    col: string
        A string identifying the response column.

    Returns
    -------------
    fig: plotly.figure
        A plotly figure object containg a pair of stacked plots of the pressure clamp stimulus and response.
    """

    fig = make_subplots(rows=2, cols=1,  row_width=[0.6, 0.3])
    
    for name, sweep in df.groupby('sweep'):
        
        fig.add_trace(
            go.Scatter(mode='lines', name=name, x=sweep.loc[:, x], y=sweep.loc[:, stim], marker=dict(color='#800000'),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'),
            row=1, col=1)
            
        fig.add_trace(
            go.Scatter(mode='lines', name=name, x=sweep.loc[:, x], y=sweep.loc[:, col], marker=dict(color='black'),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'),
            row=2, col=1)

    fig.update_layout(
        height=400,
        width=600,
        template='none',
        xaxis_showticklabels=False,
        xaxis_showgrid=False,
        yaxis_showticklabels=False,
        yaxis_showgrid=False,
        xaxis2_showticklabels=False,
        xaxis2_showgrid=False,
        yaxis2_showticklabels=False,
        yaxis2_showgrid=False,
        showlegend=False,
        hovermode='closest')

    fig.update_xaxes(matches='x')

    return(fig)

def plot_sweeps_stacked(df, x, stim, col):
    """
    This function will plot a dataframe of sweeps using plotly with hidden axis. Each sweep will be stacked with a defined offset.

    Arguments
    --------------
    df: dataframe
    
    x: string
        A string identifying the column defining the abscissa of the plot.
    
    stim: string
        A string identifying the column defining the stimulus amplitude.
        
    col: string
        A string identifying the response column.

    Returns
    -------------
    fig: plotly.figure
        A plotly figure object containg a pair of stacked plots of the pressure clamp stimulus and response.
    """
    nsweeps = len(np.unique(df.sweep))

    fig = make_subplots(rows=nsweeps + 1, cols=1,  row_width=[1/(nsweeps + 1) for i in range(nsweeps + 1)])
    
    for name, sweep in df.groupby('sweep'):
        
        fig.add_trace(
            go.Scatter(mode='lines', name=name, x=sweep.loc[:, x], y=sweep.loc[:, stim], marker=dict(color='#800000'),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'),
            row=1, col=1)
            
        fig.add_trace(
            go.Scatter(mode='lines', name=name, x=sweep.loc[:, x], y=sweep.loc[:, col], marker=dict(color='black'),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'),
            row= int(np.unique(sweep.sweep)) + 1, col=1)

    fig.update_layout(
        height=800,
        width=800,
        template='none',
        showlegend=False,
        hovermode='closest')

    fig.update_xaxes(matches='x')

    return(fig)

def add_scalebars(df, fig, locs):
    """
    This function will add scalebars to a plot.

    Arguments
    ---------
    df: dataframe
    
    fig: plotly.figure
        A plotly figure of pressure clamp sweeps as made by ``plot_sweeps``
    locs: dictionary 
        A dictionary with the axis names as keys and scalebar limits as values for scalebars.

    Returns
    ---------
    fig: plotly.figure 
        A modified plotly figure of sweeps with scalebars.
    """

    try:
        if all(value == 0 for value in locs['p']) == False:
            pscale = dict(type="line", 
                        x0=locs['t'][0],
                        x1=locs['t'][0], 
                        y0=locs['p'][0], 
                        y1=locs['p'][1],
                        line=dict(color="black",
                                    width=2))

            fig.add_shape(pscale, row=1, col=1)

        if all(value == 0 for value in locs['i']) == False:
            iscale = dict(type="line", 
                        x0=locs['t'][0], 
                        x1=locs['t'][0], 
                        y0=locs['i'][0], 
                        y1=locs['i'][1],
                        line=dict(color="black",
                                    width=2))

            fig.add_shape(iscale, row=2, col=1)
            
        if all(value == 0 for value in locs['t']) == False:
            tscale = dict(type="line", 
                        x0=locs['t'][0], 
                        x1=locs['t'][1], 
                        y0=locs['i'][0], 
                        y1=locs['i'][0],
                        line=dict(color="black",
                                    width=2))
            
            fig.add_shape(tscale, row=2, col=1)
    except (KeyError, TypeError):
        print("Values must be entered as space separated integers.")   
    return(fig) 

def plot_summary(df, x, y):
    """
    This function will plot ``x`` as a function of ``y`` from a summary statistics dataframe as produced by ``sweep_summary``.

    Arguments
    ------------
    df: dataframe
        A dataframe of summarized pressure clamp sweeps.
    x: string
        A string indicating the abscissa.
    y: string
        A string indicating the ordinate.
    
    Returns
    ------------
    fig: plotly.figure
        A plotly figure object plotting ``x`` as a function of ``y``.
    """

    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(mode='markers',
                   name='p50', 
                   marker_color='#FF3300', 
                   marker_line_width = 1,
                   marker_size = 5,
                   x=df[x], 
                   y=df[y],
                   hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'
                   )
    )

    fig.update_xaxes(title_text='Pressure (-mm Hg)')
    fig.update_yaxes(title_text='I/Imin')

    fig.update_layout(
        height=400,
        width=400,
        template='simple_white',
        showlegend=False,
        hovermode='closest')

    return(fig)

def fit_layer(df, x, fig, fit):
    """
    This function will overlay a fit on an existing current-pressure response curve as produced by ``plot_summary``.

    Arguments
    ------------
    df: dataframe
        A dataframe of summarized pressure clamp sweeps.
    x: string
        A string identifying the abscissus of the plot.
    fig: plotly.figure
        A plotly figure of pressure clamp sweeps as made ``plot_summary``
    fit: list
        A list or other iterable with fit parameters for a boltzmann sigmoid as defined in ``sigmoid_fit``.
    
    Returns
    ------------
    fig: plotly.figure
        A plotly figure object plotting ``x`` as a function of ``y``.
    """

    xfine = np.linspace(min(df.loc[:,x]),max(df.loc[:,x]), 100)
    fig.add_trace(
    go.Scatter(mode='lines',
               name='fit', 
               marker_color='black', 
               marker_line_width = 1,
               x=xfine, 
               y=sigmoid_fit(xfine, *fit),
               hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'
               )
    )

    return(fig)

def frequency_histogram(df, col, nbins, ngauss = 2):
    """
    This function will fit a histogram to an current trace for analyzing single-channel events.

    Arguments
    ------------
    df: dataframe
        A dataframe of an isolated single-channel event.
    col: string
        A string identifying the column to be binned into histograms.
    nbins: int
        The number of histogram bins.
    ngauss: int
        The number of gaussians to be fit to the data. Defaults to 2.
    
    Returns
    ------------
    fig: plotly.figure
        A plotly figure showing the histogram of values for ``col`` in your dataframe overlaid with gaussian fits.
    popt: list
        An iterable containing the fit parameters for the gaussians.
    pcov: list
        An iterable of covariance matrices for the fits.
    """
    
    range_x = np.max(df.loc[:, col]) - np.min(df.loc[:,col])
    #bin_width = 2*iqr(df.i)*len(df.i)**(-1/3) ## Freedman and Diaconis method
    #nbins = round(range_x/bin_width)
    bin_width = range_x/nbins
    [y, x]=np.histogram(df.loc[:,col], nbins, density=True)
    test = ngauss_guesses(x, y, ngauss)

    fig = go.Figure([go.Bar(x=x[0:-1]+0.5*bin_width, y=y, marker_color = "black")])
    
    fig.update_xaxes(title_text='Current (pA)')
    fig.update_yaxes(title_text='Density')

    fig.update_layout(
        height=600,
        width=600,
        template='simple_white',
        showlegend=False,
        hovermode='closest')

    if ngauss == 3:
        popt, pcov = curve_fit(triple_gauss_fit, x[0:-1]+0.5*bin_width, y, p0=test)
        xfine = np.linspace(min(df.loc[:, col]), max(df.loc[:, col]), 500)

        fig.add_trace(
            go.Scatter(mode='lines',
                name='fit',
                marker_color='orange',
                marker_line_width = 1,
                fill = 'tozeroy',
                x=xfine,
                y=single_gauss_fit(xfine, *popt[[0,3,6]]),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'
            )
        )

        fig.add_trace(
            go.Scatter(mode='lines',
                name='fit',
                marker_color='purple',
                marker_line_width = 1,
                fill = 'tozeroy',
                x=xfine,
                y=single_gauss_fit(xfine, *popt[[1,4,7]]),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'
            )
        )

        fig.add_trace(
            go.Scatter(mode='lines',
                name='fit',
                marker_color='red',
                marker_line_width = 1,
                fill = 'tozeroy',
                x=xfine,
                y=single_gauss_fit(xfine, *popt[[2,5,8]]),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'
            )
        )

    else:
        popt, pcov = curve_fit(double_gauss_fit, x[0:-1]+0.5*bin_width, y, p0=test)
        xfine = np.linspace(min(df.loc[:,col]), max(df.loc[:,col]), 500)

        fig.add_trace(
            go.Scatter(mode='lines',
                name='fit',
                marker_color='orange',
                marker_line_width = 1,
                fill = 'tozeroy',
                x=xfine,
                y=single_gauss_fit(xfine, *popt[[0,2,4]]),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'
            )
        )

        fig.add_trace(
            go.Scatter(mode='lines',
                name='fit',
                marker_color='purple',
                marker_line_width = 1,
                fill = 'tozeroy',
                x=xfine,
                y=single_gauss_fit(xfine, *popt[[1,3,5]]),
                hovertemplate='x: %{x}<br>' + 'y: %{y}<br>'
            )
        )

    return(fig, popt, pcov)

