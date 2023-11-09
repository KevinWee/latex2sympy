import sys
import getopt
import traceback
import sympy
from latex2sympy2 import latex2sympy, variances, latex

def usage():
    print('-h: --help 帮助;')
    print('--latex=LaTeX表达式 获取表达式计算结果;')
    print('--logical=LaTeX表达式 获取表达式真值;')

def numerical(tex):
    try:
        result = latex(sympy.simplify(latex2sympy(tex).subs(variances).doit().doit()).evalf(subs=variances))
        print(result)
    except Exception as e:
        print("请检查表达式", str(e))
        # 打印完整的异常信息
        traceback.print_exc()
        sys.exit()

def logical(tex):
    try:
        result = sympy.simplify(latex2sympy(tex).subs(variances).doit().doit())
        print(result)
    except Exception as e:
        print("请检查条件表达式是否正确", str(e))
        # 打印完整的异常信息
        traceback.print_exc()
        sys.exit()

def start(argv):
    if len(argv)<1:
        print("-h 获取帮助信息")
        sys.exit()
    opts, argvs = getopt.getopt(argv, '-h', ["latex=", "logical="])

    for opt,arg in opts:
        if opt == "-h":
            usage()
        elif opt == "--latex":
            numerical(arg)
        elif opt == "--logical":
            logical(arg)

if __name__ == '__main__':
    start(sys.argv[1:])