import random

feet_in_mile=5280
beatles=["john lennon","paul McCartney","george harrison","Ringo Star"]
meters_in_kilometer=1000

def get_file_ext(filename):
    return filename[filename.index(".")+1:]
def roll_dice(num):
    return random.randint(1,num)