## 👩🏻‍💻 DESCRIPTION
> welcome to `stats and chats 📊`, a text-analysis and generative text program. this project comes in two parts: `stats.py` and `chats.py`.

> `stats.py`: takes a text and examines its contiguous runs of alphabet characters (or "words"). these "words" are analyzed and returned as a statistical report.
this report includes:
* the word count of the text file
* the number of distinct words
* the top _n_ words ranked by frequency, alongside the # of times they appear
* the number of words that occur exactly once

![](./visuals/mlk-stats)
⬆️ an example of `stats.py`'s output using `mlk.txt`
<br>
<br>
> `chats.py`: takes a text and analyzes it for "bi-grams" and "tri-grams"-- or strings of words that occur in 2s or 3s. a dictionary is then made for each word storing that words' bi-grams and tri-grams. using this dictionary, a unique text is stochastically generated.

![](./visuals/mlk-chats)
⬆️ an example of `chats.py`'s output using `mlk.txt`

##  📦 INSTALLING AND RUNNING 
1. from [00eemsy/csci-121-projects/stats and chats](https://github.com/00eemsy/csci-121-projects/tree/main/stats%20and%20chats), download the following files/folders:
   * `stats.py`
   * `chats.py`
   * the `texts` folder
2. using your preferred console, type the following:
* for `stats.py`:
```
python3 stats.py < ./texts/[text of your choice].txt
```
* for `chats.py`:
```
python3 chats.py < ./texts/[text of your choice].txt
```  
   

## 🎮 DEMOS 
`jabberywocky.txt`
* `stats.py`
  ![](./visuals/jabberywocky-stats)
* `chats.py`
  ![](./visuals/jabberywocky-chats)

`cien_anos.txt`
* `stats.py`
  ![](./visuals/cien-anos-stats)
* `chats.py`
  ![](./visuals/cien-anos-chats)
