

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />

  </p>
</div>




<!-- ABOUT THE PROJECT -->
## About The Project
For our project we scraped data from Stack Overflow and performed multiple analyses on it. Language processing was used to explore trends in the popularity of computer languages and topics, as well as to identify the sentiment of users, on Stack Overflow over time. <br>
The second part of our project involved using Linear Discriminant and Cosine Similarity analysis to identify and predict the topics of user entered text and recommend similar questions.   


## Dataset
We downloaded pre-scraped data, available here:


* https://www.brentozar.com/archive/2015/10/how-to-download-the-stack-overflow-database-via-bittorrent/


We first attempted to scrape the data directly using the Stack Overflow API. However due to query limits, it was decided that starting with the above dataset would be much faster. After downloading the dataset, it was loaded into a local Microsoft SQL database so that it could be queried directly from the Python working environment.<br>


## Built With
The data processing was done in Python using Jupyter Notebook. The topic/similar question predictor part of the project was built as a simple Flask application and then integrated into Tableau. The actual visualization of the data is presented in Tableau.<br>
The following Python libraries were used in performing the language processing and analysis:
* [NLTK](https://www.nltk.org/)
* [Gensim](https://radimrehurek.com/gensim/)
* [Pickle](https://docs.python.org/3/library/pickle.html#module-pickle)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)


## Project part I - Language Analysis 
This is an example of how you may give instructions on setting up your project locally.


## Project part II - Question and Topic Predictor
buildLDAModel.ipynb contains the code needed to build an LDA model based on the scraped question text data. The following calls the methods needed to process the text and prepare a set of tokens for the dictionary:
  ```sh
for key in dict:
    tokens = tokenizeText(dict[key]['Text'])
    tokens = removeFirstLastThree(tokens)
    tokens = toLowerCase(tokens)
    tokens = removeStopWords(tokens)
    tokens = applyPStemmer(tokens)
    tokens = get_lemma(tokens)
  ```

Then we create create a dictionary for the text tokens and save it so that it can be reused:
  ```sh
dict = corpora.Dictionary(text_tokens)
dict.save('dictionary.gensim')
  ```
This dictionary is then used to create a bag of words model which is also saved:
  ```sh
bagOfWords = [dict.doc2bow(t) for t in text_tokens]
pickle.dump(bagOfWords, open('corpus.pkl', 'wb'))
  ```
Then the actual LDA model can be generated and saved. The number of topics, passes and words was varied and the following provided good results: 

```shl 
NUM_TOPICS = 25
NUM_WORDS = 2

lda model = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save('models/lda_model.model')
  ```
Once the LDA model is built and saved, it can be loaded and run as follows:
```shl 
ldamodel =  models.LdaModel.load('models/lda_model.model')
topics = ldamodel.print_topics(num_words=NUM_WORDS)
  ```
Where NUM_WORDS gives the number of words in each of the NUM_TOPICS that the model identifies 

Printing this gives:
```shl 
(12, '0.192*"self" + 0.026*"let"')
(8, '0.118*"file" + 0.038*"line"')
(17, '0.115*"image" + 0.046*"category"')
(16, '0.107*"div" + 0.103*"class"')
(10, '0.084*"string" + 0.075*"public"')
(22, '0.058*"int" + 0.034*"array"')
(23, '0.237*"app" + 0.076*"tag"')
(15, '0.037*"version" + 0.030*"build"')
(14, '0.139*"property" + 0.047*"binding"')
(7, '0.067*"function" + 0.057*"var"')
(24, '0.022*"strong" + 0.019*"like"')
(19, '0.102*"http" + 0.073*"com"')
(18, '0.072*"stack" + 0.070*"http"')
(4, '0.032*"server" + 0.028*"test"')
(11, '0.192*"android" + 0.049*"view"')
(21, '0.115*"model" + 0.079*"date"')
(9, '0.033*"task" + 0.032*"system"')
(6, '0.048*"row" + 0.046*"list"')
(13, '0.066*"product" + 0.059*"query"')
(1, '0.065*"width" + 0.063*"color"')
  ```


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



## References
The following sites were used as a reference during the creation of our project:


* [LDA Topic Modelling With Gensim](https://predictivehacks.com/lda-topic-modelling-with-gensim/) 

Site #2
* [abc](https://www.webpagefx.com/tools/emoji-cheat-sheet)
