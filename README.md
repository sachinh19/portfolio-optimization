# Portfolio Optimization
## Reinforcement Learning using Q Learning.

![Stock Trading](https://flextrade.com/wp-content/uploads/2015/07/Blog_FeatureImage_PTS_10959394-300x225.jpg)

###Problem Formulation :-
We are trying to solve a very simplied version of the original Portfolio Optimization Problem, so that it can be within the capabilities of Reinforcemen learning using Q-learning and specifically done to avoid any Neural Network based approaches.

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
3. The possible actions from the current state will be obtained by checking all possible 5% exchanges that can happen on the stock portfolio.






