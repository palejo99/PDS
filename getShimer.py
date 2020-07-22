# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:08:52 2017

@author: ssd
"""


import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import math as math

def preprocesar(y) :
    promedio = sum(y)/len(y);
    mayorAbs = max( abs(max(y)-promedio), abs(min(y)-promedio) );
    yOut = [((val-promedio)/mayorAbs) for val in y];
    return yOut;


colors = ["r", "g", "b", "y", "k", "r", "g", "b", "y", "k"];
personas = ["alejandroAlzate", "AlejandroMontoya", "AlejandroPatinho",
            "Carlos", "Diego", "Edwin", "John", "Miguel", "Veronica"];
nombres = ["normalA", "normalE", "normalI", "normalO", "normalU", 
           "AislamientoA", "AislamientoE", "AislamientoI", "AislamientoO", 
           "AislamientoU", "promedio normal", "promedio en aislamiento"];
    
for per in range(len(personas)) :    ## recorrer todas las personas
    figureName = "PY_shimer_" + personas[per];
    handleFig = plt.figure(figureName, figsize=[20,18]);
    plt.figure()
    plt.hold("on");
    
    maximo = 167;
    promNormal = [0     for j in range(maximo) ];
    promAislamiento = [0     for j in range(maximo) ];
    for n in range(10):      ## utilizar todos los audios de una persona
        audioName = personas[per] + "/" + nombres[n] + ".wav";
        [fs, data]= waves.read(audioName);
        data = preprocesar(data);

        x = int(0.02*fs); ## inicios
        y = int(0.03*fs); ## para sumarle al inicio
        
               
        """  maximo = math.floor( len(data)/(y) ); """
        Amax = [0  for j in range(maximo)];
        sh = [0  for j in range(maximo)];
        promedio=0;
        
        
        for i in range(maximo-1) :
            subData = [data[j]  for j in range(x*i, x*i+y -1)];
            Amax[i] = max(subData);
            promedio = promedio + Amax[i]; 
        
        promedio = promedio/maximo;
        
        for i in range(maximo-2) :
           sh[i] = abs(Amax[i+1] - Amax[i]);
      
        
        if n <= 5:
            promNormal = [promNormal[j] + sh[j]  for j in range(maximo)];
        else:
            promAislamiento = [promAislamiento[j] + sh[j]  for j in range(maximo)];
        
         
        if n <= 5 :
            plt.plot(sh, colors[n], LineWidth=1);
        else:
            plt.plot(sh, colors[n], LineWidth=2);

            
    promNormal = [val/10  for val in promNormal];
    plt.plot(promNormal, "m", LineWidth=1);
    
    promAislamiento = [val/10  for val in promAislamiento];
    plt.plot(promAislamiento, "m", LineWidth=2);
    
    plt.title(personas[per]);
    plt.ylabel("Shimer del audio");
    plt.xlabel("Número de trama");
    plt.legend(nombres, loc='lower right');
    plt.hold("off");
    
    #guardar figura en formato png
    plt.savefig(figureName+".png", dpi=100);
    #print(handleFig, 'PY'+figureName,'-dpng');
    #plt.plotfile(handleFig,'PY'+figureName);

