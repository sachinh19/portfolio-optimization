# Portfolio Optimization
## (Reinforcement Learning using Q Learning)

![Stock Trading](https://3ncb884ou5e49t9eb3fpeur1-wpengine.netdna-ssl.com/wp-content/uploads/2018/01/canadian-marijuana-stocks-full-bloom-hero.jpg)

### Problem Formulation :-
We are trying to solve a very simplified version of the classic Portfolio Optimization Problem, so that it can be within the scope of Reinforcement learning[Q-learning].

#### Assumptions :-
1. A stock portfolio will consist of exactly 5 stocks[A,B,C,D,E] at any given time.
2. Only one transaction of exchange(selling one stock and buying another) is allowed per day.
3. Only 5% of one stock can be exchanged with another stock on any given day.

#### State description :-
1. To reduce the infinite state space concern, we have classified the state as follows:
* We have represented the state of the stock in a string of 5 alphabets each alphabet is one from letters A,B,C,...R,S,T,U
* Based on the percentage of stock in the portfolio in the current state, a letter is assigned to represent the state of that stock in the overall state of the portfolio.
	* The letter 'A' corresponds to a stock with 0% share in the portfolio, B corresponds to values in the set (0-5]%, C corresponds to (5-10] and so on till U which corresponds to (95,100].
	* e.g. If a stock portfolio in share of percentages looks something like this :[9,24,44,20,3]; then it will be represented in the 5-character string representation as CFJEB. Similarly [19,24,44,7,6] is EFJCC and [95,1,1,2,1] is TBBBB.
	* Thus state transition is just a change of alphabets in the string of 5 characters.

2. The possible actions from the current state will be obtained by checking all possible 5% exchanges that can happen on the stock portfolio.

#### Goal :-
Goal of the system is to maximize the value of the stock portfolio over a period of 5 years(4 years of exploration + 1 year of exploitation)

#### Evaluation :-
The do-nothing benchmark
- If the stock portfolio is kept aside for the exploitation period, then the system should outperform the price rise of those stocks in that period.
- For all the stocks, the do-nothing benchmark is calculated by giving equal weightage to all stocks(i.e. 20% -> EEEEE) and then allowing the stock value to increase over the period.

## Authors
* Aditya Masurkar
* Sachin Haldavanekar


