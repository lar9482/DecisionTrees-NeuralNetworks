import matplotlib.pyplot as plt
import os
import sys
import math

def graph_DT_data(data, num_instances, domain):

    possibleColors =['r', 'b', 'g', 'm', 'c', 'k', 'y', '#FFA500']
    currentColor = 0
    legendList = []

    for info_gain_metric in data.keys():
        all_instances = []
        all_training_accuracies = []
        all_testing_accuracies = []
        for unit in data[info_gain_metric]:
            all_instances.append(unit[2])
            all_training_accuracies.append(unit[0])
            all_testing_accuracies.append(unit[1])

        plt.plot(all_instances, all_training_accuracies, color = possibleColors[currentColor], label = info_gain_metric.name + "_TN")
        currentColor += 1

        plt.plot(all_instances, all_testing_accuracies, possibleColors[currentColor], label = info_gain_metric.name + "_TT")
        currentColor += 1

        legendList.append(info_gain_metric.name + "_TN")
        legendList.append(info_gain_metric.name + "_TT")

    plt.legend(bbox_to_anchor=(1.15, 1.15), loc='upper right')
    plt.xlabel('Number of Instances')
    plt.ylabel('Accuracy')
    
    plt.xlim(0, 4600)
    plt.ylim(0, 1.05)

    filePath = os.path.join(sys.path[0], "Results", "DecisionTree", domain.__name__)
    plt.savefig(filePath)
    plt.clf()


def graph_NN_data(data_dict, domain):
    possibleColors =['r', 'b', 'g', 'm', 'c', 'k']
    currentColor = 0
    legendList = []

    for node_option in data_dict.keys():
        all_alphas = []
        all_training_accuracies = []
        all_testing_accuracies = []
        for unit in data_dict[node_option]:
            all_alphas.append(unit[2])
            all_training_accuracies.append(unit[0])
            all_testing_accuracies.append(unit[1])

        plt.plot(all_alphas, all_training_accuracies, color = possibleColors[currentColor], label = node_option + "_TN")
        currentColor += 1

        plt.plot(all_alphas, all_testing_accuracies, possibleColors[currentColor], label = node_option + "_TT")
        currentColor += 1

        legendList.append(node_option + "_TN")
        legendList.append(node_option + "_TT")

    plt.legend(bbox_to_anchor=(1.15, 1.15), loc='upper right')
    plt.xlabel('Learning Rate(Alpha)')
    plt.ylabel('Accuracy')
    
    plt.xlim(-0.05, 1.05)
    plt.ylim(-0.05, 1.05)

    filePath = os.path.join(sys.path[0], "Results", "NN", domain.__name__)
    plt.savefig(filePath)
    plt.clf()

def graph_training_testing_NN_data(domain_name, training, testing, node_options, alpha, decay):
    x = list(range(1, len(training)+1))

    #Plotting
    plt.plot(x, training, color = 'r', label='Training')
    plt.plot(x, testing, color = 'b', label='Testing')

    plt.legend(bbox_to_anchor=(1.15, 1.15), loc='upper right')

    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')

    file_name = '_'.join([domain_name, node_options, alpha, decay])
    filePath = os.path.join(sys.path[0], "Results", "NN", domain_name, file_name + '.png')
    plt.savefig(filePath)
    plt.clf()