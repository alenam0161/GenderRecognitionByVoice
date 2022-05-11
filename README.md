# Gender Recognition by Voice and Speech Analysis

The analysis are inspired by Kaggle competition of gender recognition by voice. 
Dataset Source: [Kaggle Datasets: Gender Recognition by Voice](https://www.kaggle.com/primaryobjects/voicegender)

This dataset is released by [Kory Becker](https://github.com/primaryobjects) on [Kaggle](https://www.kaggle.com/) under [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/).  

Our Research has been done in [CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D) dataset, especially, AudioWAV dataset inside.

Dataset includes 7442 original clips from 91 actors.  These clips were from 48 male and 43 female actors between the ages of 20 and 74 coming from a variety of races and ethnicities (African America, Asian, Caucasian, Hispanic, and Unspecified). Actors spoke from a selection of 12 sentences. It means, that we focus on creating more general model, with non-one sentence speech.

We used python feature extraction created by ourselves, with focusing the attributes, that are able to identify the features that indicate differences between male and female.

# The Dataset

## The following acoustic properties of each voice are measured and included within the CSV:

* **meanfreq  :** mean frequency (in kHz)
* **sd        :** standard deviation of frequency
* **median    :** median frequency (in kHz)
* **mode_val  :** mode of frequency
* **Q25       :** first quantile (in kHz)
* **Q75       :** third quantile (in kHz)
* **IQR       :** interquantile range (in kHz)
* **skew      :** skewness (see note in specprop description)
* **kurt      :** kurtosis (see note in specprop description)
* **sp.ent    :** spectral entropy
* **sfm       :** spectral flatness
* **fft_mode  :** mean mode frequency
* **fft_max   :** max frequency
* **fft_min   :** min frequency
* **centroid  :** frequency centroid (see specprop)
* **peakf     :** peak frequency (frequency with highest energy)
* **meanf     :** average of fundamental frequency measured across acoustic signal
* **minf      :** minimum fundamental frequency measured across acoustic signal
* **maxf      :** maximum fundamental frequency measured across acoustic signal
* **meandom   :** average of dominant frequency measured across acoustic signal
* **mindom    :** minimum of dominant frequency measured across acoustic signal
* **maxdom    :** maximum of dominant frequency measured across acoustic signal
* **dfrange   :** range of dominant frequency measured across acoustic signal
* **modindx   :** modulation index. Calculated as the accumulated absolute difference between adjacent measurements of fundamental frequencies divided by the frequency range
* **label     :** male or female
