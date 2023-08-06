quickstartlog
=============

A simple log utility, write log into console & file(TimedRotatingFileHandler)

Examples
--------

main.py::

    import quickstartlog as qslog
    qslog.debug('this is debug')
    qslog.info('this is info')
    qslog.warn('this is warning')
    qslog.error('this is error')
    qslog.info_ex(qslog.LIGHT_GREEN)('this is info with LIGHT_GREEN')
    
console output & ./var/log/main.log::

    [19:04:46 INFO ] this is info message
    [19:04:46 WARNI] this is warning message
    [19:04:46 ERROR] this is error message
    [19:04:46 INFO ] this is info message with LIGHT_GREEN