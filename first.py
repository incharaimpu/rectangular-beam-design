import math
from cmath import sqrt
b =float(input('Enter support width for beam (in m):'))
L =float(input('Enter the span of the beam (in m):'))
B=float (input('Enter the width of beam (in m)B:'))
LL= float(input(' Enter live load on the beam (in kN/m):'))
fck = float(input('Enter grade of concrete:'))
fy = float(input('Enter grade of steel:'))
d1=float(L/12)
d2=float(L/15)
print ('the depth of beam d1',d1)
print ('the depth of beam d2',d2)
d=d1
if d < d1:
 print ('the depth of the beam d','<',d1)
else: d = d2
print ('the depth of the beam d','=', d2)
D = d+.050
print ('the effective depth of the beam D', '=', D)
Ef = L + b
print ('the centre to centre supports', Ef)
cl = L + d
print ('the clear span + d cl=' , cl)
print ('effective span is Ef=', Ef)
selfwt = B*D*1*25
print ('the self wt of the beam is(in kN/m)', selfwt)
Wu = (1.5*LL)+(1.5*selfwt)
print ('the factored load Wu','=',Wu)
Mu = (Wu*Ef*Ef)/8
print ('Mu','=',Mu)
Vu = (1/2)*(Wu*Ef)
print ('Vu','=',Vu)
Xulim = float(0.48*d)
print ('Xulim','=',Xulim)
Mulim = float(0.36*fck*B*Xulim*(d-0.42*Xulim))*1000
print ('Mu','=',Mu)
print ('Mulim','=',Mulim)
M = Mulim
if M > Mulim :
  print('M','>', Mulim)
else: M = Mu
print ('the section can be designed as singly reinforced Mulim > Mu')
Ast1 = ((fy/(b*d*fck))+(sqrt((((fy/(b*d*fck))*(fy/(b*d*fck)))-(4*1*(fy/(b*d*fck))*(Mu/(0.87*fy*d)))))))/(2*1)
print ('area of steel is  Ast1', Ast1)
(D1)= float(input('Enter support dia of bars (in mm):'))
nb = float(input('no.of bars :'))
Ast2 = nb * ((3.1429 * (D1) * (D1) /4))
print('area of steel provided is  Ast2', Ast2)
tv = (Vu*1000) /( B * d)
Pt = (100 * Ast2) / (B * d)
print('tv (in N/mm^2)', tv)
print('Pt (in N/mm^2)', Pt)
Tc = float(input('Enter Tc value by seeing IS 456 in 19 (in N/mm^2):'))
Tcmax = 2.8
print ('Tcmax value by seeing IS 456 in 20 (in N/mm^2)  2.8 ',Tcmax)
Tc = tv = Tcmax
Tc < tv < Tcmax
print('Tc < tv < Tcmax=',Tc < tv < Tcmax)
Vc=(Tc*B*d)
print('shear force is Vc=',Vc)
Vus=Vu-Vc
print ('shear to resisted by reinforcement Vus=',Vus)
D2=float(input('Enter support dia of bars (in mm):'))
nb1=float(input('no.of bars :'))
Asv=( nb1*( 3.1429/4) * D2 *D2 )
print('area of steel provided is  Asv', Asv)
Sv= (0.87*250*Asv * d) / Vus
print('the spacing is Sv', Sv)
print ('but max spacing permitted :')
Dmax = (0.75 * d)
print('max spacing is', Dmax)
print('check for deflection :')
x=(L/d)
print('check for deflection x:',x)
print('modification factor for tensile steel:')
fs=(0.58*fy*(Ast2/Ast1))
print('modification factor for tensile steel (N/mm)',fs)
F1=float(input('F1 :'))
F2=float(input('no.compressive steel from IS 456 fig.4 F2:'))
F3=float (input('not flanged section from IS 456 fig.4 F3:'))
Mp=F1*F2*F3*20
print('Mp:',Mp)
Ld=Ef/d
print('Ld',Ld)
print('thus Ld provide < Mp permitted')














