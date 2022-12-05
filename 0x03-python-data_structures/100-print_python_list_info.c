#include <stdlib.h>
#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints information about a list in python
 * @p: python list argument passed to the function as type PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	long int size_of_list, idx;
	PyListObject *listobj;
	ssize_t memory_alloc;

	/**
	 * PyObject *p casted to PyListObject
	 * see https://github.com/python/cpython/blob/main/Include/object.h
	 * for documentation
	 */
	listobj = (PyListObject *)p;

	/* returns and prints the size of the list */
	size_of_list = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size_of_list);
	/**
	 * allocated memory: returns type Py_ssize_t of struct member allocated
	 * The code used was obtained at:
	 * https://github.com/python/cpython/blob/main/Include/cpython/listobject.h
	 * Py_ssize_t is a long signed int
	 */
	memory_alloc = listobj->allocated;
	printf("[*] Allocated = %ld\n", memory_alloc);
	/**
	 * see "https://docs.python.org/3/c-api/typeobj.html" for reference
	 * on Type objects: tp_name => Pointer to a NUL-terminated string containing
	 * the name of the type; const char *PyTypeObject.tp_name
	 */
	for (idx = 0; idx < size_of_list; idx++)
	{
		item = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(item)->tp_name);
	}
}
