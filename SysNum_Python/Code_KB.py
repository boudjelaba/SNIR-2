import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

def creation_sinus(freq, fe, duree=None, return_time=False):
    
    # Si duree est None, retourne une période du signal
    if duree is None:
        duree = 1 / freq

    t = np.arange(duree * fe)/fe
    sig_sin = np.sin(2 * np.pi * freq * t)

    if return_time is False:
        return sine_wave
    else:
        return (t, sig_sin)

def trace_echant_demo(duree, freqs, FE=10000, fe=50):

    n_caracts = len(freqs)
    fig_haut = n_caracts * 3.25
    fig, axes = plt.subplots(n_caracts, 1, figsize=(15,fig_haut))
    
    t = None
    
    i = 0
    #fe = fe
    facteur = int(FE/fe)
    print(f"Fréquence d'échantillonnage : {fe} Hz")
    for freq in freqs:
        t, signal = creation_sinus(freq, FE, duree, return_time = True)
        td = t[::facteur]
        signal_ech = signal[::facteur]
        
        axes[i].plot(t, signal)
        axes[i].axhline(0, color="gray", linestyle="-", linewidth=0.5)
        axes[i].plot(td, signal_ech, linestyle='None', alpha=0.8, marker='s', color='black')
        axes[i].vlines(td, ymin=0, ymax=signal_ech, linestyle='-.', alpha=0.8, color='black')
        axes[i].set_ylabel("Amplitude")
        axes[i].set_xlabel("Temps (s)")
        axes[i].set_title(f"Signal de fréquence {freq}Hz échantillonné à {fe}Hz")
        
        i += 1
    fig.tight_layout(pad = 3.0)