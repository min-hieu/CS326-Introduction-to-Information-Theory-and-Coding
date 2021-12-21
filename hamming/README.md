# Hamming Code

We want to implement the (7,4,3) Hamming code with the parity check matrix `H` over a binary symmetric channel with probability `p`. The transmitted codeword, received vector and estimated codeword is denoted `c`,`r`, and `c_hat` respectively. The output of the program should show the graph of the theoretical derivation and emperical result of the probabilities of error that occur. 

## Theoretical Derivation

![](https://raw.githubusercontent.com/min-hieu/EE326-Introduction-to-Information-Theory-and-Coding/main/hamming/img/theoretical_derivation.png)

## Emperical Result

- We have the error probability of undetected error: 

![](https://raw.githubusercontent.com/min-hieu/EE326-Introduction-to-Information-Theory-and-Coding/main/hamming/img/undetected.png)

- We have the error probability of detected and corrected error: 

![](https://raw.githubusercontent.com/min-hieu/EE326-Introduction-to-Information-Theory-and-Coding/main/hamming/img/detected_corrected.png)

- We have the error probability of detected but not corrected error: 

![](https://raw.githubusercontent.com/min-hieu/EE326-Introduction-to-Information-Theory-and-Coding/main/hamming/img/detected_uncorrected.png)

## Final Result 
We have the final result of the probability for `p` as follow (top to bottom):
![](https://raw.githubusercontent.com/min-hieu/EE326-Introduction-to-Information-Theory-and-Coding/main/hamming/img/p.png)
And thus we have the final graph: 

![](https://raw.githubusercontent.com/min-hieu/EE326-Introduction-to-Information-Theory-and-Coding/main/hamming/img/result.png)
