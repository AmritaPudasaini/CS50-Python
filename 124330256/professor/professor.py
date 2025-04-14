import random

def main():
    level = get_level()
    score = 0

    for i in range (10):
      x = generate_integer(level)
      y = generate_integer(level)
      problem = f"{x} + {y} = "
      correct_answer = x + y

      for j in range(3):
        try:
          user_answer = int(input(problem))
          if user_answer == correct_answer:
            score += 1
            break
          else:
            print("EEE")

        except ValueError:
          print("EEE")

      if j==2 and user_answer != correct_answer:
        print(f"{problem}{correct_answer}")

    print(f"Score: {score}")

def get_level():
  while True:
    try:
      level = int(input("Level: "))
      if 1 <= level <= 3:
        return level
    except ValueError:
      pass

def generate_integer(level):

  if level==1:
    return random.randint(0,9)

  elif level==2:
    return random.randint(10,99)

  elif level==3:
    return random.randint(100,999)

  else:
    raise ValueError

if __name__ == "__main__":
  main()
