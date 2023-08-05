PyGeneNet
---------

This package implements GeneNet algorithm for learning causal genetic network from time series data. The original implementation is described here

N. A. Barker, C. J. Myers, and H. Kuwahara, “Learning Genetic Regulatory Network Connectivity from Time Series Data,” IEEE/ACM Transactions on Computational Biology and Bioinformatics, vol. 8, no. 1, pp. 152–165, Jan. 2011.

Installation
------------

The program requires python 2.7 and packages below
    * numpy 1.8.2
    * pandas 0.15.2
    * graphviz 0.4.3
    * matplotlib (only required for timing in ``examples``)

To use this program, please have python installed on your system, and run:
    python setup.py install

The package will be installed in Python ``site-packages`` directory by default and will be available under the name pygenenet. 

To check your installation:
    python
    >>> import pygenenet

should not return an error


To remove the package, run (with appropriate permission)
    pip uninstall pygenenet

Or manually remove the files in the location installed above. The exact locations of each files can be obtained by running installation again with the --record option
    python setup.py install --record files.txt
Location of files will be written to `files.txt`.

Usage
-----
Example use can be found in pygenenet/examples
    Data files:
        ``net3_ssa_10``  : synthetic data from stochastic simulation of a 3-species network, for 2000s, trajectories written every 10s
        ``net3_ssa_100`` : synthetic data from stochastic simulation of a 3-species network, for 2000s, trajectories written every 100s
        ``net4_ssa_10``  : synthetic data from stochastic simulation of a 4-species network, for 2000s, trajectories written every 10s
        ``net4_ssa_100`` : synthetic data from stochastic simulation of a 4-species network, for 2000s, trajectories written every 100s

    Example scripts:
        1. ``demo_net3.py`` to learn the network from ``net3_ssa_10``. The result should look like this
            Learned causal network in 23.927177906s
                  CI  LacI  TetR
            CI     0     0    -1
            LacI  -1     0     0
            TetR   0    -1     0

        2. ``demo_net4.py`` to learn the network from ``net4_ssa_10``. The result should look like this
            Learned causal network in 23.927177906s
                  CI  GFP  LacI  TetR
            CI     0    0    -1     0
            GFP    0    0     1     0
            LacI   0    0    -1     0
            TetR   0    0    -1     0

        3. ``performance_net3.py`` and ``performance_net4.py`` will time the learning algorithm with various input subsets and input data frequencies and report a plot. These scripts require ``matplotlib``.


