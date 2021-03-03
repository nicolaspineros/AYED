import ecg
import numpy as np

path = "creado_ecg.xml"
leadName = "I"
volt = np.array([0.36,0.93])

example = ecg.ECG()
print("ECG object Created")
Lead = example.getLead(leadName)
Lead.setAmplitudValues(volt,"mV")
