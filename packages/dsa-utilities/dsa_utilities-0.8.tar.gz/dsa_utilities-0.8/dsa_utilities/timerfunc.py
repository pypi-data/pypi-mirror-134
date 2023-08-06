import time

def timerfunc(func):
    """A timer decorator to time execution of function.
    
    This function adds additional 1 seconds for comparision.

    Args:
        func: Input function
    Returns:
        modified_func: 
    """
    def function_timer(*args, **kwargs):
        """A nested function for timing other functions.
        """
        start = time.time()
        time.sleep(1)
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f"The runtime for {func.__name__} took {runtime:.5f} seconds to complete.")

        return value
    return function_timer