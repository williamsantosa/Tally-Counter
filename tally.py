import tkinter as tk
from tkinter import ttk

class Counter(tk.Tk):
  def __init__(self):
    super().__init__()

    # Initialize variables and set title
    self.counter = 0
    self.increment = 1
    self.title('Tally Counter')
    self.resizable(False, False)
    self.geometry("250x100")
    # Create buttons
    self.resetButton = tk.Button(self, text="reset", padx=24, pady=28, command=self.reset)
    self.increaseButton = tk.Button(self, text="+", padx=35, pady=28, command=lambda: self.increase(self.increment))
    self.decreaseButton = tk.Button(self, text="-", padx=35, pady=28, command=lambda: self.decrease(self.increment))
    self.counterDisplay = tk.Entry(self, justify=tk.CENTER)

    # Place on screen
    self.resetButton.grid(row=0, column=0)
    self.increaseButton.grid(row=0, column=2)
    self.decreaseButton.grid(row=0, column=1)
    self.counterDisplay.grid(row=1, column=0, columnspan=3, sticky=tk.N+tk.S+tk.W+tk.E)

    # Initialize variable
    self.reset()

  def reset(self):
    self.counter = 0
    self.updateDisplay()

  def increase(self, n):
    self.counter += n
    self.updateDisplay()

  def decrease(self, n):
    self.counter -= n
    self.updateDisplay()

  def updateDisplay(self):
    self.counterDisplay.delete(0, tk.END)
    self.counterDisplay.insert(0, str(self.counter))
    self.update()


if __name__ == "__main__":
  app = Counter()
  app.mainloop()