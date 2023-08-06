#include <stdio.h>
#include <string.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>

typedef void (*rhs_t)(int *n, double *x, double *y, double *f, float *rpar, int *ipar);
typedef void (*jac_t)(int *n, double *x, double *y, double *dfy, int *ldfy, float *rpar, int *ipar);
typedef void (*mas_t)(int *n, double *am, int *lmas, float *rpar, int *ipar);
typedef void (*sol_t)(int *nr, double *xold, double *x, double *y, int *cont, int *lrc, int *n,
		float *rpar, int *ipar, int *irtrn);

#ifdef __cplusplus
extern "C" {
#endif
	// Signature of Fortran RADAU function
	void radau_(
		int    *N,       // Dimension
		rhs_t   FCN,     // RHS function
		double *X,       // Initial time
		double *Y,       // Initial y array
		double *XEND,    // Final integration time
		double *H,       // Initial step size
		double *RTOL,    // Tolerances
		double *ATOL,    //
		int    *ITOL,    // Whether rtol and atol are vector valued
		jac_t   JAC ,    // Jacobian function
		int    *IJAC,    // Whether to use JAC (1) or finite differences
		int    *MLJAC,   // Band-width of the jacobian. N for full.
		int    *MUJAC,   // Upper band-width (0 is MLJAC == N)
		mas_t   MAS ,    // Mass matrix function
		int    *IMAS,    // Whether to use the mass matrix function
		int    *MLMAS,   // Band-width of the mass matrix
		int    *MUMAS,   // Upper band-widh of the mass matrix
		sol_t   SOLOUT,  // Dense output function
		int    *IOUT,    // Wether to call the dense output function
		double *WORK,    // Temporary array of size LWORK
		int    *LWORK,   // N*(LJAC+LMAS+7*N+3*NSMAX+3)+20
		int    *IWORK,   // Temporary array of size LIWORK
		int    *LIWORK,  // (2+(NSMAX-1)/2)*N+20
		float  *RPAR,    // User-supplied RHS arguments
		int    *IPAR,    // See RPAR
		int    *IDID     // Return value
						 //  IDID= 1  COMPUTATION SUCCESSFUL,
						 //  IDID= 2  COMPUT. SUCCESSFUL (INTERRUPTED BY SOLOUT)
						 //  IDID=-1  INPUT IS NOT CONSISTENT,
						 //  IDID=-2  LARGER NMAX IS NEEDED,
						 //  IDID=-3  STEP SIZE BECOMES TOO SMALL,
						 //  IDID=-4  MATRIX IS REPEATEDLY SINGULAR.
	);
#ifdef __cplusplus
}
#endif

struct radau_options {
	PyObject *dense_callback;
	PyObject *rhs_fn;
	PyArrayObject *y_out;
};

static void radau_rhs(int *n, double *x, double *y, double *f, float *rpar, int *ipar) {
	struct radau_options *options = (struct radau_options *)ipar;

	PyObject *y_current = PyArray_SimpleNewFromData(PyArray_NDIM(options->y_out), PyArray_DIMS(options->y_out), NPY_DOUBLE, y);
	PyObject *rhs_retval = PyObject_CallFunction(options->rhs_fn, "dO", *x, y_current);
	Py_DECREF(y_current);

	if(rhs_retval == NULL) return;
	PyArrayObject *rv_array = (PyArrayObject *)PyArray_FROM_OTF(rhs_retval, NPY_DOUBLE, NPY_ARRAY_IN_ARRAY);
	if(rv_array == NULL) return;
	int use_n = PyArray_SIZE(rv_array);
	if(use_n >= *n) use_n = *n;
	memcpy(f, (double *)PyArray_DATA(rv_array), use_n * sizeof(double));
	Py_DECREF(rv_array);
	Py_DECREF(rhs_retval);
}

static void radau_dense_feedback(int *nr, double *xold, double *x, double *y, int *cont, int *lrc, int *n, float *rpar, int *ipar, int *irtrn) {
	struct radau_options *options = (struct radau_options *)ipar;

	PyObject *y_current = PyArray_SimpleNewFromData(PyArray_NDIM(options->y_out), PyArray_DIMS(options->y_out), NPY_DOUBLE, y);
	if(y_current == NULL) return;
	PyObject *y_copy = (PyObject *)PyArray_Copy((PyArrayObject *)y_current);
	if(y_copy == NULL) return;
	PyObject *rhs_retval = PyObject_CallFunction(options->dense_callback, "dO", *x, y_copy);
	Py_DECREF(y_copy);
	Py_DECREF(y_current);

	if(PyObject_IsTrue(rhs_retval)) {
		*irtrn = -1;
	}
	else {
		*irtrn = 1;
	}
	Py_DECREF(rhs_retval);
}

static PyObject *radau13(PyObject *self, PyObject *args, PyObject *kwargs) {
	// Parse arguments
	static char *kwlist[] = {"rhs_fn", "y0", "t_final", "order", "max_steps", "dense_callback", "t0", "h0", "abstol", "reltol", "max_stepsize", NULL};
	PyObject *rhs_fn, *y0, *dense_callback = NULL;
	double t_final, t_0 = 0., h_0 = 1e-6, abstol = 1e-13, reltol = 1e-9, max_stepsize = 0.;
	int order = 13.;
	unsigned int max_steps = 10000;

	if(!PyArg_ParseTupleAndKeywords(args, kwargs, "OOd|iIOddddd", kwlist, &rhs_fn, &y0, &t_final, &order, &max_steps, &dense_callback, &t_0, &h_0, &abstol, &reltol, &max_stepsize)) return NULL;
	PyArrayObject *y0_array = (PyArrayObject *)PyArray_FROM_OTF(y0, NPY_DOUBLE,  NPY_ARRAY_IN_ARRAY | NPY_ARRAY_C_CONTIGUOUS);
	if(!y0_array) {
		PyErr_SetString(PyExc_ValueError, "y0 must be convertible to a numpy array");
		return NULL;
	}
	if(!PyCallable_Check(rhs_fn)) {
		PyErr_SetString(PyExc_ValueError, "rhs_fn must be callable");
		return NULL;
	}
	if(dense_callback != NULL && !PyCallable_Check(dense_callback)) {
		PyErr_SetString(PyExc_ValueError, "dense_callback, if set, must be callable");
		return NULL;
	}
	if(order != 13 && order != 5 && order != 9) {
		PyErr_SetString(PyExc_ValueError, "Only orders 13, 9 and 5 are implemented.");
		return NULL;
	}

	// Prepare memory for RADAU
	int n = PyArray_SIZE(y0_array);
	PyArrayObject *y_out = (PyArrayObject *)PyArray_Copy(y0_array); // PyArray_FromArray(y0_array, PyArray_DESCR(y0_array), NPY_ARRAY_WRITEABLE | NPY_ARRAY_ENSURECOPY);
	struct radau_options options = { dense_callback, rhs_fn, y_out };
	int lwork  = n * (n + 7*n + 3*7 + 3) + 20;
	int liwork = (2 + (7 - 1) / 2) * n + 20;
	double *work = calloc(lwork, sizeof(double));
	int *iwork = calloc(lwork, sizeof(int));
	int no[] = { 0, 0, 0, 0 };
	int nc[] = { n, n, n };
	int bw[] = { 0, 0 };
	int yes = 1;
	int idid = 0;

	iwork[0] = 1;                          // Use Hessenberg matrix form
	iwork[1] = max_steps;                  // Increase maximum number of steps
	iwork[12] = (order + 1) / 2;           // Start off with given order
	work[2] = 0.01;                        // Recompute Jacobian less often (default 0.001)
	work[6] = max_stepsize;                // Maximal step size

	// Call RADAU
	radau_(
		&nc[0],                            // Dimension
		radau_rhs,                         // RHS function
		&t_0,                              // Initial time
		PyArray_DATA(y_out),               // Initial y array and output
		&t_final,                          // Final integration time
		&h_0,                              // Initial step size
		&reltol,                           // Tolerances
		&abstol,                           //
		&no[0],                            // Whether rtol and atol are vector valued
		NULL,                              // Jacobian function
		&no[1],                            // Whether to use JAC (1) or finite differences
		&nc[1],                            // Band-width of the jacobian. N for full.
		&bw[0],                            // Upper band-width (0 is MLJAC == N)
		NULL,                              // Mass matrix function
		&no[2],                            // Whether to use the mass matrix function
		&nc[2],                            // Band-width of the mass matrix
		&bw[1],                            // Upper band-widh of the mass matrix
		radau_dense_feedback,              // Dense output function
		dense_callback ? &yes : &no[3],    // Wether to call the dense output function
		&work[0],                          // Temporary array of size LWORK
		&lwork,                            // N*(LJAC+LMAS+7*N+3*NSMAX+3)+20
		&iwork[0],                         // Temporary array of size LIWORK
		&liwork,                           // (2+(NSMAX-1)/2)*N+20
		NULL,                              // User-supplied RHS arguments
		(int*)&options,                    // See RPAR
		&idid                              // Return value
						                   // IDID= 1  COMPUTATION SUCCESSFUL,
						                   // IDID= 2  COMPUT. SUCCESSFUL (INTERRUPTED BY SOLOUT)
						                   // IDID=-1  INPUT IS NOT CONSISTENT,
						                   // IDID=-2  LARGER NMAX IS NEEDED,
						                   // IDID=-3  STEP SIZE BECOMES TOO SMALL,
						                   // IDID=-4  MATRIX IS REPEATEDLY SINGULAR.
	);

	free(work);
	free(iwork);
	Py_DECREF(y0_array);

	if(idid != 1 || y_out == NULL) {
		char err[30];
		sprintf(err, "radau failed with idid = %d", idid);
		PyErr_SetString(PyExc_RuntimeError, err);
		Py_DECREF(y_out);
		return NULL;
	}

	return Py_BuildValue("O", y_out);
}

static PyMethodDef methods[] = {
	{"radau13", (PyCFunction)radau13, METH_VARARGS | METH_KEYWORDS,
		"radau13 - Solve ODE system using the radau13 integrator\n\n"
		"Syntax: radau13(rhs_fn, y0, t_final, order=13, max_steps=10000,\n"
		"                dense_callback=None, t0=0, h0=1e-6, abstol=1e-13,\n"
		"                reltol=1e-9, max_stepsize=0)\n\n"
		" Parameters:\n"
		" - rhs_fn must be a callable of the type rhs_fn(t, y), where\n"
		"     t is the current integration time, and\n"
		"     y is the current state vector.\n"
		"     it should return a vector df/dt.\n\n"
		" - y0 must be the initial state vector.\n"
		" - t_final must be the desired new time level\n"
		" - order must be one of 13, 9 or 5.\n"
		" - max_steps denotes the maximal step count to take.\n"
		" - dense_callback must be either not set, or a callable of the\n"
		"     type dense_callback(t, y). It is called after each internal\n"
		"     integration step.\n"
		"     If dense_callback returns a value that evaluates to True, integration\n"
		"     is halted.\n"
		" - t0 denotes the initial time.\n"
		" - h0 denotes the initial step size.\n"
		" - abstol/reltol denote the integrator tolerances\n"
		" - max_stepsize denotes the maximal step size. It is only required\n"
		"     if you need fixed times in dense_callback; for normal operation\n"
		"     abstol/reltol are fine.\n\n"
		" The function returns the state at time t_final, or throws a\n"
		" RuntimeError if it vails. The runtime error contains the error message\n"
		" from RADAU13, which can be\n"
		"   IDID= 1  COMPUTATION SUCCESSFUL,\n"
		"   IDID= 2  COMPUT. SUCCESSFUL (INTERRUPTED BY SOLOUT)\n"
		"   IDID=-1  INPUT IS NOT CONSISTENT,\n"
		"   IDID=-2  LARGER NMAX IS NEEDED,\n"
		"   IDID=-3  STEP SIZE BECOMES TOO SMALL,\n"
		"   IDID=-4  MATRIX IS REPEATEDLY SINGULAR.\n"
	},
	{NULL, NULL}
};

PyMODINIT_FUNC initpyradau13(void) {
   (void)Py_InitModule("pyradau13", methods);
   import_array();
}
