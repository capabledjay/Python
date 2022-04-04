class Guess():
    def __init__(self):
        print(" WELCOME TO MY GUESSING GAME \n")
        self.mm()
        self.replay()
    def mm(self):
        self.count = 1
        while self.count <= 5:
            self.count+=1
            self.guess = "apple"
            self.what = input(" what do i have in the box >> ")
            if self.what == self.guess:
                print(" your guess is not correct")
                break
            
        else:
            print(" \n GAME OVER \n ")
    def replay(self):
        self.count = 0
        while self.count < 5:
            print(F" \n DO YOU WANT TO CONTINUE ")
            self.opt = [ "yes", " no"]
            print(self.opt)
            self.ans = input(">>>>>>> ")
            self.D = self.ans.lower()
            if self.D == self.opt[0]:
                print("\n WELCOME BACK")
                self.mm()
            else:
                self.D == self.opt[1]
                print(" THANK YOU FOR PLAYING")
                break
mm = Guess()