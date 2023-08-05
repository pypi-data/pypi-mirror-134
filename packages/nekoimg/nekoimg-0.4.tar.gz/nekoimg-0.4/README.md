
# First Installing
You Need To Have python installed
and for install the module you use ```pip install nekoimg```

⚠️ WARNING ⚠️ For The moment the only option is nekoimg.random
# THERE IS AN EXAMPLE:

```py
import time
import nekoimg

open = input('Hey You Want a Random Neko Image? (Yes Or No): ')
if open == 'Yes':
    nekoimg.random()
    exit()
if open == 'No':
    time.sleep(0.5)
    print('Bye!')
    exit()
else:
    print('Hey! "' + open + '" Is Not A Valid Option! Try Again')
