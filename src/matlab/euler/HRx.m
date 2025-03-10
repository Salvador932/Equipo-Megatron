 function  RHx=HRx(theta)
dato=whos('theta');
if strcmp(dato.class, 'sym') %variables simb�licas   
RHx=simplify([1,          0,           0, 0;
              0, cos(theta), -sin(theta), 0;
              0, sin(theta),  cos(theta), 0;
              0,          0,           0, 1],3);
else                
digits(3); %c�lculos num�ricos
     RHx=[1,       0,        0,      0;
    0,    cos(theta),   -sin(theta),   0;
    0,    sin(theta),   cos(theta),    0;
     0,        0,       0,      1];
end
 end
 