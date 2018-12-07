import re, json, sys

def get_project_lines(path):
  with open(path) as f:
    text = f.read()
  return text.splitlines()

def main():
  jobs = []
  line_iter = iter(get_project_lines(sys.argv[-1]))
  while True:
    try:
      jobs.append(Job(line_iter))
    except StopIteration:
      break
  print(json.dumps([job.__dict__ for job in jobs], indent=2))

class Job:
  def __init__(self, line_iter):
    '''
    title                #  Full-stack Team Desired for Mobile, Web, & Liferay Portal Development
    time_money           #  Hourly - Expert ($$$) - Est. Time: More than 3 months, Less than 10 hrs/week - Posted 6 minutes ago
    note                 #   Only freelancers located in the United States may apply.
    project_description  #  We are a small but growing assessment and consulting company in US. Our current development needs include: * Mobile App (we have wireframes, etc); * Web Launch w/some editing (all content written, most has been laid out in NOVI responsive template ... more
    tags                 #  HTML5 Liferay Mobile App Development Responsive Web Design Website Development  1 more
    proposals            #  Proposals: Less than 5
    payment_info         #  Payment verified   $70k+ spent   United States
    '''

    self.title = next(line_iter)
    self.has_special_tag = False
    split = self.title.split()
    if len(split) > 1 and split[1] == 'JOB':
      self.has_special_tag = True
      self.title = next(line_iter)
    self.time_money = next(line_iter)
    self.note = next(line_iter)
    self.project_description = next(line_iter)
    next_line = next(line_iter)
    if next_line.startswith('Proposals'):
      self.tags = ''
      self.proposals = next_line
    else:
      self.tags = next_line
      self.proposals = next(line_iter)
    self.payment_info = next(line_iter)

    # while True:
    #   next_line = next(line_iter)
    #   if is_review(next_line):
    #     self.review += next_line
    #   else:
    #     break
    # self.freelancer_response = None
    # if next_line.startswith("Freelancer's Response"):
    #   self.freelancer_response = next(line_iter)
    #   self.dollar_amount = next(line_iter)
    # else:
    #   self.dollar_amount = next_line
    # self.hourly_or_fixed = next(line_iter)
    # self.hours = None
    # if self.hourly_or_fixed.endswith('/ hr'):
    #   self.hours = next(line_iter)

def is_review(line):
  if line.startswith("Freelancer's Response"):
    return False
  if line.startswith('$'):
    return False
  return True

if __name__ == '__main__':
  main()
