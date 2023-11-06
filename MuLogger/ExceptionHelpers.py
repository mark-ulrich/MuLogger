import os
import sys


def get_clean_exception_message(e: Exception) -> str:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    if os.name == 'nt':
        filename = filename.split('\\')[-1]
    else:
        filename = filename.split('/')[-1]
    msg = f'{filename}:{exc_tb.tb_lineno} -- {exc_type} -- {str(e)}'
    return msg
