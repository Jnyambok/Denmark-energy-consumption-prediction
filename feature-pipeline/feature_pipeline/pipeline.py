import datetime
from typing import Optional
import fire
import pandas as pd

from feature_pipeline.etl import cleaning,load,extract,validation
from feature_pipeline import utils

logger = utils.get_logger(__name__)

#This is a tutorial



def run(
        export_end_reference_datetime: Optional[datetime.datetime] = None,
        days_delay : int = 15,
        days_export: int = 30,
        url:str ="https://api.energidataservice.dk/dataset/ConsumptionDE35Hour",
        feature_group_version:int = 1,

) -> dict:
   """    
   Extract data from the API.
    Args:
        export_end_reference_datetime: The end reference datetime of the export window. If None, the current time is used.
            Because the data is always delayed with "days_delay" days, this date is used only as a reference point.
            The real extracted window will be computed as [export_end_reference_datetime - days_delay - days_export, export_end_reference_datetime - days_delay].
        days_delay: Data has a delay of N days. Thus, we have to shift our window with N days.
        days_export: The number of days to export.
        url: The URL of the API.
        feature_group_version: The version of the feature store feature group to save the data to.
    Returns:
          A dictionary containing metadata of the pipeline.
          """
   logger.info(f"Starting data extraction from API....")
   data, metadata = extract.from_api(
      export_end_reference_datetime,days_delay,days_export,url
   )
   logger.info(f"Successfully extracted data from API")


   #Data Transformation
   logger.info(f"Starting data transformation......")
   data = transform(data)
   logger.info(f"Successfully transformed data")

   #Validation Expectation suite
   logger.info(f"Starting validation expectation suite......")
   validation_expectation_suite = validation.build_expectation_suite()
   logger.info(f"Successfully built validation expectation suite")

   #Validating the data and loading it to feature store
   logger.info(f"Starting data validation......")
   load.to_feature_store(
      data,
      validation_expectation_suite = validation_expectation_suite,
      feature_group_version = feature_group_version,
   )
   metadata["feature_group_version"] = feature_group_version
   logger.info(f"Successfully loaded data to feature store")


   #Finishing up the pipeline
   logger.info(f"Wrapping up the pipeline......")
   utils.save_json(metadata, file_name = "feature_pipeline_metadata.json")
   logger.info("Done!")

   return metadata

def transform(data :pd.DataFrame):
      """
      Wrapper containing all the Transformations from the ETL Pipeline.
      
      """
      data = cleaning.rename_columns(data)
      data = cleaning.cast_columns(data)
      data = cleaning.encode_area_column(data)
      return data


#Just testing this pipeline
if __name__ == "__main__":
    fire.Fire(run)


