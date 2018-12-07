import re

def get_project_lines():
  with open('../data/arthur.txt') as f:
    text = f.read()

  lines = text.splitlines()
  for i, line in enumerate(lines):
    if line.startswith('Work history and feedback'):
      break
  return lines[i + 1:]

def main():
  jobs = []
  line_iter = iter(get_project_lines())
  while True:
    jobs.append(Job(line_iter))
    print('job:', jobs[-1].__dict__)

class Job:
  def __init__(self, line_iter):
    '''
    New Boho Site
    Nov 2018 - Present    # time range
    Job in progress       # review (possibly multiline)
    Freelancer's Response # optional response label
    foo bar               # optional response body
    $125.00               # dollar amount
    Fixed-price           # hourly or fixed
    22 hours              # if hourly, number of hours will appear here
    '''

    self.title = next(line_iter)
    self.time_period = next(line_iter)
    self.review = ''
    while True:
      next_line = next(line_iter)
      if is_review(next_line):
        self.review += next_line
      else:
        break
    self.freelancer_response = None
    if next_line.startswith("Freelancer's Response"):
      self.freelancer_response = next(line_iter)
      self.dollar_amount = next(line_iter)
    else:
      self.dollar_amount = next_line
    self.hourly_or_fixed = next(line_iter)
    self.hours = None
    if self.hourly_or_fixed.endswith('/ hr'):
      self.hours = next(line_iter)

def is_review(line):
  if line.startswith("Freelancer's Response"):
    return False
  if line.startswith('$'):
    return False
  return True

if __name__ == '__main__':
  main()
