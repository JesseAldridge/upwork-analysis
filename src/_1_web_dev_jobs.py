import json, collections, sys

def main():
  with open(sys.argv[-1]) as f:
    text = f.read()
  jobs = json.loads(text)
  for job in jobs:
    print(job['title'])

if __name__ == '__main__':
  main()
