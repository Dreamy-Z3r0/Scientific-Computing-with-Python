import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Construct a sample space
        self.contents = []
        for ball in kwargs:
            self.contents.extend([ball] * kwargs[ball])

    def draw(self, num):
        # Return the previously drawn balls to contents 
        # before a new draw operation
        try:
            self.contents.extend(self.ballsDrawn)
            self.ballsDrawn.clear()
        except AttributeError:
            pass

        # If number of balls to draw exceeds available quantity
        # in the hat, the draw operation is not executed.
        if num >= len(self.contents):
            self.ballsDrawn = copy.deepcopy(self.contents)
            self.contents.clear()
        else:
            # Draw random balls
            self.ballsDrawn = []
            while num > 0:
                # Get a random index from contents
                index = random.randrange(len(self.contents))

                # Insert the value of contents at index to ballDrawn
                self.ballsDrawn.append(self.contents[index])

                # Remove the entry at index from contents
                self.contents.pop(index)

                # Decrement num count
                num -= 1

        # Return the list of drawn balls
        return self.ballsDrawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Set up sampling space
    N = num_experiments
    M = 0

    # Start drawing balls from the hat
    while num_experiments > 0:
        # Draw {num_balls_drawn} balls from {hat}
        ballsDrawn = hat.draw(num_balls_drawn)

        # Check if the list of drawn balls matches the expected
        matchingExpected = True
        for ball in expected_balls:
            matchingExpected &= (expected_balls[ball] <= ballsDrawn.count(ball))

        # Increment M if the condition is met
        if matchingExpected:
            M += 1

        # Decrement the num_experiments count
        num_experiments -= 1

    # Calculate and return the probability
    return M/N

if __name__ == '__main__':
    hat = Hat(black=6, red=4, green=3)

    for _ in range(10):
        num_balls_drawn=random.randrange(15)
        probability = experiment(hat=hat,
                        expected_balls={"red":2,"green":1},
                        num_balls_drawn=random.randrange(15),
                        num_experiments=2000)
        print(f'num_balls_drawn = {num_balls_drawn} | probability = {probability}')