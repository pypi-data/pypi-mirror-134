from subprocess import Popen, PIPE as l
from pysimplelog import Logger

logger = Logger(__name__)
logger.set_log_file_basename('run_cmd')
logger.set_minimum_level(logger.logLevels['info'])


def run_cmd(cmd:str, split=False):
    
    '''
    run_cmd in python with out Popen
    '''
    
    debug_msg = f"""########
                  {cmd=}{type(cmd)=}
                  {split=}{type(split)=}"""
    logger.debug(debug_msg)
    
    out, err = Popen(cmd,shell=True,stdout=l).communicate()
    debug_msg = f"""What is {out=}?
                    What is {err=}?"""
    logger.debug(debug_msg)
    
    if err:
        error_msg = f"""There was an error:
                        {err}
                        """
        logger.error(error_msg, stack_info= True)
        raise OSError(err)
    return [o for o in out.decode().split('\n') if o] if split else out.decode()