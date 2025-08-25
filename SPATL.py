import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cmath
import warnings
warnings.filterwarnings("ignore")

Type= float(input("Enter the length of transmission line (km): "))
if Type<80:
    print("This is a Short Transmission line")
elif 80<=Type<250:
    print("This is a Medium Transmission line")
else :
    print("This is a Long Transmission line")
    

#input value
Vr=float(input("Enter the recieving end voltage(v): ")) #recieving end voltage in volts
p= float(input("Enter the load power(W): ")) #load power in watts
pf= float(input("Enter the power factor(lagging): ")) #power factor lagging
R= float(input("Enter the resistance per km(ohm): ")) #resistance per km
X= float(input("Enter the reactance per km(ohm): ")) #reactance per km
length= float(input("Enter the length in km: "))#line length in km

def short_line():
    V_base=Vr / np.sqrt(3) #convert line voltage into phase voltage

    #calculations
    Z= complex(R*length,X*length) #total series impedance
    Ir_mag= p/(np.sqrt(3)*Vr*pf) #current magnitude
    phi = np.arccos(pf) #phase angle in radians
    Ir= Ir_mag*(np.cos(-phi)+ 1j*np.sin(-phi)) #complex load current


    #sending end voltage (short line model)
    Vs= V_base + Ir*Z #sending end phase voltage
    Vs_line= abs(Vs)*np.sqrt(3)    
    
    #voltage regulation and efficiency
    VR= ((Vs_line-Vr)/Vr)*100
    losses= 3*abs(Ir)**2*abs(Z) #3-phase loss
    p_out = p
    p_in= p_out + losses
    efficiency= (p_out/p_in)*100

    #results
    print("\n--- SHORT TRANSMISSION LINE RESULTS---")
    print("sending end voltage (line): {:.2f}kV".format(Vs_line/1000))
    print("voltage Regulation: {:.2f}%".format(VR))
    print("Transmission Efficiency: {:.2f}%".format(efficiency))

    #plotting voltage profilr along line
    x=np.linspace(0,length,100)
    voltage_profile=[]

    for d in x:
        Z_d= complex(R*d,X*d)
        Vd= V_base +Ir*Z_d
        voltage_profile.append(abs(Vd))
    #graph   
    plt.figure(figsize=(8,5))
    plt.plot(x,voltage_profile,label='voltage(phase)',color='blue')
    plt.xlabel('Distance along line (km)')
    plt.ylabel('Voltage(V)')
    plt.title('Voltage profile along short Transmission line')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    #bar graph
    parameters=['voltage Regulation %','Efficiency %']
    values=[VR,efficiency]
    plt.figure(figsize=(10,5))
    plt.bar(parameters,values,color=['orange','green'])
    plt.title("SHORT TRANSMISSION LINE")
    plt.ylabel('value')
    plt.grid(False)
    plt.show()

    #line chart
    plt.figure(figsize=(10,5))
    plt.plot(x,np.array(voltage_profile)/1000,color='pink',marker='o') #convert v into kv
    plt.title('VOLTAGE PROFILE ALONG SHORT TRANSMISSION LINE')
    plt.xlabel('Distance from sending end voltage')
    plt.ylabel('voltage(kv)')
    plt.grid(True)
    plt.show()

    
def medium_line():
    C= float(input("Enter the capacitance per km(F): "))#capacitance per km
    f=float(input("Enter the frequency in Hz: "))#frequency in Hz
    
    V_base=Vr / np.sqrt(3) #convert line voltage into phase voltage

    #calculations
    Z= complex(R*length,X*length) #total series impedance
    Y= complex(0,2*np.pi*f*C*length) #total shunt admittance
    Ir_mag= p/(np.sqrt(3)*Vr*pf) #current magnitude
    phi = np.arccos(pf) #phase angle in radians
    Ir= Ir_mag*(np.cos(-phi)+ 1j*np.sin(-phi)) #complex load current
    Ic=(Y*V_base)/2 #half of shunt current
    Is=Ir+Ic #sending end current


    #sending end voltage (short line model)
    Vs= V_base + Ir*Z +Ic*Z #sending end phase voltage
    Vs_line= abs(Vs)*np.sqrt(3)    
    
    #voltage regulation and efficiency
    VR= ((Vs_line-Vr)/Vr)*100
    losses= 3*abs(Ir)**2*abs(Z) #3-phase loss
    p_out = p
    p_in= p_out + losses
    efficiency= (p_out/p_in)*100

    #results
    print("\n--- MEDIUM TRANSMISSION LINE RESULTS---")
    print("sending end voltage (line): {:.2f}kV".format(Vs_line/1000))
    print("voltage Regulation: {:.2f}%".format(VR))
    print("Transmission Efficiency: {:.2f}%".format(efficiency))

    #plotting voltage profilr along line
    x=np.linspace(0,length,100)
    voltage_profile=[]

    for d in x:
        Z_d= complex(R*d,X*d)
        Vd= V_base +Ir*Z_d
        voltage_profile.append(abs(Vd))
     #graph   
    plt.figure(figsize=(8,5))
    plt.plot(x,voltage_profile,label='voltage(phase)',color='green')
    plt.xlabel('Distance along line (km)')
    plt.ylabel('Voltage(V)')
    plt.title('Voltage profile along Medium Transmission line')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    #bar graph
    parameters=['voltage Regulation %','Efficiency %']
    values=[VR,efficiency]
    plt.figure(figsize=(10,5))
    plt.bar(parameters,values,color=['orange','green'])
    plt.title("MEDIUM TRANSMISSION LINE")
    plt.ylabel('value')
    plt.grid(False)
    plt.show()

    #line chart
    plt.figure(figsize=(10,5))
    plt.plot(x,np.array(voltage_profile)/1000,color='pink',marker='o') #convert v into kv
    plt.title('VOLTAGE PROFILE ALONG MEDIUM TRANSMISSION LINE')
    plt.xlabel('Distance from sending end voltage')
    plt.ylabel('voltage(kv)')
    plt.grid(True)
    plt.show()

def long_line():
    C= float(input("Enter the capacitance per km(F): "))#capacitance per km
    f=float(input("Enter the frequency in Hz: "))#frequency in Hz
    L= float(input("Enter the inductance per km (H/km): "))
    G= float(input("Enter the conductance per km(s/km):"))
    #calculations
    w=2*np.pi*f #angular frequency

    z=R+1j*w*L #serries impedance
    y=G+1j*w*C #shunt admittance

    gamma=np.sqrt(z*y)
    Zc=np.sqrt(z/y)

    #ABCD parameters
    A=np.cosh(gamma*length)
    D=A
    B=Zc*np.sinh(gamma*length)
    C_=(1/Zc)*np.sinh(gamma*length)

    #receiving end current
    Ir=p/(Vr*pf) #magnitude
    phi=np.arccos(pf) #power factor angle
    Ir_complex=Ir*(np.cos(-phi) + 1j*np.sin(-phi))

    #sending end voltage and current
    Vs=A*Vr + B*Ir_complex
    Is=C_*Vr + D*Ir_complex

    #voltage regulation and efficiency
    VR_percent = ((abs(Vs) -Vr)/Vr)*100
    efficiency = (p/(abs(Vs)*abs(Is)))*100

    #output
    print("\n--- LONG TRANSMISSION LINE RESULTS---")
    print(f"A= {A}")
    print(f"B= {B}")
    print(f"C= {C_}")
    print(f"D= {D}")
    print(f"sending end voltage = {abs(Vs):.2f} v")
    print(f"sending end current = {abs(Is):.2f} A")
    print(f"voltage regulation = {VR_percent:.2f} %")
    print(f"Transmission Efficiency = {efficiency:.2f} %")

    #voltage profile
    x=np.linspace(0,length,100)
    voltage_profile=[]
    for d in x:
        Ad = np.cosh(gamma*d)
        Bd=Zc*np.sinh(gamma*d)
        Vd=Ad*Vr + Bd*Ir_complex
        voltage_profile.append(abs(Vd))
    #graph
    plt.figure(figsize=(8,5))
    plt.plot(x,voltage_profile,label='voltage magnitude(V)',color='red')
    plt.xlabel('Distance along line(Km)')
    plt.ylabel('voltage(V)')
    plt.title('Voltage profile along Long Transmission line')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show

    
    #bar graph
    parameters=['voltage Regulation %','Efficiency %']
    values=[VR_percent,efficiency]
    plt.figure(figsize=(10,5))
    plt.bar(parameters,values,color=['orange','green'])
    plt.title("LONG TRANSMISSION LINE")
    plt.ylabel('value')
    plt.grid(False)
    plt.show()

    #line chart
    plt.figure(figsize=(10,5))
    plt.plot(x,np.array(voltage_profile)/1000,color='pink',marker='o') #convert v into kv
    plt.title('VOLTAGE PROFILE ALONG LONG TRANSMISSION LINE')
    plt.xlabel('Distance from sending end voltage')
    plt.ylabel('voltage(kv)')
    plt.grid(True)
    plt.show()
    
    
#condition
if 80>= length:
    short_line()
elif 80<length<250:
    medium_line()
else:
    long_line()
