import colorlog
import logging
from sys import stdout

#  Logger settings

logger = logging.getLogger('')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('task.log')
sh = logging.StreamHandler(stdout)
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s [%(asctime)s] %(levelname)s  %(message)s', datefmt='%a, %d %b %Y %H:%M:%S'))
logger.addHandler(fh)
logger.addHandler(sh)
logger.info("\n")


class Utils:
    """
    Class for utility functions for editing Tag for music
    """

    def __init__(self):
        """
        Constructor for Utils class
        """

    def log_msg(self, msg):
        logger.info(msg)

    def log_error(self, msg, fatal=False):
        if fatal:
            logger.error(
                "| Fatal Error: Application Terminated, error: " + msg)
            exit()
        else:
            logger.error(msg)

    def log_warning(self, msg):
        logger.warning(msg)

    # Terminal app Design Utils

    def print_banner(self):
        banner = """
        
        iAssets 

        - By A29\n"""
        print(banner)

    def break_line(self, spacing=0):
        print("-"*45)
        for _ in range(spacing):
            print("\n")

    def better_exit(reason="quit (y/n): ", on_yes="Starting the process", on_no="Bye"):
        ask = input(reason)
        exit(f"\n{on_no}") if ask.lower() == "n" else print(on_yes)


#  TESTING

def test():
    utils = Utils()
    print("TESTING")
    utils.print_banner()


if __name__ == "__main__":
    test()
