# Loan Approval Prediction

This project predicts loan approvals using machine learning. It uses a Support Vector Classifier (SVC) model trained on a loan dataset.

## Dataset

The dataset used for this project contains information about loan applicants, such as their income, education, credit history, and loan status. The dataset was cleaned and preprocessed before training the model.

## Model

The project utilizes an SVC model with a linear kernel. The data is standardized before being fed to the model using `StandardScaler`. To evaluate the model's performance, 5-fold cross-validation is performed, and the average accuracy is reported.

## Results

The model achieved an average cross-validation accuracy of around 81% (this value might slightly vary due to randomness). This indicates that the model can effectively predict loan approvals based on the provided features.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.
