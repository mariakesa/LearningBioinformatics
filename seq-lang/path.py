import sys
import os

print(os.path.join(os.path.dirname(sys.executable), 'lib', f'libpython{sys.version_info.major}.{sys.version_info.minor}m.so'))