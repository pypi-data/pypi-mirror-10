quickstartlog
=============

A simple log utility, write log into console & file(TimedRotatingFileHandler)

Examples
--------

main.py::

    import quickstartlog as qslog

    qslog.info('this is info message')
    qslog.warn('this is warning message')
    qslog.error('this is error message')
    
console output & ./var/log/main.log::
    
    [10:13:44 INFO ] this is info message
    [10:13:44 WARNI] this is warning message
    [10:13:44 ERROR] this is error message