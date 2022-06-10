import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    self.contents = []
    for key,value in args.items():
      for i in range(0, value):
        self.contents.append(key)

  def draw(self, nb_balls):
    balls = []
    if nb_balls >= len(self.contents):
      balls = copy.deepcopy(self.contents)
      self.contents.clear()
    else:
      for i in range(0, nb_balls):
        balls.append(self.contents.pop(random.randrange(len(self.contents))))

    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_valid_draw = 0
  is_valid = False
  
  for i in range(0, num_experiments):
    hat_copy = copy.deepcopy(hat)
    chose_balls = hat_copy.draw(num_balls_drawn)

    for key,value in expected_balls.items():
      if chose_balls.count(key) >= value:
        is_valid = True
      else:
        is_valid = False
        break

    if is_valid:
      num_valid_draw += 1
    
  return num_valid_draw / num_experiments
