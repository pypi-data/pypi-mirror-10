===============
 README
===============

MRI-FFT is a package for efficiently calculating the inverse Fourier’s Transform. It contains classes for 1D, 2D, and 3D iFFTs, and there are two routes available to process the data:

- direct iFFTs, for when all of the k-space data is available immediately
- decomposed iFFTs, to enable data to be processed during a scan