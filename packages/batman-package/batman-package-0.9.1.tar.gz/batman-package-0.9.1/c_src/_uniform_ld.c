#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include "numpy/arrayobject.h"
#include <math.h>

#if defined (_OPENMP)
#  include <omp.h>
#endif

static PyObject *_uniform_ld(PyObject *self, PyObject *args)
{
	int nthreads;
	double z, p, kap0, kap1;

	PyArrayObject *zs, *flux;
	npy_intp i, dims[1];
	
  	if(!PyArg_ParseTuple(args,"Odi", &zs, &p, &nthreads)) return NULL;		//parses function input

	dims[0] = PyArray_DIMS(zs)[0]; 
	flux = (PyArrayObject *) PyArray_SimpleNew(1, dims, PyArray_TYPE(zs));	//creates numpy array to store return flux values
	
	double *f_array = PyArray_DATA(flux);
	double *z_array = PyArray_DATA(zs);

	if(fabs(p-0.5)<1.e-3) p = 0.5;

	#if defined (_OPENMP)
	omp_set_num_threads(nthreads);
	#endif

	#if defined (_OPENMP)
	#pragma omp parallel for private(z, kap1, kap0)
	#endif
	for(i=0; i<dims[0]; i++)
	{
		z = z_array[i]; 				// separation of centers
		
		if(z >= 1.+p) f_array[i] = 1.;			//no overlap
		if(p >= 1. && z <= p - 1.) f_array[i] = 0.;	//total eclipse of the star
		else if(z <= 1.-p) f_array[i] = 1.-p*p;		//planet is fully in transit
		else									//planet is crossing the limb
		{
			kap1=acos(fmin((1.-p*p+z*z)/2./z,1.));
			kap0=acos(fmin((p*p+z*z-1.)/2./p/z,1.));
			f_array[i] = 1. - (p*p*kap0+kap1 -0.5*sqrt(fmax(4.*z*z-pow(1.+z*z-p*p, 2.), 0.)))/M_PI;
		}
	}

	return PyArray_Return((PyArrayObject *)flux);
}


static char _uniform_ld_doc[] = "This extension module returns a limb darkened light curve for a uniform stellar intensity profile.";

static PyMethodDef _uniform_ld_methods[] = {
  {"_uniform_ld", _uniform_ld, METH_VARARGS, _uniform_ld_doc},{NULL}};

#if PY_MAJOR_VERSION >= 3
	static struct PyModuleDef _uniform_ld_module = {
		PyModuleDef_HEAD_INIT,
		"_uniform_ld",
		_uniform_ld_doc,
		-1, 
		_uniform_ld_methods
	};

	PyMODINIT_FUNC
	PyInit__uniform_ld(void)
	{
		PyObject* module = PyModule_Create(&_uniform_ld_module);
		if(!module)
		{
			return NULL;
		}
		import_array(); 
		return module;
	}
#else

	void init_uniform_ld(void)
	{
	  	Py_InitModule("_uniform_ld", _uniform_ld_methods);
		import_array(); 
	}
#endif

