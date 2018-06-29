# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:26:57 2018

@author: Caelum.kamps
"""

import security_objects as so
import plotting as p
 
td = so.equity('TD', 76.0, 0.0391, 0, 65.0, 10)     
        
# Speficy Commission per stock ie broker commission/100
commission = 0.025
fixed = 0.2

# Speficy option objects
tdc = so.option(td, 'call', 'long', 77.5, 0.13, 7, 365, 0.5, 1)
tdp = so.option(td, 'put', 'long', 77.5, 0.13, 7, 365, 2, 1)

# Create a portfolio of options held
book = [tdc, tdp]

p.plot_value(book, 0.2)
p.plot_delta(book, 0.2)
p.plot_gamma(book, 0.2)
