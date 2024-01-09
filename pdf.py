from pyhtml2pdf import converter
from sympy import true

source = './sport-program-build-new-version/newFile0.html'
target = './index.pdf'
converter.convert(source,target,timeout=2,compress=True,power=3,install_driver=False)
