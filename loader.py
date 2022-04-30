import time
import sys


class Loader():

    def loading(self, max):
        # animation = "|/-\\"
        # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        # animation = ["[■□□□□□□□□□□□]", "[■■□□□□□□□□□□]", "[■■■□□□□□□□□□]", "[■■■■□□□□□□□□]", "[■■■■■□□□□□□□]", "[■■■■■■□□□□□□]",
        #              "[■■■■■■■□□□□□]", "[■■■■■■■■□□□□]", "[■■■■■■■■■□□□]", "[■■■■■■■■■■□□]", "[■■■■■■■■■■■□]", "[■■■■■■■■■■■■]"]

        for i in range(max):
            time.sleep(0.1)
            # sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
            sys.stdout.write(f"\rNumber of Hits : {i}")
            sys.stdout.flush()

        # print("\nDone!")
