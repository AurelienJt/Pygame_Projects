run = True

class Hanoi():
    def __init__(self):
        self.sticks = {
            "1": ["big","med","small"],
            "2": [],
            "3":[],
        }
        self.finished = False
        
    def play(self,sender:str,destination:str):
        self.sender = sender
        self.destination = destination

        if Hanoi.check_rule(self):
            Hanoi.move(self)
            Hanoi.check_won(self)
        else:
            print("Not possible, play again please.")
   
    def move(self):
        if len(self.sticks[self.sender]) > 0:
            target = self.sticks[self.sender][-1]
            self.sticks[self.sender].pop(-1)
            self.sticks[self.destination].append(target)
            
    def check_won(self):
        win_situation = ["big","med","small"]
        if self.sticks["3"] == win_situation:
            self.finished = True

    def check_rule(self):
        transferred = self.sticks[self.sender][-1]
        if len(self.sticks[self.destination]) != 0:
            host = self.sticks[self.destination][-1]
            if transferred == "big":
                return False
            elif transferred == "med" and host == "small":
                return False
            return True
        else:
            return True
        
    def display(self):
        output = f"""
        Stick_1: {self.sticks["1"]}
        Stick_2: {self.sticks["2"]}
        Stick_3: {self.sticks["3"]}
        """
        return output

game_1 = Hanoi()

while run:
    print(game_1.display())
    print("Next Turn...\n")
    sender = input("Sender: ")
    destination = input("Destination: ")
    
    game_1.play(sender=sender,destination=destination)
    if game_1.finished:
        print("You won")
        run = False
