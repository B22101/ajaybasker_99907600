
"""Implement a class called player that represent a criket player. The player class should have a
method cslled plsy() which prints "The player is playing cricket. derive two classes , Batsman and
Bowler, from the player class. override the play() method in each derived class to print "The batsman is bating"
and "The bowler is bowling", respectively. write a program to create objects of both the 
Batsman and Bowler classes and cell the play() method for each object."""

class player:
   def play(self):
      print("The is playing cricket.")
class Batsman(player):
  def play(self):
      print("The batsman is batting.") 
class Batsman(player):
  def play(self):
      print("The batsman is batting.")
class Bowler(player):
  def play(self):
      print("The bowler is bowling.")
batsman = Batsman()
bowler =  Bowler()
batsman.play()
bowler.play()