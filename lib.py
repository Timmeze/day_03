def is_creditable(age, salary):
    """
    >>> is_creditable(30,30_000)
    True

    """
    min_age = 20
    max_age = 60
    min_salary = 30_000
    if age < min_age:
        return False
    if age > max_age:
        return False
    if salary < min_salary:
        return False
    return True
    #if min_age < age < max_age and salary >= min_salary:
        #return True
    #else:
        #return False


