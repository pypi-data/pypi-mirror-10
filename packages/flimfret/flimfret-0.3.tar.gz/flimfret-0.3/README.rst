flimfret
--------

First, you will need to setup your data folder.
It should look something like this:

yourfolder/
	dateofdatacollection/
		celltype1/
			1.dat
			2.dat
			3.dat
		celltype2/
			1.dat
			2.dat
			3.dat
		celltype3/
			1.dat
			2.dat
			3.dat
etc.

The *.dat files are the lifetime curve output w/fitted models from SymPhoTime (in development: other formats) and MUST be a number and then .dat.

To use (with caution), simply navigate to yourfolder (seen above) and run the following after starting the python interpreter::

    >>> import flimfret
    >>> print flimfret.pipeline()
    
You will be prompted to enter the names of your celltypes--make sure these are spelled correctly!

This will create 
1) a new folder in each celltype folder containing normalized data
2) files with the averages for fit and decay of each celltype
3) files with compiled data for residuals, fit, and decay of each celltype
4) files with long format (suitable for downstream R analysis) compiled data for residuals, fit, and decay of each celltype
5) files with long format (suitable for downstream R analysis) compiled AVERAGES data for fit, and decay of ALL celltypes