def iterate_list(lst, func):
    """Iterates through a list, with a global generator, optionally executing callable.
       User hits enter to go to the next value.
        
        parameters
        ---------
        
        lst: iterable
            the list to sort through
        func: callable
             callable executes using the  next element of the lst as its parameter
    
       global
       ------
       gen: iterator 
           global object which is the iterator of lst. If gen doesn't exist it is created.
      
       returns
       -------
           when execution is complete, if the user aborts or if invalid arguments are passed.
    """
    import collections
    gen = iter(lst)

    try:
        while 1 == 1:
            dummy = input(prompt="enter or q to quit")
            if dummy == 'q': return
            if func == None:
                return next(gen)
            else:
                try:
                    isinstance(func, collections.Callable)
                    func(next(gen))
                except TypeError:
                    "second argument needs to be a function "
                    return
    except StopIteration:
        print ("EOF")
        return