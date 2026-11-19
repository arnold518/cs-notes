## Reference: /home/arnold/arnold/github/cs-notes/docs/rl/RLbook2020.md
| New ref | Original ref | Location | References | Referenced by |
| --- | --- | --- | --- | --- |
| § 2. Multi-armed Bandits |  | rl/2.md |  |  |
| § 2.1. A k-armed Bandit Problem |  | rl/2.md |  |  |
| Definition 2.1 | **k-armed bandit problem** | rl/2.md |  |  |
| Definition 2.2 | **value of an action**; **A_t**; **R_t** | rl/2.md |  |  |
| Concept 2.3 | **Equation (2.2)**; **greedy actions**; **exploiting vs exploring** | rl/2.md |  |  |
| § 2.2. Action-value Methods |  | rl/2.md |  |  |
| Concept 2.4 | **Equation (2.1)**; **Equation (2.2)**; **action-value methods** | rl/2.md |  |  |
| Concept 2.5 | **Equation (2.1)**; **Equation (2.3)**; **Equation (2.4)**; **Equation (2.7)**; **sample-average methods** | rl/2.md |  |  |
| Concept 2.6 | **Equation (2.1)**; **Equation (2.2)**; **greedy action selection methods** | rl/2.md |  |  |
| Concept 2.7 | **Equation (2.2)**; **Figure 2.1**; **Figure 2.2**; **epsilon-greedy methods** | rl/2.md |  |  |
| § 2.3. The 10-armed testbed |  | rl/2.md |  |  |
| Example 2.8 | **Equation (2.1)**; **Equation (2.2)**; **Figure 2.1**; **Figure 2.2**; **10-armed testbed**; **greedy vs epsilon greedy results** | rl/2.md |  |  |
| Concept 2.9 | **Equation (2.5)**; **Equation (2.6)**; **Equation (2.7)**; **stationary vs nonstationary tasks**; **an exponential recency-weighted average** | rl/2.md |  |  |
| Concept 2.10 | **Equation (2.2)**; **Figure 2.1**; **Figure 2.2**; **epsilon greedy vs greedy (reward variances, nonstationarity)** | rl/2.md |  |  |
| § 2.4. Incremental Implementation |  | rl/2.md |  |  |
| Concept 2.11 | **Equation (2.3)**; **Equation (2.4)**; **incremental formulas for updating averages** | rl/2.md |  |  |
| Code 2.12 | **simple bandit algorithm** | rl/2.md |  |  |
| Concept 2.13 | **Equation (2.3)**; **Equation (2.4)**; **step-size parameter**; **general form of update rule** | rl/2.md |  |  |
| § 2.5. Tracking a Nonstationary Problem |  | rl/2.md |  |  |
| Concept 2.14 | **Equation (2.5)**; **Equation (2.6)**; **Equation (2.7)**; **an exponential recency-weighted average** | rl/2.md |  |  |
| Theorem 2.15 | **Equation (2.7)**; **convergence condition for step-size parameter** | rl/2.md |  |  |
| Concept 2.16 | **Equation (2.7)**; **the convergence condition are often not met** | rl/2.md |  |  |
| § 2.6. Optimistic Initial Values |  | rl/2.md |  |  |
| Concept 2.17 | **Figure 2.3**; **optimistic initial values encourage exploration** | rl/2.md |  |  |
| Example 2.18 | **Figure 2.3**; **10-armed testbed results with optimistic initial value** | rl/2.md |  |  |
| § 2.7. Upper-Confidence-Bound Action Selection |  | rl/2.md |  |  |
| Concept 2.19 | **Equation (2.10)**; **intuition on equation**; **UCB** | rl/2.md |  |  |
| Example 2.20 | **Equation (2.10)**; **Figure 2.4**; **10-armed testbed results with UCB** | rl/2.md |  |  |
| § 2.8. Gradient Bandit Algorithm |  | rl/2.md |  |  |
| Concept 2.21 | **Equation (2.11)**; **Equation (2.12)**; **Equation (2.13)**; **Equation (Q.E.D)**; **Figure 2.5**; **intuition on equation**; **gradient bandit algorithm**; **baseline** | rl/2.md |  |  |
| Concept 2.22 | **Equation (2.12)**; **Equation (2.13)**; **Equation (Q.E.D)**; **derivation of gradient ascent**; **baseline** | rl/2.md |  |  |
| Example 2.23 | **Equation (2.11)**; **Equation (2.12)**; **Figure 2.5**; **10-armed testbed results with gradient bandit** | rl/2.md |  |  |
| § 2.9. Associative Search (Contextual Bandits) |  | rl/2.md |  |  |
| Concept 2.24 | **associative vs nonassociative tasks**; **contextual bandits in the literature**; **because it involves both trial-and-error learning to search for the best actions** | rl/2.md |  |  |
| Example 2.25 | **contextual bandits in the literature**; **associative multi k-armed bandit example**; **because it involves both trial-and-error learning to search for the best actions** | rl/2.md |  |  |
| Concept 2.26 | **contextual bandits in the literature**; **because it involves both trial-and-error learning to search for the best actions**; **k-armed bandit vs associative search task vs full reinforcement learning problem** | rl/2.md |  |  |
| § 3. Finite Markov Decision Processes |  | rl/3.md |  |  |
| § 3.1. The Agent-Environment Interface |  | rl/3.md |  |  |
| Definition 3.1 | **Equation (3.1)**; **Equation (3.2)**; **Equation (3.3)**; **Figure 3.1**; **finite MDP**; **markov property**; **agent**; **environment**; **probabilistic dynamic function p** | rl/3.md |  |  |
| Concept 3.2 | **Equation (3.2)**; **Equation (3.3)**; **Equation (3.4)**; **Equation (3.5)**; **Equation (3.6)**; **state-transition probabilities**; **expected rewards for state-action pairs**; **expected rewards for state-action-next triples** | rl/3.md |  |  |
| Concept 3.3 | **Equation (3.1)**; **Figure 3.1**; **agent-environment boundary** | rl/3.md |  |  |
| Example 3.4 | **transition grpah of MDP**; **recycling robot example (example 3.3)** | rl/3.md |  |  |
| § 3.2. Goals and Rewards |  | rl/3.md |  |  |
| Definition 3.5 | **goal (reward hypothesis)** | rl/3.md |  |  |
| Concept 3.6 | **not how you want it achieved**; **reward signal is to communicate to the agent what you want achieved** | rl/3.md |  |  |
| § 3.3. Returns and Episodes |  | rl/3.md |  |  |
| Concept 3.7 | **Equation (3.7)**; **sum of rewards**; **expected return** | rl/3.md |  |  |
| Concept 3.8 | **Equation (3.7)**; **episodic tasks**; **terminal state** | rl/3.md |  |  |
| Concept 3.9 | **Equation (3.8)**; **Equation (3.9)**; **Equation (3.10)**; **discount rate**; **discounted return** | rl/3.md |  |  |
| Concept 3.10 | **Equation (3.8)**; **Equation (3.9)**; **discount rate**; **recurrence relation for discounted return** | rl/3.md |  |  |
| § 3.4. Unified Notation for Episodic and Continuing Tasks |  | rl/3.md |  |  |
| Concept 3.11 | **Equation (3.11)**; **unified notation for epsidoc and continuing tasks** | rl/3.md |  |  |
| § 3.5. Policies and Value Functions |  | rl/3.md |  |  |
| Concept 3.12 | **policy**; **policies** | rl/3.md |  |  |
| Concept 3.13 | **Equation (3.12)**; **state-value function for policy**; **policies** | rl/3.md |  |  |
| Concept 3.14 | **Equation (3.12)**; **Equation (3.13)**; **action-value function for policy** | rl/3.md |  |  |
| Concept 3.15 | **Equation (3.9)**; **Equation (3.12)**; **Equation (3.14)**; **backup diagram**; **bellman equation for state-value function** | rl/3.md |  |  |
| Concept 3.16 | **Equation (3.9)**; **Equation (3.13)**; **Equation (3.14)**; **backup diagram**; **bellman equation for action-value function** | rl/3.md |  |  |
| Example 3.17 | **Figure 3.2**; **gridworld example (example 3.5)** | rl/3.md |  |  |
| § 3.6. Optimal Policies and Optimal Value Functions |  | rl/3.md |  |  |
| Concept 3.18 | **Equation (3.15)**; **optimal policy**; **optimal state-value function**; **partial ordering between policies** | rl/3.md |  |  |
| Concept 3.19 | **Equation (3.15)**; **Equation (3.16)**; **Equation (3.17)**; **optimal state-alue function**; **optimal action-value function** | rl/3.md |  |  |
| Concept 3.20 | **Equation (3.9)**; **Equation (3.18)**; **Equation (3.19)**; **Equation (3.20)**; **Figure 3.4**; **backup diagram**; **bellman optimality equation for state-value function** | rl/3.md |  |  |
| Concept 3.21 | **Equation (3.16)**; **Equation (3.17)**; **Equation (3.20)**; **Figure 3.4**; **backup diagram**; **bellman optimality equation for action-value function** | rl/3.md |  |  |
| Concept 3.22 | **Equation (3.9)**; **Equation (3.18)**; **Equation (3.19)**; **Equation (3.20)**; **Figure 3.4**; **v_star can be solved with solving systems of unlinear equations**; **optimal policy can be obtained from v_star or q_star (through greedy search)** | rl/3.md |  |  |
| Concept 3.23 | **limitation of explicitly solving the bellman optimality equation** | rl/3.md |  |  |
| § 3.7. Optimality and Approximation |  | rl/3.md |  |  |
| Concept 3.24 | **why optimal solutions are unrealistic**; **approximation due to time and memory limits** | rl/3.md |  |  |
| § 4. Dynamic Programming |  | rl/4.md |  |  |
| § 4.1. Policy Evaluation (Prediction) |  | rl/4.md |  |  |
| Concept 4.1 | **Equation (3.9)**; **Equation (4.3)**; **Equation (4.4)**; **policy evaluation in the DP literature**; **existence and uniqueness**; **policy evalutaion equation (3.6 bellman equation for state-value function)** | rl/4.md |  |  |
| Concept 4.2 | **Equation (3.9)**; **Equation (4.3)**; **Equation (4.4)**; **Equation (4.5)**; **Figure 4.1**; **policy evaluation in the DP literature**; **expected update**; **iterative policy evaluation**; **convergence** | rl/4.md |  |  |
| Code 4.3 | **Equation (4.5)**; **iterative policy evaluation**; **expected updates because they are based on an expectation over all possible next states rather than on a sample next state** | rl/4.md |  |  |
| § 4.2. Policy Improvement |  | rl/4.md |  |  |
| Theorem 4.4 | **Equation (4.6)**; **Equation (4.7)**; **Equation (4.8)**; **policy improvement theorem**; **strict inequality condition** | rl/4.md |  |  |
| Concept 4.5 | **Equation (4.6)**; **Equation (4.7)**; **Equation (4.8)**; **Equation (4.9)**; **policy improvement**; **greedy policy**; **choosing the argmax of actions (for deterministic policy)**; **optimality checking condition** | rl/4.md |  |  |
| Concept 4.6 | **Equation (4.6)**; **Equation (4.7)**; **Equation (4.8)**; **Equation (4.9)**; **Figure 4.1**; **policy improvement**; **extension to stochastic policy (policy improvement theorem)** | rl/4.md |  |  |
| § 4.3. Policy Iteration |  | rl/4.md |  |  |
| Concept 4.7 | **Equation (3.9)**; **Equation (4.3)**; **Equation (4.4)**; **Equation (4.5)**; **Equation (4.6)**; **Equation (4.7)**; **Equation (4.8)**; **Equation (4.9)**; **Figure 4.2**; **policy evaluation in the DP literature**; **policy iteration**; **finite convergence**; **policy improvement**; **iterative policy evaluation**; **expected updates because they are based on an expectation over all possible next states rather than on a sample next state** | rl/4.md |  |  |
| Code 4.8 | **policy iteration** | rl/4.md |  |  |
| § 4.4. Value Iteration |  | rl/4.md |  |  |
| Concept 4.9 | **Equation (4.10)**; **update rule**; **value iteration**; **truncated policy iteration**; **convergence** | rl/4.md |  |  |
| Concept 4.10 | **Equation (4.1)**; **Equation (4.2)**; **Equation (4.10)**; **value iteration**; **reference to bellman optimality** | rl/4.md |  |  |
| Code 4.11 | **Equation (4.10)**; **value iteration** | rl/4.md |  |  |
| § 4.5. Asynchronous Dynamic Programming |  | rl/4.md |  |  |
| Concept 4.12 | **asynchronous DP algorithm**; **asymptotic convergence guarantee**; **it still have to sweep over all states** | rl/4.md |  |  |
| Concept 4.13 | **update when agent is experiencing MDP**; **application of asynchronous DP: ordering updates** | rl/4.md |  |  |
| § 4.6. Generalized Policy Iteration |  | rl/4.md |  |  |
| Concept 4.14 | **stabilized only when both are consistent**; **and value functino being driven toward correct value for policy**; **generalized policy iteration - policy being improved by value function** | rl/4.md |  |  |
| Concept 4.15 | **GPI - two constraints (goals) or competition** | rl/4.md |  |  |
| § 4.7. Efficiency of Dynamic Programming |  | rl/4.md |  |  |
| Concept 4.16 | **complexity of DP - polynomial to state and action size** | rl/4.md |  |  |
| Concept 4.17 | **compare with exhaustive search and LP** | rl/4.md |  |  |
| Concept 4.18 | **asynchronous DP and other variations of GPI can be used to improve speed/memory** | rl/4.md |  |  |
| Concept 4.19 | **bootstrapping** | rl/4.md |  |  |
| § 5. Monte Carlo Methods |  | rl/5.md |  |  |
| § 5.1. Monte Carlo Prediction |  | rl/5.md |  |  |
| Concept 5.1 | **every-visit MC method**; **first-visit MC method**; **a visit to $s$** | rl/5.md |  |  |
| Code 5.2 | **first-visit MC prediction**; **a visit to $s$** | rl/5.md |  |  |
| Concept 5.3 | **every-visit MC**; **difference and convergence of first-visit**; **a visit to $s$** | rl/5.md |  |  |
| Concept 5.4 | **backup diagrams of Monte Carlo algorithm**; **a visit to $s$** | rl/5.md |  |  |
| Concept 5.5 | **estimates for each state is independent (no bootstrapping)** | rl/5.md |  |  |
| Concept 5.6 | **three advantages over DP methods**; **ability to learn from actual experience**; **ability to learn from simulated experience**; **estimating the value of a single state is independent of the number of total states** | rl/5.md |  |  |
| § 5.2. Monte Carlo Estimation of Action Values |  | rl/5.md |  |  |
| Concept 5.7 | **monte carlo estimation of action values** | rl/5.md |  |  |
| Concept 5.8 | **exploring starts**; **maintaining exploration problem** | rl/5.md |  |  |
| § 5.3. Monte Carlo Control |  | rl/5.md |  |  |
| Concept 5.9 | **Equation (5.1)**; **verification with policy improvement theorem**; **policy improvement with deterministic maximal action-value function** | rl/5.md |  |  |
| Concept 5.10 | **Equation (5.1)**; **GPI with monte carlo**; **exploring starts** | rl/5.md |  |  |
| Code 5.11 | **Monte Carlo ES (Exploring starts)** | rl/5.md |  |  |
| § 5.4. Monte Carlo Control without Exploring Starts |  | rl/5.md |  |  |
| Concept 5.12 | **target policy**; **behavior policy**; **on-policy vs off-policy** | rl/5.md |  |  |
| Definition 5.13 | **epsilon-soft policies** | rl/5.md |  |  |
| Definition 5.14 | **epsilon-greedy policy** | rl/5.md |  |  |
| Concept 5.15 | **Equation (5.2)**; **on-policy Monte Carlo Control** | rl/5.md |  |  |
| Code 5.16 | **Equation (5.2)**; **on-policy first-visit MC control (epsilon-soft policies)** | rl/5.md |  |  |
| Theorem 5.17 | **Equation (5.2)**; **epsilon greedy policy can hold iff they are better than or equal to all epsilon-soft policies** | rl/5.md |  |  |
| Theorem 5.18 | **Equation (5.2)**; **equality of epsilon greedy policy can hold iff they are better than or equal to all other epsilon-soft policies** | rl/5.md |  |  |
| § 5.5. Off-Policy Prediction via Importance Sampling |  | rl/5.md |  |  |
| Concept 5.19 | **target policy**; **behavior policy**; **off-policy learning**; **assumption of coverage** | rl/5.md |  |  |
| Concept 5.20 | **target policy**; **behavior policy**; **assumption of coverage**; **prediction problem setting (fixed target and behavior policies)** | rl/5.md |  |  |
| Concept 5.21 | **target policy**; **behavior policy**; **assumption of coverage**; **behavior example in many control examples** | rl/5.md |  |  |
| Definition 5.22 | **Equation (5.3)**; **Equation (5.4)**; **assumption of coverage**; **importance sampling ratio** | rl/5.md |  |  |
| Concept 5.23 | **Equation (5.3)**; **Equation (5.4)**; **Equation (5.5)**; **Equation (5.6)**; **importance-sampling ratio**; **ordinary importance sampling** | rl/5.md |  |  |
| Concept 5.24 | **Equation (5.3)**; **Equation (5.4)**; **Equation (5.5)**; **Equation (5.6)**; **Equation (5.7)**; **Equation (5.8)**; **Figure 5.3**; **target policy**; **behavior policy**; **assumption of coverage**; **importance-sampling ratio**; **ordinary importance sampling**; **weighted importance sampling** | rl/5.md |  |  |
| Concept 5.25 | **Equation (5.3)**; **Equation (5.4)**; **Equation (5.5)**; **Equation (5.6)**; **importance-sampling ratio**; **ordinary importance sampling**; **difference of ordinary and weighted importance sampling (biases and variance)** | rl/5.md |  |  |
| Example 5.26 | **Figure 5.4**; **infinite variance of ordinary importance sampling (example 5.5)** | rl/5.md |  |  |
| § 5.6. Incremental Implementation |  | rl/5.md |  |  |
| Concept 5.27 | **Equation (5.3)**; **Equation (5.4)**; **Equation (5.5)**; **assumption of coverage**; **importance-sampling ratio**; **ordinary importance sampling** | rl/5.md |  |  |
| Concept 5.28 | **Equation (5.7)**; **Equation (5.8)**; **incremental implementation for weighted importance sampling** | rl/5.md |  |  |
| Code 5.29 | **Equation (5.3)**; **Equation (5.4)**; **Equation (5.5)**; **Equation (5.6)**; **Equation (5.7)**; **Equation (5.8)**; **every-visit MC prediction**; **assumption of coverage**; **importance-sampling ratio**; **ordinary importance sampling**; **weighted importance sampling**; **off-policy** | rl/5.md |  |  |
| § 5.7. Off-Policy Monte Carlo Control |  | rl/5.md |  |  |
| Concept 5.30 | **target policy**; **behavior policy**; **off-policy monte carlo control** | rl/5.md |  |  |
| Code 5.31 | **off-policy MC control**; **target policy**; **behavior policy** | rl/5.md |  |  |
| Concept 5.32 | **so learning will be slow**; **learn only from the tail of episodes** | rl/5.md |  |  |
| § 5.8. Discounting-aware Importance Sampling |  | rl/5.md |  |  |
| Example 5.33 | **Equation (5.9)**; **Equation (5.10)**; **flat partial returns**; **intuition example for unnecessary large variance when discount factor is present**; **horizon (and $T$ is the time of termination of the episode)** | rl/5.md |  |  |
| Definition 5.34 | **flat partial return**; **horizon (and $T$ is the time of termination of the episode)** | rl/5.md |  |  |
| Concept 5.35 | **flat partial returns**; **horizon (and $T$ is the time of termination of the episode)** | rl/5.md |  |  |
| Concept 5.36 | **Equation (5.9)**; **Equation (5.10)**; **flat partial returns**; **discounting-aware importance sampling estimators**; **horizon (and $T$ is the time of termination of the episode)** | rl/5.md |  |  |
| § 5.9. Per-Decision Importance Sampling |  | rl/5.md |  |  |
| Concept 5.37 | **Equation (5.11)**; **Equation (5.12)**; **Equation (5.13)**; **Equation (5.14)**; **Equation (5.15)**; **per-decision importance sampling** | rl/5.md |  |  |
| § 6. Temporal-Difference Learning |  | rl/6.md |  |  |
| § 6.1. TD Prediction |  | rl/6.md |  |  |
| Concept 6.1 | **Equation (6.1)**; **constant-alpha MC (recall)** | rl/6.md |  |  |
| Concept 6.2 | **Equation (3.9)**; **Equation (6.1)**; **Equation (6.2)**; **Equation (6.3)**; **Equation (6.4)**; **Equation (6.5)**; **Equation (6.6)**; **TD error**; **one-step TD**; **$\mathrm{TD}(0)$** | rl/6.md |  |  |
| Code 6.3 | **TD(0) for estimating v_pi**; **$\mathrm{TD}(0)$** | rl/6.md |  |  |
| Concept 6.4 | **Equation (3.9)**; **Equation (6.1)**; **Equation (6.2)**; **Equation (6.3)**; **Equation (6.4)**; **DP vs MC vs TD**; **TD methods combine sampling of MC with bootstrapping or DP**; **$\mathrm{TD}(0)$** | rl/6.md |  |  |
| Concept 6.5 | **Equation (3.9)**; **Equation (6.1)**; **Equation (6.2)**; **Equation (6.3)**; **Equation (6.4)**; **backup diagram of TD**; **sample updates vs expected update**; **$\mathrm{TD}(0)$** | rl/6.md |  |  |
| Concept 6.6 | **Equation (3.9)**; **Equation (6.5)**; **Equation (6.6)**; **TD error** | rl/6.md |  |  |
| § 6.2. Advantages of TD Prediction Methods |  | rl/6.md |  |  |
| Concept 6.7 | **advantage of TD**; **do not require model of environment**; **online and fully incremental fashion** | rl/6.md |  |  |
| Concept 6.8 | **Figure 6.2**; **convergence of TD**; **TD converges faster than constant-alpha on stochastic tasks**; **certainty-equivalence estimate because it is equivalent to assuming that the estimate of the underlying process was known with certainty rather than being approximated** | rl/6.md |  |  |
| Example 6.9 | **example 6.2** | rl/6.md |  |  |
| § 6.3. Optimality of TD |  | rl/6.md |  |  |
| Concept 6.10 | **Figure 6.2**; **batch updating**; **certainty-equivalence estimate because it is equivalent to assuming that the estimate of the underlying process was known with certainty rather than being approximated** | rl/6.md |  |  |
| Concept 6.11 | **Figure 6.2**; **under batch updating TD and constant-alpha MC converges deterministically to a different value**; **certainty-equivalence estimate because it is equivalent to assuming that the estimate of the underlying process was known with certainty rather than being approximated** | rl/6.md |  |  |
| Example 6.12 | **example 6.4**; **certainty-equivalence estimate because it is equivalent to assuming that the estimate of the underlying process was known with certainty rather than being approximated** | rl/6.md |  |  |
| Concept 6.13 | **Figure 6.2**; **batch MC finds estimates that minimize MSE of the training set**; **and batch TD finds estimates exactly correct for maximal likelihood markov model**; **certainty-equivalence estimate** | rl/6.md |  |  |
| Concept 6.14 | **Figure 6.2**; **why TD methods converge quickly than MC in terms of certainty equivalence estimate**; **certainty-equivalence estimate because it is equivalent to assuming that the estimate of the underlying process was known with certainty rather than being approximated** | rl/6.md |  |  |
| Concept 6.15 | **Figure 6.2**; **TD are optimal in sense of approximating certainty-equivalence solution**; **certainty-equivalence estimate because it is equivalent to assuming that the estimate of the underlying process was known with certainty rather than being approximated** | rl/6.md |  |  |
| § 6.4. Sarsa : On-policy TD Control |  | rl/6.md |  |  |
| Concept 6.16 | **Equation (6.7)**; **backup diagram for SARSA**; **action-value function (SARSA)** | rl/6.md |  |  |
| Concept 6.17 | **Equation (6.7)**; **on-policy algorithm based on SARSA** | rl/6.md |  |  |
| Code 6.18 | **Equation (6.7)**; **SARSA (on-policy TD control)** | rl/6.md |  |  |
| Concept 6.19 | **Equation (6.7)**; **convergence condition of SARSA**; **it "Modified Connectionist Q-learning** | rl/6.md |  |  |
| § 6.5. Q-learning : Off-policy TD Control |  | rl/6.md |  |  |
| Concept 6.20 | **Equation (6.8)**; **Figure 6.4**; **backup diagram for Q-learning**; **$Q$-learning (Watkins)** | rl/6.md |  |  |
| Code 6.21 | **Equation (6.8)**; **Q-learning (off-policy TD control)**; **$Q$-learning (Watkins)** | rl/6.md |  |  |
| Concept 6.22 | **Equation (6.8)**; **convergence of Q-learning**; **$Q$-learning (Watkins)** | rl/6.md |  |  |
| Concept 6.23 | **Equation (6.8)**; **Exercise 6.11**; **why q-learning is considered off-policy**; **$Q$-learning (Watkins)** | rl/6.md |  |  |
| § 6.6. Expected Sarsa |  | rl/6.md |  |  |
| Concept 6.24 | **Equation (6.9)**; **Figure 6.3**; **Figure 6.4**; **Expected Sarsa** | rl/6.md |  |  |
| Concept 6.25 | **Equation (6.9)**; **Figure 6.3**; **Figure 6.4**; **Expected Sarsa**; **generalization of sarsa and q-learning** | rl/6.md |  |  |
| Example 6.26 | **Equation (6.9)**; **Figure 6.3**; **Figure 6.4**; **Expected Sarsa**; **comparison of sarsa**; **q-learning** | rl/6.md |  |  |
| § 6.7. Maximization Bias and Double Learning |  | rl/6.md |  |  |
| Concept 6.27 | **Figure 6.5**; **Double Q-learning**; **maximization bias** | rl/6.md |  |  |
| Example 6.28 | **Figure 6.5**; **example 6.7** | rl/6.md |  |  |
| Concept 6.29 | **double learning intuition (in bandits)** | rl/6.md |  |  |
| Concept 6.30 | **Figure 6.5**; **Double Q-learning** | rl/6.md |  |  |
| Code 6.31 | **Double Q-learning** | rl/6.md |  |  |
| § 7. n-step Bootstrapping |  | rl/7.md |  |  |
| § 7.1. n-step TD Prediction |  | rl/7.md |  |  |
| Concept 7.1 | **Equation (7.1)**; **Equation (7.2)**; **Figure 7.1**; **them one-step TD methods**; **one-step return (TD) (recall)**; **n-step return**; **complete return (monte carlo)**; **$n$-step TD methods** | rl/7.md |  |  |
| Concept 7.2 | **Equation (7.1)**; **Equation (7.2)**; **Equation (7.3)**; **Figure 7.1**; **n-step TD**; **them one-step TD methods**; **error reduction property of $n$-step returns** | rl/7.md |  |  |
| Code 7.3 | **n-step TD for estimating v** | rl/7.md |  |  |
| Theorem 7.4 | **Equation (7.1)**; **Equation (7.2)**; **Equation (7.3)**; **convergence of n-step TD prediction**; **error reduction property** | rl/7.md |  |  |
| § 7.2. n-step SARSA |  | rl/7.md |  |  |
| Concept 7.5 | **Equation (7.4)**; **Equation (7.5)**; **Figure 7.3**; **Figure 7.4**; **n-step sarsa**; **n-step return (in action values)** | rl/7.md |  |  |
| Code 7.6 | **n-step sarsa for estimating q** | rl/7.md |  |  |
| Example 7.7 | **Equation (7.4)**; **Equation (7.5)**; **Figure 7.3**; **Figure 7.4**; **why n-step sarsa can speed up learning compared to one-step** | rl/7.md |  |  |
| Concept 7.8 | **Equation (7.4)**; **Equation (7.5)**; **Equation (7.7)**; **Equation (7.8)**; **Figure 7.3**; **n-step expected sarsa** | rl/7.md |  |  |
| § 7.3. n-step off policy learning |  | rl/7.md |  |  |
| Concept 7.9 | **Equation (7.9)**; **Equation (7.10)**; **Equation (7.11)**; **importance sampling ratio**; **n-step off-policy learning with importance sampling** | rl/7.md |  |  |
| Code 7.10 | **Equation (7.9)**; **Equation (7.10)**; **Equation (7.11)**; **importance sampling ratio**; **off-policy n-step sarsa for estimating q** | rl/7.md |  |  |
| Concept 7.11 | **Equation (7.7)**; **Equation (7.8)**; **Equation (7.9)**; **Equation (7.10)**; **Equation (7.11)**; **importance sampling ratio**; **off-policy version of n-step expected sarsa** | rl/7.md |  |  |
| § 7.4. Per-decision Methods with Control Variates |  | rl/7.md |  |  |
| Concept 7.12 | **Equation (7.1)**; **Equation (7.2)**; **Equation (7.12)**; **Equation (7.13)**; **n-step TD update with off-policy definition**; **control variate (reduces variance)**; **a control variate (for obscure reasons)**; **off-policy definitino of n-step return for state values**; **7.4 \*Per-decision Methods with Control Variates** | rl/7.md |  |  |
| Concept 7.13 | **Equation (7.4)**; **Equation (7.5)**; **Equation (7.7)**; **Equation (7.8)**; **Equation (7.9)**; **Equation (7.10)**; **Equation (7.11)**; **Equation (7.12)**; **Equation (7.13)**; **Equation (7.14)**; **importance sampling ratio**; **a control variate (for obscure reasons)**; **n-step sarsa update with off-policy definition**; **off-policy definition of n-step return for action values**; **7.4 \*Per-decision Methods with Control Variates** | rl/7.md |  |  |
| § 7.5. Off-policy Learning without Importance Sampling : The n-step Tree Backup Algorithm |  | rl/7.md |  |  |
| Concept 7.14 | **Equation (7.15)**; **Equation (7.16)**; **backup diagram**; **tree-backup algorithm**; **a tree-backup update**; **it is an update from the entire tree of estimated action values** | rl/7.md |  |  |
| Concept 7.15 | **Equation (7.15)**; **Equation (7.16)**; **tree-backup algorithm**; **action-value update rule**; **recursive definition of tree-backup n-step return**; **a tree-backup update**; **it is an update from the entire tree of estimated action values** | rl/7.md |  |  |
| Code 7.16 | **Equation (7.15)**; **Equation (7.16)**; **tree-backup algorithm**; **a tree-backup update**; **it is an update from the entire tree of estimated action values**; **n-step tree backup for estimating q** | rl/7.md |  |  |
| § 7.6 A Unifying Algorithm : n-step Q(sigma) |  | rl/7.md |  |  |
| Concept 7.17 | **Equation (7.17)**; **Figure 7.5**; **backup diagram**; **unified algorithm**; **7.6 \*A Unifying Algorithm: $n$-step $Q(\sigma)$** | rl/7.md |  |  |
| Concept 7.18 | **Equation (7.4)**; **Equation (7.5)**; **Equation (7.17)**; **Figure 7.3**; **Figure 7.5**; **equations of n-step Q(sigma)**; **update for n-step sarsa without importance sampling**; **7.6 \*A Unifying Algorithm: $n$-step $Q(\sigma)$** | rl/7.md |  |  |
| Code 7.19 | **off-policy n-step Q(sigma) for estimating q** | rl/7.md |  |  |
