import subprocess

def run_pipeline(basename, all_tags):
  raw_text_path = '../data/{}.txt'.format(basename)
  json_path = '../data/{}.json'.format(basename)
  tag_rates_path = '../data/{}_rates.txt'.format(basename)
  cmd_list = ['python3', '_0_parse_jobs_feed.py', raw_text_path]
  out_str = subprocess.Popen(cmd_list, stdout=subprocess.PIPE).communicate()[0].decode('utf8')
  with open(json_path, 'w') as f:
    f.write(out_str)
  cmd_list = ['python3', '_1_parse_jobs_json.py', json_path]
  out_str = subprocess.Popen(cmd_list, stdout=subprocess.PIPE).communicate()[0].decode('utf8')
  with open(tag_rates_path, 'w') as f:
    f.write(out_str)
  all_tags.append(out_str.strip())

all_tags = []
for i in range(5):
  suffix = '' if i == 0 else (i + 1)
  run_pipeline('jobs_feed{}'.format(suffix), all_tags)

with open('../data/tag_rates_all.txt', 'w') as f:
  f.write('\n'.join(sorted(all_tags, key=lambda line: float(line.rsplit(' ', 1)[-1]))))

run_pipeline('web_dev_jobs', all_tags)
