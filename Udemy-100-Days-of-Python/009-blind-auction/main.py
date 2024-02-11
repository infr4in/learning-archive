# from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

auction_dict = {}


def add_new_bidders(new_name, new_bill):
    auction_dict[new_name] = new_bill


end_of_auction = False
while not end_of_auction:
    name = input("What is your name?: ")
    bill = int(input("What's your bid?: $"))
    add_new_bidders(name, bill)
    answer = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if answer == "no":
        end_of_auction = True
    # clear()

highest_bill = 0
for bidder in auction_dict:
    bidder_bill = auction_dict[bidder]
    if bidder_bill >= highest_bill:
        highest_bill = bidder_bill
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bill}")
