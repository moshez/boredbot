if __name__ != '__main__':
    raise ImportError('module cannot be imported')

import sys
import mainland

mainland.main(
    root='boredbot',
    marker='BOREDBOT_MAIN_OK',
    argv=sys.argv,
)
