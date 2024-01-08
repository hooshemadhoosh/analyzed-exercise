from pyhtml2pdf import converter
from sympy import true
source = r'D:\Projects\analyzed-exercise\sport-program-build-new-version\newFile0.html'
target = 'index.pdf'
converter.convert(source,target,timeout=1,compress=true,power=0)