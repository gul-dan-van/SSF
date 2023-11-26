# SSF for Efficient Model Tuning

"Scaling & Shifting Your Features: A New Baseline for Efficient Model Tuning" ([arXiv](https://arxiv.org/abs/2210.08823)). 



#### Team Members
1. Gauranshu (12040560)
2. Himanshu Chalpe (12040460)
3. Prakhar Sharma (12041070)

#### Changes Done in the Repository
- We Cloned the ([official git repe](https://github.com/dongzelian/SSF))
- We adjusted the code and made it available for CPU and GPU.
- Updated code for outdated dependencies.
- Fixed corrupted path.

#### Novelty Implementation
- We introduced Median Elimination Multi-Armed Bandit Algorithm (MEMABA)
- Each SSF layer will be assigned to one of the arms of the bandit
- Each SSF layer will be switched off initially and an arm of bandit will switch it on.
- Each arm will be selected once and model will be trained for a few epochs
- After a certain number of epochs, all arms with expected score less than median score will be eliminated
- Above process will be continued until only a single arm is left, that will switch on SSF layer with best performance