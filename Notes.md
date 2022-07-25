# Notes

Just some of my thoughts and stuff that is important to note when using Tkinter.

## Nuances

1. To pass parameters into `Tkinter.Button(command=function)`, we must change it from `Button(command=func(val))` to `Button(command=lambda: func(val))`.
2. [Making Buttons Span Multiple Columns](https://stackoverflow.com/questions/44659879/ttk-button-span-multiple-columns)
3. [https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLJ0MS0ZtPWoNz1C3lRlvrUCwPoDM2JYQ6&index=4&t=10936s&ab_channel=freeCodeCamp.org](Awesome Tkinter tutorial)
4. [Tkinter with Classes](https://www.youtube.com/watch?v=IYHJRnVOFlw&t=249s&ab_channel=thenewboston)