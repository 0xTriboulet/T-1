# T-1: Intelligent VM Detection with DTC

## Project Overview

**T-1** is a C++ project inspired by the **T-1 Battlefield Robot**, also known as the **T-1 Ground Assault Vehicle**, which is a fully autonomous ground offensive system developed by Cyber Research Systems. This project simulates part of the logic behind the T-1 by leveraging a **Decision Tree Classifier (DTC)** trained using Python's **scikit-learn** library to implement VM detection in a C++ environment.

The model is trained to predict whether the system is running on a virtual machine based on the number of processes per user. The trained model is then used to implement VM detection in the C++ file `VmDetection.cxx`. The decision tree logic is extracted and converted into conditional statements that can be applied in any language, allowing the developer to integrate machine learning predictions into a C++ application.

### Key Features:
- **Decision Tree Classifier (DTC) Training**: A Python script uses `scikit-learn` to train a decision tree model based on system data, which can be visualized and implemented in C++.
- **VM Detection**: Implements the decision tree logic in the function `VmDetection` to determine whether the system is running on bare metal or inside a virtual machine.
- **Self-Deletion and Shellcode Execution**: Based on the VM detection result, the system can either execute shellcode or self-delete when running in a virtualized environment.

## Project Structure

- **`main.cxx`**: The main entry point of the project, which handles process and user counting, executes VM detection, and takes appropriate action based on the result.
- **`intelligence.h`**: Contains declarations for system functions such as `GetProcessCountViaSnapShot`, `GetUniqueUserCountViaSnapshot`, and `VmDetection`.
- **`VmDetection.cxx`**: Implements the `VmDetection` logic based on the decision tree classifier's learnings.

- **Python Scripts**:
    - The `python` directory contains scripts for training the decision tree classifier on system data, visualizing the model, and exporting the learned logic for use in C++.

## Decision Tree Classifier Logic

The `VmDetection` function in C++ is based on the decision tree classifier model, which uses the `process_count_per_user` as the main feature to detect whether the system is virtualized or not:

```c++
BOOL VmDetection(float process_count_per_user){
	
	// Conditional extracted from DecisionTreeClassifier learnings
	if ((process_count_per_user > 75.3) || (process_count_per_user > 61.45 && process_count_per_user <= 69.3)){
		
		PRINT("[i] Running on bare metal machine!\n");
		return TRUE;
		
	}

	return FALSE;
}
```

This logic is derived from the decision tree model's learnings and applied to the `VmDetection` function in C++.

## Dependencies

- **C++**: The project is written in C++ and utilizes standard C++ libraries for system interaction.
- **scikit-learn (Python)**: Used for training the decision tree model. The `python` directory contains all scripts and data needed to train and visualize the model.

## Setup Instructions

### Step 1: Train the Decision Tree Classifier
The first step is to train the decision tree classifier using the provided Python scripts. These scripts are located in the `python` directory:

```bash
cd .\python\DecisionTree
python decision_tree.py
```

This script will train the model based on the collected system data and output a visualization of the decision tree, which you can use to understand the model's decision-making process.

### Step 2: Build the C++ Project
Once the decision tree logic has been extracted and implemented in `VmDetection.cxx`, you can build the C++ project using a standard C++ compiler.

```bash
mingw32-make.exe
```

### Step 3: Run the Executable
After building the project, you can run the executable to perform VM detection and trigger appropriate actions:

```bash
./build/T-1.exe
```

## Special Thanks

Special thanks to all the researchers who voluntarily ran the Python script to collect the necessary data for training the Decision Tree Classifier. Your contributions made this project possible!

## License

T-1 is licensed under the MIT License.

---

*Inspired by the T-1 Ground Assault Vehicle, the first Terminator-class robot.*  
More information: [T-1 Terminator](https://terminator.fandom.com/wiki/T-1)

