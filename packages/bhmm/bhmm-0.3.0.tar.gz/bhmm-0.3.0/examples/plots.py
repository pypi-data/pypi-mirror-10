"""
Plotting utilities for Bayesian hidden Markov models.

"""

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bhmm import GaussianOutputModel

__author__ = "John D. Chodera, Frank Noe"
__copyright__ = "Copyright 2015, John D. Chodera and Frank Noe"
__credits__ = ["John D. Chodera", "Frank Noe"]
__license__ = "FreeBSD"
__maintainer__ = "John D. Chodera"
__email__="jchodera AT gmail DOT com"

def plot_state_assignments(model, s_t, o_t, tau=1.0, time_units=None, obs_label=None, title=None, figsize=(7.5,1.5), markersize=3, pdf_filename=None, npoints = 100, nbins=40):
    """
    Plot hidden state assignments and emission probabilities.

    Parameters
    ----------
    model : bhmm.HMM
        An HMM model with hidden state assignments to be plotted.
    s_t : numpy.array of shape (T) of int type
        The state assignments to be used to color the observations during plotting, or None if the observations should be colored black.
    o_t : numpy.array of shape (T) of float type
        The observation trajectory to be plotted.
    tau : float, optional, default=1.0
        Time interval between samples.
    time_units : str, optional, default=None
        Time unit label to associate with temporal axis.
    obs_label : str, optional, default=None
        Observation axis label.
    title : str, optional, default=None
        Title for the plot, if desired.
    pdf_filename : str, optional, default=None
        If specified, the plot will be written to a PDF file.
    npoints : int, optional, default=100
        Number of points for plotting output probability distributions.
    nbins : int, optional, default=40
        Number of bins for empirical histograms for each state.

    Example
    -------

    >>> from bhmm.util import testsystems    >>>     >>> import tempfile
    >>> filename = tempfile.NamedTemporaryFile().name
    >>> [model, O, S, bhmm_sampler] = testsystems.generate_random_bhmm(nstates=3, ntrajectories=1, length=10000)
    >>> plot_state_assignments(model, S[0], O[0], pdf_filename=filename)

    Label the axes.

    >>> models = bhmm_sampler._sample_output_mode(nsamples=1, save_hidden_state_trajectory=True)
    >>> plot_state_assignments(models[0], models[0].hidden_state_trajectories[0], O[0], tau=0.001, time_units='ms', obs_label='force / pN', pdf_filename=filename)

    """
    if pdf_filename:
        from matplotlib.backends.backend_pdf import PdfPages
        pp = PdfPages(pdf_filename)

    # Set plotting style.
    np.random.seed(sum(map(ord, "aesthetics")))
    palette = sns.color_palette('muted', model.nstates)
    sns.set(style='white', palette=palette, font_scale=0.75)

    # Create subplots.
    gridspec = { 'width_ratios' : [0.9, 0.1] }
    f, axes = plt.subplots(1,2, figsize=figsize, sharey=True, gridspec_kw=gridspec)
    ax1 = axes[0]; ax2 = axes[1]
    f.tight_layout()
    f.subplots_adjust(wspace=0.0)
    #f.subplots_adjust(left=0.05, right=0.95, bottom=0.15, top=0.9, wspace=0.0)

    ax1.hold(True)
    ax2.hold(True)

    # Determine min and max of observable range.
    omin = o_t.min(); omax = o_t.max()
    tmin = 0; tmax = o_t.size * tau

    # get output model
    output_model = model.output_model

    nsamples = o_t.shape[0] # total number of samples

    if s_t is None:
        # Plot all samples as black.
        tvec = tau * np.array(np.arange(nsamples), dtype=np.float32)
        ax1.plot(tvec, o_t, 'k.', markersize=markersize)

    # Plot histogram of all data.
    ax2.hist(o_t, nbins, align='mid', orientation='horizontal', color='k', stacked=True, edgecolor=None, alpha=0.5, linewidth=0, normed=True)

    # output distributions
    ovec = np.linspace(omin, omax, npoints)
    pobs = output_model.p_obs(ovec)

    # Plot.
    for state_index in range(model.nstates):
        # Get color for this state.
        color = next(ax1._get_lines.color_cycle)

        # Find and plot samples in state.
        if s_t is not None:
            indices = np.where(s_t == state_index)[0]
            nsamples_in_state = len(indices)
            if nsamples_in_state > 0:
                tvec = tau * np.array(np.squeeze(indices), dtype=np.float32)
                line, = ax1.plot(tvec, o_t[indices], '.', markersize=markersize, color=color)

        # Plot shading at one standard deviation width.
        if type(output_model) is GaussianOutputModel:
            mu = output_model.means[state_index]
            sigma = output_model.sigmas[state_index]
        else:
            # TODO: Generalize this to other kinds of output models.
            raise Exception('Not supported for non-gaussian output models.')
        ax1.plot(np.array([tmin, tmax]), mu*np.ones([2]), color=color, linewidth=1, alpha=0.7)
        ax1.fill_between(np.array([tmin, tmax]), (mu-sigma)*np.ones([2]), (mu+sigma)*np.ones([2]), facecolor=color, alpha=0.3, linewidth=0)

        #print "HIST: s_t = ",(s_t is not None)
        #print "HIST: nsamples_in_states",nsamples_in_state
        if s_t is not None:
            if nsamples_in_state > 0:
                # Plot histogram of data assigned to each state.
                #ax2.hist(o_t[indices], nbins, align='mid', orientation='horizontal', color=color, stacked=True, edgecolor=None, alpha=0.5, linewidth=0, normed=True)
                histrange = (o_t[indices].min(), o_t[indices].max())
                dx = (histrange[1]-histrange[0]) / nbins
                weights = np.ones(o_t[indices].shape, np.float32) / nsamples / dx
                [Ni, bins, patches] = ax2.hist(o_t[indices], nbins, align='mid', orientation='horizontal', color=color, stacked=True, edgecolor=None, alpha=0.5, linewidth=0, range=histrange, weights=weights)

        # Plot model emission probability distribution.
        pvec = pobs[:,state_index]
        pvec *= model.stationary_distribution[state_index] # Scale the Gaussian components since we are plotting the total histogram.
        ax2.plot(pvec, ovec, color=color, linewidth=1)

    if title:
        ax1.set_title(title)

    # Label axes.
    xlabel = 'time'
    if time_units:
        xlabel += ' / %s' % time_units
    ylabel = 'observable'
    if obs_label:
        ylabel = obs_label
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)

    # Clear ticks for probability histogram plot.
    ax2.set_xticks([])

    # Despine
    sns.despine()

    if pdf_filename:
        # Write figure.
        pp.savefig(bbox_inches='tight')
        pp.close()

    return

if __name__ == '__main__':
    # DEBUG

    # Create plots.
    from bhmm import testsystems
    [model, O, S, bhmm] = testsystems.generate_random_bhmm(nstates=3, ntrajectories=1, length=10000)
    models = bhmm._sample_output_mode(nsamples=1, save_hidden_state_trajectory=True)
    # Extract hidden state trajectories and observations.
    s_t = S[0]
    o_t = O[0]

    # Plot.
    plot_state_assignments(model, s_t, o_t, pdf_filename='plot.pdf')

