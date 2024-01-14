## 👩🏻‍💻 DESCRIPTION
Welcome to `stats and chats 📊`, a text-analysis and generative text program. This project comes in two parts: `stats.py` and `chats.py`.

`stats.py`: Takes a text and examines its contiguous runs of alphabet characters (or "words"). These "words" are analyzed and returned as a statistical report.
This report includes:
* The word count of the text file
* The number of distinct words
* The top _n_ words ranked by frequency, alongside the # of times they appear
* The number of words that occur exactly once
  
⬇️ An example of `stats.py`'s output using `mlk.txt`
![](./visuals/mlk-stats.png)
<br>
<br>
`chats.py`: Takes a text and analyzes it for "bi-grams" and "tri-grams"-- or strings of words that occur in 2s or 3s. A dictionary is then made for each word storing that words' bi-grams and tri-grams. Using this dictionary, a text is stochastically generated.

⬇️ An example of `chats.py`'s output using `mlk.txt`
![](./visuals/mlk-chats.png)

##  📦 INSTALLING AND RUNNING 
1. From [00eemsy/csci-121-projects/stats and chats](https://github.com/00eemsy/csci-121-projects/tree/main/stats%20and%20chats), download the following files/folders:
   * `stats.py`
   * `chats.py`
   * The `texts` folder
2. Using your preferred console, type the following:
* For `stats.py`:
```
python3 stats.py < ./texts/[text of your choice].txt
```
* For `chats.py`:
```
python3 chats.py < ./texts/[text of your choice].txt
```  
   

## 🎮 DEMOS 
`jabberywocky.txt`
* `stats.py`
  ![](./visuals/jabberywocky-stats.png)
* `chats.py`
  ![](./visuals/jabberywocky-chats.png)

`cien_anos.txt`
* `stats.py`
  ![](./visuals/cien-anos-stats.png)
* `chats.py`
  ![](./visuals/cien-anos-chats.png)
