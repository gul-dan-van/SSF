import random
import statistics

# Dummy function to train the model with active layers
def train_model_with_active_layers(active_layers):
    pass

# Dummy function to evaluate model performance
def evaluate_model_performance():
    scores = [random.uniform(0, 1) for _ in range(k)]
    return scores

def median_elimination_bandit(k_layers, num_iterations):
    arms = [False] * k_layers  
    
    for _ in range(num_iterations):
        active_arms = [i for i, arm in enumerate(arms) if arm]  
        
        train_model_with_active_layers(active_arms)  
        scores = evaluate_model_performance()  
        
        median_score = statistics.median(scores)  
        
        # Eliminate arms with scores below median
        for i, score in enumerate(scores):
            if score < median_score:
                arms[i] = False
    
    best_arm = scores.index(max(scores))  
    
    return best_arm

k = 12
iterations = 10  

best_layer = median_elimination_bandit(k, iterations)
print(f"The best layer selected is: Layer {best_layer + 1}")
