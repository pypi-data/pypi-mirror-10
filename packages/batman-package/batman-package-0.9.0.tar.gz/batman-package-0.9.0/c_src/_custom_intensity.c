#include <math.h>

/*
	- The intensity function returns the stellar intensity at a radius r; where 0 <= r <= 1
	- The function arguments are the normalized radius (r), and limb darkening coefficients u1, ..., un
	- see below for an example intensity profile for I(r) \propto 1 - u1*(1-sqrt(1-r^2)) - u2*ln((sqrt(1-r^2)+c)/(1+c))
	- The normalization constant is calculated by constraining the integrated intensity to equal 1:
		\int_r \int_theta {I(r)*r*dr*dtheta}/norm = 1
*/

double intensity(double r, double u1, double u2, double u3, double u4, double u5, double u6) 
{
	if(r > 0.99995) r = 0.99995;
	double mu = sqrt(1.-r*r);
	double norm = 2.*M_PI*(-u1/6. - u2*u3/2. + u2/4. + 0.5 + u2*u3*u3*log(1. + 1./u3)/2.); 
	return (1. - u1*(1. - mu) - u2*log((mu+u3)/(1.+u3)))/norm;
}
