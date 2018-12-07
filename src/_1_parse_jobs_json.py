import json, collections, sys

def main():
  with open(sys.argv[-1]) as f:
    text = f.read()
  jobs = json.loads(text)
  tag_to_count = collections.defaultdict(int)
  for job in jobs:
    if not job['tags'].strip():
      tag_to_count['<untagged>'] += 1
      continue
    tags = []
    for word in job['tags'].split(' '):
      if not word:
        tag_to_count['more'] += 1
        break
      if tags and is_part_of_previous(tags[-1], word):
        tags[-1] += ' ' + word
      else:
        tags.append(word)
    for tag in set(tags):
      tag_to_count[tag] += 1

  for tag, count in sorted(tag_to_count.items(), key=lambda t: t[1]):
    print(tag, round(count / len(jobs), 2))

def is_part_of_previous(prev_word, next_word):
  if next_word in ('Design', 'Development'):
    return True
  if prev_word in ('Adobe', 'Video', 'Content'):
    return True
  return False

if __name__ == '__main__':
  main()
