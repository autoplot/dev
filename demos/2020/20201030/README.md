These are two methods for finding a zero crossing of a monotonic function.  The
first does a bisection search of a table, looking for where the tabulated function
crosses zero, and interpolates to find the result.  The second uses Apache Math's
univariate root finder to find a solution.
