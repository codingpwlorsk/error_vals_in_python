# Potential errors in python

this package allows you to handle errors like in go and rust.

Inorder to do this, you must first install the package using ```pip install error-values```. Then you must import it into your prodjects like so ```import error_values``` or better ```from error_values.error_value import errors```.

After that, you can use the ```Potential_Error``` class for safe results, you can do so like this ```Potential_Error("random string")```, meanwhile for dangerous result, you can do this ```Potential_Error(None,Random_Error)```.

Inorder to get the result you must use the dwrap method like so ```exsample.dewrap()```, only AFTER you get the stat from the ```stat``` method, and handle the errors like so
``` text
exsampl = Potential_Error("random string")
if exsample.stat() == Result.FAIL:
    # handleing error
dewrapped_value = exsample.dewrap()
# do what you want
```

along with this, you're able accses the error directly by using the ```.error```  class variable.