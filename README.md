# K-Style Hub AI Developer Technical Test

## Folder Solution_2  
Contains:  
- Raw dataset  
- Dataset converted to Excel format  
- Preprocessing code  
- Cleaned dataset  

## Folder Solution_3a  
Contains:  
- Cleaned dataset  
- Code for predicting **MathScore** based on features from 1st (Gender) to 11th (WklyStudyHours) columns  

## Folder Solution_3b  
Contains:  
- Cleaned dataset  
- Code for classifying **WklyStudyHours** based on **MathScore**, **ReadingScore**, and **WritingScore**  
- Saved model in multiple formats: `.h5`, `.keras`, `SavedModel`, `TensorFlowJS`, and `.tflite`  
- `classification.py` script for interactive classification  
- `requirements.txt` file to install dependencies for running `classification.py`

**Installation and Usage to Run `classification.py`**
1. Clone the repository.
    ```
    git clone https://github.com/sylviahamidah/kstyle_technical_test.git
    cd kstyle_technical_test
    cd Solution_3b
    ```
2. Create a virtual environment and activate it.
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
3. Install the required dependencies. If you cannot install TensorFlow with the required version specified in the requirements.txt file, then Python needs to be upgraded to version 3.11.8 or above.
    ```
    pip install -r requirements.txt
    ```
4. Run the script with the following command.
    ```
    # Format
    python classification.py --math <MathScore> --reading <ReadingScore> --writing <WritingScore>
    # Example
    python classification.py --math 70 --reading 70 --writing 70
    ```

## Folder Solution_3c  
Contains:  
- Code for classifying images of cats and dogs  
- Saved model in multiple formats: `.h5`, `.keras`, `SavedModel`, `TensorFlowJS`, and `.tflite`  

## Folder Solution_3d  
Contains:  
- Code for classifying product reviews as **recommended** or **not recommended**  
- Saved model in multiple formats: `.h5`, `.keras`, `SavedModel`, `TensorFlowJS`, and `.tflite`  
- Link to the dataset used for training
