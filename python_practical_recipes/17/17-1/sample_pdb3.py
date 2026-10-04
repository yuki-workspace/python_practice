import sys
import ipdb

# 環境変数 PYTHONBREAKPOINT に "ipdb.set_trace()"をセット → breakpoint()で使える
sys.breakpointhook = ipdb.set_trace

def add(a,b):
  breakpoint()
  return a + b

def main():
  add(1,2)

if __name__ == "__main__":
  main()