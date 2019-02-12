import copy, random

original_questions = {
  #Format is 'question':[options]
  'According to the new 2017 NIST guidelines, how often should you change your password?':['Never','Every month','Every 6 months','Every year'],
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
  selected_keys = []
  i = 0
  while i < len(q):
    current_selection = random.choice(q.keys())
    if current_selection not in selected_keys:
      selected_keys.append(current_selection)
      i = i+1
  return selected_keys

questions_shuffled = shuffle(questions)

for i in questions_shuffled:
 random.shuffle(questions[i])
 print('''
 Where is {} located?
 {}
 Correct Answer is: {}
 ''').format(i,questions[i],original_questions[i][0])
