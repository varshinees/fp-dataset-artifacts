import json
#import matplotlib.pyplot as plt 

'''
captum
    integrated gradients
lit
'''

def read_eval_output():
    file_name = "eval_output_final2/eval_predictions.jsonl"
    f = open(file_name)
    data = []
    avg_predicted_score = []
    num_entails_right = 0
    num_contradicts_right = 0
    num_neutral_right = 0
    num_entails_wrong = 0
    num_contradicts_wrong = 0
    num_neutral_wrong = 0
    avg_confidence_right = 0
    num_right = 0
    avg_confidence_wrong = 0
    num_wrong = 0

    num_pred_entails = 0
    num_pred_contradicts = 0
    count = 0
    for line in f:
        example = json.loads(line)
        label = example['label']
        pred_label = example['predicted_label']
        hypothesis = example['hypothesis']
        count += 1
        if pred_label == 0:
            num_pred_entails += 1
        elif pred_label == 1:
            num_pred_contradicts += 1

        if  label == pred_label:
            #print("Hypothesis: " + str(example['hypothesis']) + " Label: " + str(example['label']) + " Pred: " + str(example['predicted_label']))
            data.append(example)
            if pred_label == 0:
                num_entails_right += 1
            elif pred_label == 1:
                num_contradicts_right += 1
            else:
                num_neutral_right += 1
            num_right += 1
            avg_confidence_right += findConfidence(example['predicted_scores'])
            #if "white" in hypothesis:
            #    print(hypothesis)
            #    print(label)
        else:
            if label == 0:
                num_entails_wrong += 1
            elif label == 1:
                num_contradicts_wrong += 1
            else:
                num_neutral_wrong += 1
            num_wrong += 1
            avg_confidence_wrong += findConfidence(example['predicted_scores'])
        
    print("Entails: " + str(num_entails_right) + " Contradicts: " + str(num_contradicts_right) + " Neutral: " + str(num_neutral_right))
    print("Entails: " + str(num_entails_wrong) + " Contradicts: " + str(num_contradicts_wrong) + " Neutral: " + str(num_neutral_wrong))
    print("Confidence right: " + str((avg_confidence_right / num_right)) + " Confidence wrong: " + str((avg_confidence_wrong / num_wrong)))
    print("Number of times predicted entails: " + str(num_pred_entails))
    print("Number of times predicted contradicts: " + str(num_pred_contradicts))
    print(count)

def findConfidence(scores):
    scores.sort()
    return scores[2] - scores[1]

'''
    0: Entails
    1: Contradicts
    2: Neutral
'''

if __name__ == "__main__":
    read_eval_output()