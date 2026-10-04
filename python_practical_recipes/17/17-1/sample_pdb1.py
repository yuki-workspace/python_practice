import sys

def get_system_imprementation():
  result = sys.implementation
  breakpoint()
  return result

def main():
  get_system_imprementation()

if __name__ == "__main__":
  main()
