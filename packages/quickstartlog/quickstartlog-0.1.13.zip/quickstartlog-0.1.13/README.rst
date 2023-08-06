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

    [19:30:07 INFO ] this is info
    [19:30:07 WARNI] this is warning
    [19:30:07 ERROR] this is error
    [19:30:07 INFO ] this is info with LIGHT_GREEN