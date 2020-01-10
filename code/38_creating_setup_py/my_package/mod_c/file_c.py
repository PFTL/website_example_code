from ..mod_a.file_a import  function_a
from my_package.mod_b.file_b import function_b

def function_c():
    print('This is function c')
    function_a()
    function_b()