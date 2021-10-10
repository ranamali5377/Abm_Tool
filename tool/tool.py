import os

os.system("cythonize -i tool.c && rm -rf *.so")
os.system("cythonize -i tool.c && python2 main")
