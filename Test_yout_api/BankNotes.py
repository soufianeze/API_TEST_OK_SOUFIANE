# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    model_key: float 
    mileage: float 
    engine_power: float 
    fuel: float 
    paint_color: float 
    car_type: float 
    private_parking_available: float 
    has_gps: float 
    has_air_conditioning: float 
    automatic_car: float 
    has_getaround_connect: float 
    has_speed_regulator: float 
    winter_tires: float 