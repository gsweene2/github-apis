# Use . when importing module in flat structure
import logging

def hello_world():
    logging.info("[hello_world]")
    print("Hello World!")

def main():
    logging.info("Program started!")
    hello_world()

if __name__ == "__main__":
    main()
