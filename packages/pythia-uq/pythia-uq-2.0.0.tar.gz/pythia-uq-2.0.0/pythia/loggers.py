""" Logger class to write output to terminal and in log file. """
import sys
import os
import datetime


class Logger(object):
    """ Logger to write function output to terminal and in log file.

    Parameters
    ----------
    fileName : string, default='logfile.log'
        Name of the log file.
    filePath : string, default='./Log/'
        Path to the log file.

    Examples
    --------
    >>> sys.stdout = Logger(fileName, filePath)

    """

    def __init__(self, fileName='logfile.log', filePath='./Log/'):
        """ Initialize Logger object. """
        if not fileName[-4:] == '.log':
            now = datetime.datetime.now()
            fn = '{}_{}{:02}{:02}-{:02}{:02}{:02}.log'.format(
                fileName, now.year, now.month, now.day, now.hour,
                now.minute, now.second)
        else:
            fn = fileName
        print('Write LOG ({})'.format(filePath+fn))
        self.terminal = sys.stdout
        if not os.path.isdir(filePath):
            os.makedirs(filePath)
        self.log = open(filePath+fn, "a")

    def write(self, message):
        """ Write string to terminal and log file. """
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        """ Flush screen. """
        pass


def log_progress(sequence, every=None, size=None, name='Items'):
    """ Progress bar for jupyter notebooks.

    .. deprecated:: 2.0.0
        `log_progress` will be removed in PyThia 3.0.0 as this is not part
        of the PyThia core functionality.

    .. note::
        Code copied from https://github.com/alexanderkuk/log-progress
    """
    from ipywidgets import IntProgress, HTML, VBox
    from IPython.display import display

    is_iterator = False
    if size is None:
        try:
            size = len(sequence)
        except TypeError:
            is_iterator = True
    if size is not None:
        if every is None:
            if size <= 200:
                every = 1
            else:
                every = int(size / 200)     # every 0.5%
    else:
        assert every is not None, 'sequence is iterator, set every'

    if is_iterator:
        progress = IntProgress(min=0, max=1, value=1)
        progress.bar_style = 'info'
    else:
        progress = IntProgress(min=0, max=size, value=0)
    label = HTML()
    box = VBox(children=[label, progress])
    display(box)

    index = 0
    try:
        for index, record in enumerate(sequence, 1):
            if index == 1 or index % every == 0:
                if is_iterator:
                    label.value = '{name}: {index} / ?'.format(
                        name=name,
                        index=index
                    )
                else:
                    progress.value = index
                    label.value = u'{name}: {index} %'.format(
                        name=name,
                        index=int(100*index/size)
                    )
            yield record
    except:
        progress.bar_style = 'danger'
        raise
    else:
        progress.bar_style = 'success'
        progress.value = index
        label.value = "{name}: {index} %".format(
            name=name,
            index=str(int(100*index/size) or '?')
        )
