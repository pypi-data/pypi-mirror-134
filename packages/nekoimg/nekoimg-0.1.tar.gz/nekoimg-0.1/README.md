# ⚠️ WARNING! ⚠️ When you import the module the module activates! so here is an example to use it!

```py
import time

open = input('Hey You Want a Random Neko Image? (Yes Or No): ')
if open == 'Yes':
    import nekoimg
    exit()
if open == 'No':
    time.sleep(0.5)
    print('Bye!')
    exit()
else:
    print('Hey! "' + open + '" Is Not A Valid Option! Try Again')