class AirTemp:
    value = None
    unit = None
    
    def set(value,unit):
        AirTemp.value = value
        AirTemp.unit = unit
        
    def get():
        return (AirTemp.value, AirTemp.unit)
    
    def ToKelvin():
        if AirTemp.unit == 'C':
            AirTemp.value = AirTemp.value + 273.15
            AirTemp.unit = 'K'
    def ToFahrenheit(): # HM1 -459.67 °F ... absolute zero temperature ... Fahrenheit = 20°C × 9/5 + 32 = 68 °F
        if AirTemp.unit == 'C':
            AirTemp.value = AirTemp.value * 1.8 + 32
            AirTemp.unit = 'F'
    
    def print():
        print(AirTemp.value, AirTemp.unit)
        
    
AirTemp.set(20,'C')
AirTemp.ToFahrenheit()
print(AirTemp.get())
        