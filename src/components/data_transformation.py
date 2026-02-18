import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer # Used to apply different transformations to different columns
from sklearn.impute import SimpleImputer # Used to fill missing values
from sklearn.pipeline import Pipeline # Used to create transformation pipelines
from sklearn.preprocessing import OneHotEncoder,StandardScaler # Used to encode categorical data & scale numeric data

from src.exception import CustomException
from src.logger import logging
import os
import dill

from src.utils import save_object # Utility function to save objects like preprocessor

# Configuration class to store file paths
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig() # Initialize configuration

    def get_data_transformer_object(self):
        '''
        This function creates preprocessing pipelines
        
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # ---------------- NUMERIC PIPELINE ----------------
            # Step 1: Replace missing values with median
            # Step 2: Scale numeric features
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            # ---------------- CATEGORICAL PIPELINE ----------------
            # Step 1: Replace missing values with most frequent value
            # Step 2: Convert categories into numbers using OneHotEncoder
            # Step 3: Scale encoded values
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            
            # Combine numeric and categorical pipelines
            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object() # Get preprocessing object


            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            # Separate input features and target (TRAIN)
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            # Separate input features and target (TEST)
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            # Fit on training data and transform
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            
            # Only transform test data (IMPORTANT: do not fit again)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            # Combine transformed features with target column
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            # Save preprocessor object for future prediction use
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            # Return transformed arrays + preprocessor path
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
        
        
#         This file is responsible for:

# 1️⃣ Creating preprocessing pipelines
# 2️⃣ Applying transformations on train and test data
# 3️⃣ Saving the preprocessor object
# 4️⃣ Returning transformed arrays for model training

