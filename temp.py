from loguru import logger

logger.add('test.log')
logger.debug('this is a debug')
logger.info('this is a debug')

# import sys
# print('hello world!', file=sys.stderr)
# sys.stdout.write('hello world!\n')
