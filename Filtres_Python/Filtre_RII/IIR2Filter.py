import numpy as np
import scipy.signal as signal

class IIR2Filter(object):           
    
    def createCoeffs(self,order,cutoff,filterType,design='butter',rp=1,rs=1,fs=0):
        
        self.designs = ['butter','cheby1','cheby2']
        self.filterTypes1 = ['lowpass','highpass','Lowpass','Highpass','low','high']
        self.filterTypes2 = ['bandstop','bandpass','Bandstop','Bandpass']
        
        self.isThereAnError = 1 
        self.COEFFS = [0] 
        
        if design not in self.designs:
            print('Vous avez donné une mauvaise conception de filtre ! Rappelez-vous : butter, cheby1, cheby2. ')
        elif filterType not in self.filterTypes1 and filterType not in self.filterTypes2:
            print('Mauvais type de filtre ! Info : lowpass, highpass, bandpass, bandstop.')
        elif fs < 0:
            print('La fréquence d''échantillonnage doit être positive!')
        else:
            self.isThereAnError = 0
        
        if fs and self.isThereAnError == 0:
            for i in range(len(cutoff)):
                cutoff[i] = cutoff[i]/fs*2
        
        if design == 'butter' and self.isThereAnError == 0:
            self.COEFFS = signal.butter(order,cutoff,filterType,output='sos')
        elif design == 'cheby1' and self.isThereAnError == 0:
            self.COEFFS = signal.cheby1(order,rp,cutoff,filterType,output='sos')
        elif design == 'cheby2' and self.isThereAnError == 0:
            self.COEFFS = signal.cheby2(order,rs,cutoff,filterType,output='sos')
        
        return self.COEFFS
        
    def __init__(self,order,cutoff,filterType,design='butter',rp=1,rs=1,fs=0):
        self.COEFFS = self.createCoeffs(order,cutoff,filterType,design,rp,rs,fs)
        self.acc_input = np.zeros(len(self.COEFFS))
        self.acc_output = np.zeros(len(self.COEFFS))
        self.buffer1 = np.zeros(len(self.COEFFS))
        self.buffer2 = np.zeros(len(self.COEFFS))
        self.input = 0
        self.output = 0

        
        
    def filter(self,input):

        if len(self.COEFFS[0,:]) > 1:
        
            self.input = input
            self.output = 0
            
            for i in range(len(self.COEFFS)):
                              
                self.FIRCOEFFS = self.COEFFS[i][0:3]
                self.IIRCOEFFS = self.COEFFS[i][3:6]
                
                self.acc_input[i] = (self.input + self.buffer1[i] 
                * -self.IIRCOEFFS[1] + self.buffer2[i] * -self.IIRCOEFFS[2])
                    
                self.acc_output[i] = (self.acc_input[i] * self.FIRCOEFFS[0]
                + self.buffer1[i] * self.FIRCOEFFS[1] + self.buffer2[i] 
                * self.FIRCOEFFS[2])
                
                self.buffer2[i] = self.buffer1[i]
                self.buffer1[i] = self.acc_input[i]
                
                self.input = self.acc_output[i]
            
            self.output = self.acc_output[i]
                
        return self.output  