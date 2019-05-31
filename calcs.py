# -*- coding: utf-8 -*-

import numpy as np

class CPTViz:

    def __init__(self, z=None, qc=None, fs=None, u2=None,
                    title='CPT01',  # CPT test number
                    gwl = 3.5,  # ground water level
                    soil_den = 18,  # soil density
                    max_depth = 30  # Maximum depth to display plots
                    ):

        # Hydrostatic water pressure
        u0 = [0]
        for i in np.arange(len(z)):
            if z[i] < gwl:
                u0.append(0)
            elif z[i] > gwl:
                u0.append((z[i] - gwl)*10)

        # U_delta
        self.udl = (u2 - u0)

        # Total Vertical Stress
        sig_vo = z * soil_den

        # Effective Vertical Stress
        sig1_vo = sig_vo - u0

        np.seterr(divide='ignore') # Ignore math errors

        # Friction Ratio
        Rf = (fs/qc) * 100

        # qt kPa
        qt = (qc * 1000) + (0.21 + u2)

        # net qc
        qn = qt - sig_vo

        # Pore pressure ratio
        self.Bq = self.udl / (qn)

        # qt MPa
        qtm = qt / 1000

        Su_15 = qn / 15 #Su Nkt = 15
        Su_15 = qn / 20 #Su Nkt = 20

        # normalised qc
        qt_norm = qn / sig1_vo

        # normalised fs
        fr_norm = ((fs * 1000) / qn) * 100

        # Soil Behaviour Type Index
        self.ic = np.sqrt(np.power(((3.47-(np.log10(qc/0.1)))),2) + np.power(((np.log10(Rf)+1.22)),2))

    @property
    def pore_pressure_ratio(self):
        return self.udl / (qn)

# def read_data_source():
#     Tk().withdraw()
#     file = askopenfilename(filetypes=[('EXCEL Files','*.xls')])
#     data_source = pd.read_excel(file,header=0,true_values=True)
#
#
# z  = data_source['SCPT_DPTH']        #Depth
# qc = data_source['SCPT_RES']          #Cone Resistance
# fs = data_source['SCPT_FRES']         #Sleeve Friction
# u2 = data_source['SCPT_PWP2']         #U2 pore pressure